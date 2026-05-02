#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RPU · Resonant Processing Unit (v0.7 OPTIMAL)

Reference implementation for an EDS/EDC-inspired resonant allocation engine.

Includes:
- spectral coherence metrics
- ethics / stress / non-parasitism gates
- civilization and life-support energy floors
- optional resonant oscillator core
- deterministic demo scenario

License: Apache-2.0
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple
from collections import deque

import numpy as np

TAU = 2 * np.pi
EPS = 1e-12


# ------------------------------------------------------------
# Utilities
# ------------------------------------------------------------

def clamp(x: float, lo: float, hi: float) -> float:
    return float(max(lo, min(hi, x)))


def safe_zscore(v: np.ndarray) -> np.ndarray:
    v = np.asarray(v, dtype=float).ravel()
    return (v - v.mean()) / (v.std() + EPS)


def wrap_pi(a: np.ndarray) -> np.ndarray:
    return (a + np.pi) % (2 * np.pi) - np.pi


def power_iteration_radius(
    A: np.ndarray,
    iters: int = 128,
    rng: Optional[int] = None
) -> float:
    rg = np.random.default_rng(rng)
    x = rg.normal(size=A.shape[0])
    x /= np.linalg.norm(x) + EPS

    r = 0.0

    for _ in range(iters):
        x = A @ x
        n = np.linalg.norm(x) + EPS
        x /= n
        r = n

    return float(r)


def quantize_balanced(x: np.ndarray, t1: float = 0.33) -> np.ndarray:
    q = np.zeros_like(x, dtype=np.int8)
    q[x >= t1] = 1
    q[x <= -t1] = -1
    return q


def quantize_W(W: np.ndarray, thresh: float = 0.2) -> np.ndarray:
    S = np.zeros_like(W, dtype=np.int8)
    S[W >= thresh] = 1
    S[W <= -thresh] = -1
    return S


# ------------------------------------------------------------
# Spectral metrics
# ------------------------------------------------------------

