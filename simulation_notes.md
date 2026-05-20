# Simulation Notes

Minimal Reproducible Oscillator Model

---

## 1. Purpose

This document defines a minimal simulation setup to reproduce synchronization dynamics corresponding to EDS/EDC.

The model tests whether coordinated subsystem dynamics can accumulate and retain structural integrity faster than destabilizing dissipation propagates over time.

---

## 2. Model

Use a Kuramoto-type system:

dφᵢ/dt = ωᵢ + (K/N) Σⱼ sin(φⱼ − φᵢ) + F_ext sin(ω_ext t − φᵢ) + η

---

## 3. Initialization

- N = 100–1000 oscillators

- ωᵢ sampled from normal distribution

- φᵢ(0) uniformly random in [0, 2π]

---

## 4. Parameters

- K: 0.1 → 5.0

- F_ext: 0 → small (0.1–1.0)

- ω_ext ≈ mean(ωᵢ)

- η: small noise (0.01–0.1)

---

## 5. Measurement

Compute:

R(t) = |(1/N) Σ exp(iφᵢ)|

Track:

- R(t)

- convergence time t_conv

- retention time t_ret

Operational meaning:

- R(t) measures synchronization of subsystem phases;

- R(t) is a measurable proxy for coordinated structural integrity;

- R(t) supports interpretation of C(t), but does not replace the full meaning of C(t).

---

## 6. Procedure

1. Run baseline:

F_ext = 0

2. Run with forcing:

F_ext > 0

3. Compare:

- R(t)

- t_conv

4. Turn off forcing and measure:

t_ret

---

## 7. Expected Behavior

- With forcing → faster synchronization

- Higher R_max

- Longer retention after forcing removal

Operational interpretation:

- synchronization should accumulate faster than destabilizing dispersion;

- retained synchronization should persist after forcing removal;

- structural regeneration must remain ahead of dissipation over time.

---

## 8. Interpretation

R(t) serves as a measurable synchronization proxy supporting C(t).

Within this framework:

C(t)

represents:

- structural regeneration;

- retained structural continuity;

- restorative structural capacity.

The observed behavior maps to:

C(t) > P(t)

Operational interpretation:

- accumulated structural integrity must exceed destabilizing dissipation;

or equivalently:

- regeneration of structural integrity must outpace structural dissipation over time.

---

## 9. Minimal Visualization

Plot:

- R(t) vs time

- φᵢ(t) phase distribution

---

## 10. Conclusion

This simulation demonstrates:

- emergence of synchronization;

- accumulation of coordinated structural integrity;

- transition toward a stable operational regime;

- dependence on forcing, coupling, and dissipation.

EDS/EDC is validated through observable synchronization behavior only if retained structural continuity persists beyond transient forcing.

The central condition remains:

C(t) > P(t)

meaning:

- structural regeneration and retained continuity exceed destabilizing structural dissipation over operational time.