def spectral_psd(x: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Return normalized PSD and FFT phase.
    """
    x = np.asarray(x, dtype=float).ravel()
    X = np.fft.fft(x)

    amp = np.abs(X)
    psd = amp ** 2
    psd /= psd.sum() + EPS

    phase = np.angle(X)

    return psd, phase


def spectral_entropy_norm(psd: np.ndarray) -> float:
    """
    Normalized spectral entropy in [0, 1].
    """
    psd = np.asarray(psd, dtype=float).ravel()
    n = len(psd)

    entropy = -np.sum(psd * np.log2(psd + EPS))
    entropy_norm = entropy / (np.log2(n) + EPS)

    return clamp(entropy_norm, 0.0, 1.0)


def resonance_order(psd: np.ndarray) -> float:
    """
    Resonance order = 1 - normalized spectral entropy.
    """
    return float(1.0 - spectral_entropy_norm(psd))


def phase_mismatch_norm(phase: np.ndarray, ref_phase: np.ndarray) -> float:
    """
    Mean circular phase mismatch normalized to [0, 1].
    """
    phase = np.asarray(phase, dtype=float).ravel()
    ref_phase = np.asarray(ref_phase, dtype=float).ravel()

    if phase.shape != ref_phase.shape:
        raise ValueError("phase and ref_phase must have the same shape")

    d = np.abs(wrap_pi(phase - ref_phase))
    return clamp(float(np.mean(d) / np.pi), 0.0, 1.0)


def coherence_time_domain(x: np.ndarray) -> float:
    """
    Simple time-domain coherence proxy.

    High if signal energy is concentrated in structured peaks.
    """
    x = np.asarray(x, dtype=float).ravel()
    z = safe_zscore(x)

    abs_z = np.abs(z)
    k = max(1, int(0.05 * len(z)))

    top = np.partition(abs_z, -k)[-k:].sum()
    total = abs_z.sum() + EPS

    concentration = top / total

    return clamp(0.2 + 0.8 * concentration, 0.0, 1.0)


# ------------------------------------------------------------
# Project model
# ------------------------------------------------------------

@dataclass
class Project:
    name: str
    pattern: np.ndarray
    horizon: float
    expansion: float = 1.0
    eta: float = 1.0
    impact: Dict[str, float] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)


# ------------------------------------------------------------
# Gates
# ------------------------------------------------------------

class EthicsGate:
    """
    Formal ethics gate.

    It estimates:
    - future debt
    - phase mismatch
    - time-domain coherence

    This is not moral judgment.
    It is a structural filter against unstable future debt.
    """

    def __init__(
        self,
        N: int,
        rng: np.random.Generator,
        generations: float = 4.0,
        horizon_factor: float = 0.35,
        max_future_debt: float = 2.5,
        max_phase_mismatch: float = 0.30,
        min_time_coherence: float = 0.25,
    ):
        self.N = int(N)
        self.generations = float(generations)
        self.horizon_factor = float(horizon_factor)
        self.max_future_debt = float(max_future_debt)
        self.max_phase_mismatch = float(max_phase_mismatch)
        self.min_time_coherence = float(min_time_coherence)

        self.clean_fft_phase = rng.uniform(-np.pi, np.pi, self.N)

    def evaluate(
        self,
        pattern: np.ndarray,
        horizon: float
    ) -> Tuple[bool, Dict[str, float], List[str]]:
        p = np.asarray(pattern, dtype=float).ravel()

        if p.size != self.N:
            raise ValueError(f"pattern size mismatch: expected {self.N}, got {p.size}")

        psd, phase = spectral_psd(p)

        se_n = spectral_entropy_norm(psd)
        r_order = 1.0 - se_n
        time_coh = coherence_time_domain(p)
        phase_mismatch = phase_mismatch_norm(phase, self.clean_fft_phase)

        h = clamp(float(horizon) / 10.0, 0.0, 1.0)

        future_debt = float(
            se_n
            * np.exp(
                self.horizon_factor
                * self.generations
                * (0.3 + 0.7 * h)
            )
        )

        ok = True
        reasons: List[str] = []

        if future_debt >= self.max_future_debt:
            ok = False
            reasons.append("ETH_FUTURE_DEBT")

        if phase_mismatch >= self.max_phase_mismatch:
            ok = False
            reasons.append("ETH_PHASE_MISMATCH")

        if time_coh < self.min_time_coherence:
            ok = False
            reasons.append("ETH_LOW_TIME_COHERENCE")

        stats = {
            "spec_entropy_norm": float(se_n),
            "r_order": float(r_order),
            "time_coherence": float(time_coh),
            "phase_mismatch": float(phase_mismatch),
            "future_debt": float(future_debt),
        }

        return ok, stats, reasons


class AntiStressGate:
    """
    Anti-stress gate.

    Estimates conflict pressure from measurable deltas.
    """

    def __init__(
        self,
        weights: Tuple[float, float, float, float] = (0.30, 0.30, 0.20, 0.20),
        s_min: float = 0.45,
    ):
        self.a, self.b, self.c, self.d = map(float, weights)
        self.s_min = float(s_min)

    def evaluate(self, impact: Dict[str, float]) -> Tuple[bool, Dict[str, float], List[str]]:
        conflict_risk = (
            self.a * float(impact.get("res_competition", 0.0))
            + self.b * float(impact.get("inequality_delta", 0.0))
            + self.c * float(impact.get("externality_damage", 0.0))
            + self.d * float(impact.get("polarization_score", 0.0))
        )

        conflict_risk = clamp(conflict_risk, 0.0, 1.0)
        s_factor = clamp(1.0 - conflict_risk, 0.0, 1.0)

        ok = s_factor >= self.s_min
        reasons = [] if ok else ["STRESS_HIGH_CONFLICT_RISK"]

        return ok, {
            "conflict_risk": conflict_risk,
            "s_factor": s_factor,
        }, reasons


class NonParasitismGate:
    """
    Non-parasitism gate.

    Checks whether externality + inequality exceeds public benefit.
    """

    def __init__(self, parasite_max: float = 0.25):
        self.parasite_max = float(parasite_max)

    def evaluate(self, impact: Dict[str, float]) -> Tuple[bool, Dict[str, float], List[str]]:
        externality = float(impact.get("externality_damage", 0.0))
        inequality = float(impact.get("inequality_delta", 0.0))
        benefit = float(impact.get("public_benefit", 0.0))

        parasite_score = max(0.0, externality + inequality - benefit)
        parasite_score = clamp(parasite_score, 0.0, 1.0)

        ok = parasite_score <= self.parasite_max
        reasons = [] if ok else ["PARASITE_EXCESS"]

        return ok, {"parasite_score": parasite_score}, reasons


# ------------------------------------------------------------
# RPU core
# ------------------------------------------------------------

class RPUCore:
    """
    Resonant oscillator core.

    Optional layer for phase-based dynamics.
    """

    def __init__(
        self,
        N: int,
        seed: int = 42,
        k_global: float = 0.6,
        dt: float = 5e-3,
        sigma: float = 0.02,
        sparsify: float = 0.8,
        threshold: Optional[float] = None,
        norm_iters: int = 96,
        gamma: float = np.pi * 0.3,
        ternary: bool = True,
        wq_thresh: float = 0.25,
        state_tau: float = 0.33,
    ):
        self.rng = np.random.default_rng(seed)
        self.N = int(N)
        self.kg = float(k_global)
        self.dt = float(dt)
        self.sigma = float(sigma)
        self.gamma = float(gamma)

        self.omega = self.rng.normal(TAU * 1.0, TAU * 0.10, self.N)
        self.theta = self.rng.uniform(0, TAU, self.N)

        W = self.rng.normal(0.0, 1.0, (self.N, self.N))
        W = (W + W.T) / 2.0
        np.fill_diagonal(W, 0.0)
        W /= np.max(np.abs(W)) + EPS

        if threshold is not None:
            W = W * (np.abs(W) >= float(threshold))
        elif sparsify > 0.0:
            q = np.quantile(np.abs(W), float(sparsify))
            W = W * (np.abs(W) >= q)

        rho = power_iteration_radius(W, iters=int(norm_iters), rng=seed)

        if rho > 1.0:
            W = W / (rho + EPS)

        self.W = W
        self.Wq = quantize_W(self.W, thresh=float(wq_thresh))

        self.use_ternary = bool(ternary)
        self.state_tau = float(state_tau)
        self.s = quantize_balanced(np.cos(self.theta), t1=self.state_tau)

        self.ext_freq = np.zeros(self.N)
        self.ext_amp = np.zeros(self.N)
        self.ext_phase = np.zeros(self.N)
        self.t = 0.0

    def _ternary_controller(self) -> np.ndarray:
        u_raw = self.Wq @ self.s
        degree = np.maximum(np.sum(np.abs(self.Wq), axis=1), 1)

        x = u_raw / degree
        u = quantize_balanced(x, t1=0.2).astype(float)

        return 0.15 * u

    def _dtheta(
        self,
        theta: np.ndarray,
        ext_phase: np.ndarray,
        amp_now: np.ndarray
    ) -> np.ndarray:
        phase_diff = theta[:, None] - theta[None, :]
        coupling = np.sum(self.W * np.sin(-phase_diff - self.gamma), axis=1)
        pll = amp_now * np.sin(ext_phase - theta)

        return self.omega + self.kg * coupling + pll

    def step(self, steps: int = 1, stability_guard: bool = True) -> None:
        for _ in range(int(steps)):
            dt = self.dt
            amp_now = self.ext_amp

            if stability_guard:
                factor = (self.kg + float(np.max(np.abs(amp_now)))) * dt

                if factor > 0.1:
                    dt = 0.1 / max(
                        self.kg + float(np.max(np.abs(amp_now))),
                        EPS
                    )

            phi_bump = self._ternary_controller() if self.use_ternary else 0.0

            self.ext_phase = (
                self.ext_phase + dt * self.ext_freq + phi_bump
            ) % TAU

            k1 = self._dtheta(self.theta, self.ext_phase, amp_now)
            theta_predict = (self.theta + dt * k1) % TAU
            k2 = self._dtheta(theta_predict, self.ext_phase, amp_now)

            dtheta = 0.5 * (k1 + k2)
            dtheta += self.sigma * self.rng.normal(0.0, 1.0, self.N)

            self.theta = (self.theta + dt * dtheta) % TAU
            self.t += dt

            if self.use_ternary:
                self.s = quantize_balanced(
                    np.cos(self.theta),
                    t1=self.state_tau
                )

    def imprint(self, pattern: np.ndarray, gain: float = 0.25) -> None:
        v = safe_zscore(np.asarray(pattern, dtype=float).ravel())

        if v.size != self.N:
            raise ValueError("pattern size mismatch")

        H = np.outer(v, v)
        np.fill_diagonal(H, 0.0)
        H /= np.max(np.abs(H)) + EPS

        self.W = np.tanh(self.W + float(gain) * H)
        self.Wq = quantize_W(self.W, thresh=0.25)


# ------------------------------------------------------------
# Teleological allocator
# ------------------------------------------------------------

class TeleologicalAllocator:
    """
    Allocates energy/resources while preserving floors and applying gates.
    """

    def __init__(
        self,
        ethics: EthicsGate,
        stress: AntiStressGate,
        parasite: NonParasitismGate,
        e_base_frac: float = 0.25,
        e_civ_frac: float = 0.15,
        p_r: float = 1.25,
        p_eta: float = 1.0,
        p_h: float = 1.4,
        p_exp: float = 1.15,
        p_s: float = 1.0,
        p_benefit: float = 0.9,
    ):
        self.ethics = ethics
        self.stress = stress
        self.parasite = parasite

        self.e_base_frac = float(e_base_frac)
        self.e_civ_frac = float(e_civ_frac)

        if self.e_base_frac < 0 or self.e_civ_frac < 0:
            raise ValueError("Energy floors must be non-negative")

        if self.e_base_frac + self.e_civ_frac >= 0.95:
            raise ValueError("Energy floors must leave at least 5% allocatable energy")

        self.p_r = float(p_r)
        self.p_eta = float(p_eta)
        self.p_h = float(p_h)
        self.p_exp = float(p_exp)
        self.p_s = float(p_s)
        self.p_benefit = float(p_benefit)

    def allocate(self, total_energy: float, projects: List[Project]) -> Dict[str, Any]:
        total_energy = float(total_energy)

        e_base = total_energy * self.e_base_frac
        e_civ = total_energy * self.e_civ_frac
        e_available = max(total_energy - e_base - e_civ, 0.0)

        allocations: Dict[str, float] = {p.name: 0.0 for p in projects}
        diagnostics: Dict[str, Dict[str, Any]] = {}
        blocked: Dict[str, List[str]] = {}

        scored: List[Tuple[str, float]] = []

        for p in projects:
            reasons: List[str] = []

            ok_eth, stats_eth, reasons_eth = self.ethics.evaluate(
                p.pattern,
                p.horizon
            )

            ok_stress, stats_stress, reasons_stress = self.stress.evaluate(
                p.impact
            )

            ok_np, stats_np, reasons_np = self.parasite.evaluate(
                p.impact
            )

            reasons.extend(reasons_eth + reasons_stress + reasons_np)

            hard_ok = ok_eth and ok_stress and ok_np

            r_order_value = float(stats_eth["r_order"])
            s_factor = float(stats_stress["s_factor"])

            eta = clamp(float(p.eta), 0.0, 1.0)
            horizon = clamp(float(p.horizon) / 10.0, 0.0, 1.0)
            expansion = clamp(float(p.expansion) / 10.0, 0.0, 1.0)
            benefit = clamp(float(p.impact.get("public_benefit", 0.0)), 0.0, 1.0)

            q_score = 0.0

            if hard_ok:
                q_score = (
                    (r_order_value ** self.p_r)
                    * (eta ** self.p_eta)
                    * ((horizon + EPS) ** self.p_h)
                    * ((expansion + EPS) ** self.p_exp)
                    * (s_factor ** self.p_s)
                    * ((benefit + EPS) ** self.p_benefit)
                )

            diagnostics[p.name] = {
                "hard_ok": bool(hard_ok),
                "reasons": reasons,
                "ethics": stats_eth,
                "stress": stats_stress,
                "non_parasitism": stats_np,
                "eta": eta,
                "horizon_norm": horizon,
                "expansion_norm": expansion,
                "public_benefit": benefit,
                "q_score": float(q_score),
                "tags": list(p.tags),
            }

            if hard_ok:
                scored.append((p.name, q_score))
            else:
                blocked[p.name] = reasons if reasons else ["BLOCKED_UNKNOWN"]

        total_score = sum(score for _, score in scored) + EPS

        for name, score in scored:
            allocations[name] = e_available * (score / total_score)

        return {
            "total_energy": total_energy,
            "e_base": e_base,
            "e_civ": e_civ,
            "e_available": e_available,
            "allocations": allocations,
            "diagnostics": diagnostics,
            "blocked": blocked,
        }


# ------------------------------------------------------------
# Demo projects
# ------------------------------------------------------------

def build_demo_projects(N: int, seed: int) -> List[Project]:
    rng = np.random.default_rng(seed)
    x = np.linspace(0, TAU, N, endpoint=False)

    pat_edu = np.sin(3 * x) + 0.2 * np.sin(11 * x)
    pat_infra = np.sin(7 * x + np.pi / 4) + 0.15 * np.sin(2 * x)

    pat_noise = rng.normal(0, 1, N)
    pat_click = np.sign(np.sin(19 * x)) + 0.05 * rng.normal(0, 1, N)

    return [
        Project(
            name="Education_Engineering_Expansion",
            pattern=pat_edu,
            horizon=8.0,
            expansion=7.0,
            eta=0.92,
            impact={
                "res_competition": 0.05,
                "inequality_delta": 0.04,
                "externality_damage": 0.03,
                "polarization_score": 0.04,
                "public_benefit": 0.85,
            },
            tags=["civilization", "kids", "future"],
        ),
        Project(
            name="Eco_Future_Infrastructure",
            pattern=pat_infra,
            horizon=7.0,
            expansion=6.0,
            eta=0.87,
            impact={
                "res_competition": 0.08,
                "inequality_delta": 0.03,
                "externality_damage": 0.05,
                "polarization_score": 0.04,
                "public_benefit": 0.75,
            },
            tags=["infrastructure", "stability"],
        ),
        Project(
            name="Doomscroll_Content_Farm",
            pattern=pat_click,
            horizon=0.5,
            expansion=0.5,
            eta=0.70,
            impact={
                "res_competition": 0.35,
                "inequality_delta": 0.25,
                "externality_damage": 0.20,
                "polarization_score": 0.30,
                "public_benefit": 0.05,
            },
            tags=["attention", "monetization"],
        ),
        Project(
            name="Entropy_Chaos_Accelerator",
            pattern=pat_noise,
            horizon=0.2,
            expansion=0.2,
            eta=0.60,
            impact={
                "res_competition": 0.40,
                "inequality_delta": 0.30,
                "externality_damage": 0.30,
                "polarization_score": 0.35,
                "public_benefit": 0.00,
            },
            tags=["chaos"],
        ),
    ]


# ------------------------------------------------------------
# CLI / Demo
# -----------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="RPU v0.7 OPTIMAL — EDS/EDC resonant allocation demo"
    )

    p.add_argument("--N", type=int, default=256)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--clean-seed", dest="clean_seed", type=int, default=None)
    p.add_argument("--energy", type=float, default=100.0)
    p.add_argument("--show-all", action="store_true")

    p.add_argument("--e-base-frac", dest="e_base_frac", type=float, default=0.25)
    p.add_argument("--e-civ-frac", dest="e_civ_frac", type=float, default=0.15)

    p.add_argument("--generations", type=float, default=4.0)
    p.add_argument("--horizon-factor", dest="horizon_factor", type=float, default=0.35)
    p.add_argument("--max-future-debt", dest="max_future_debt", type=float, default=2.5)
    p.add_argument("--max-phase-mismatch", dest="max_phase_mismatch", type=float, default=0.30)
    p.add_argument("--min-time-coherence", dest="min_time_coherence", type=float, default=0.25)

    p.add_argument("--w-res", dest="w_res", type=float, default=0.30)
    p.add_argument("--w-ineq", dest="w_ineq", type=float, default=0.30)
    p.add_argument("--w-ext", dest="w_ext", type=float, default=0.20)
    p.add_argument("--w-pol", dest="w_pol", type=float, default=0.20)
    p.add_argument("--s-min", dest="s_min", type=float, default=0.45)

    p.add_argument("--parasite-max", dest="parasite_max", type=float, default=0.25)

    p.add_argument("--p-r", dest="p_r", type=float, default=1.25)
    p.add_argument("--p-eta", dest="p_eta", type=float, default=1.0)
    p.add_argument("--p-h", dest="p_h", type=float, default=1.4)
    p.add_argument("--p-exp", dest="p_exp", type=float, default=1.15)
    p.add_argument("--p-s", dest="p_s", type=float, default=1.0)
    p.add_argument("--p-benefit", dest="p_benefit", type=float, default=0.9)

    return p


def demo_run(args: argparse.Namespace) -> None:
    rng = np.random.default_rng(int(args.seed))

    ethics = EthicsGate(
        N=int(args.N),
        rng=rng,
        generations=float(args.generations),
        horizon_factor=float(args.horizon_factor),
        max_future_debt=float(args.max_future_debt),
        max_phase_mismatch=float(args.max_phase_mismatch),
        min_time_coherence=float(args.min_time_coherence),
    )

    if args.clean_seed is not None:
        clean_rng = np.random.default_rng(int(args.clean_seed))
        ethics.clean_fft_phase = clean_rng.uniform(-np.pi, np.pi, int(args.N))

    stress = AntiStressGate(
        weights=(
            float(args.w_res),
            float(args.w_ineq),
            float(args.w_ext),
            float(args.w_pol),
        ),
        s_min=float(args.s_min),
    )

    parasite = NonParasitismGate(
        parasite_max=float(args.parasite_max)
    )

    allocator = TeleologicalAllocator(
        ethics=ethics,
        stress=stress,
        parasite=parasite,
        e_base_frac=float(args.e_base_frac),
        e_civ_frac=float(args.e_civ_frac),
        p_r=float(args.p_r),
        p_eta=float(args.p_eta),
        p_h=float(args.p_h),
        p_exp=float(args.p_exp),
        p_s=float(args.p_s),
        p_benefit=float(args.p_benefit),
    )

    projects = build_demo_projects(int(args.N), int(args.seed))

    out = allocator.allocate(
        total_energy=float(args.energy),
        projects=projects
    )

    print("\n=== RPU v0.7 OPTIMAL · Allocation Report ===")
    print(
        f"Total: {out['total_energy']:.2f} | "
        f"E_BASE: {out['e_base']:.2f} | "
        f"E_CIV: {out['e_civ']:.2f} | "
        f"Available: {out['e_available']:.2f}"
    )

    print("\nAllocations:")
    for name, value in sorted(out["allocations"].items(), key=lambda kv: -kv[1]):
        print(f" - {name}: {value:.6f}")

    if out["blocked"]:
        print("\nBlocked:")
        for name, reasons in out["blocked"].items():
            print(f" - {name}: {', '.join(reasons)}")

    if args.show_all:
        print("\nDiagnostics:")
        for name, diag in out["diagnostics"].items():
            print(f"\n[{name}]")
            print(diag)


def main() -> None:
    args = build_parser().parse_args()
    demo_run(args)


if __name__ == "__main__":
    main()
