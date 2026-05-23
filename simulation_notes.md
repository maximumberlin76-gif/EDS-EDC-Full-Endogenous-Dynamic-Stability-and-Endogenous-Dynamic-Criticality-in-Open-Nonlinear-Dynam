# Simulation Notes

Minimal Reproducible Oscillator Model

## 1. Purpose

This document defines a minimal simulation setup to reproduce synchronization dynamics relevant to the EDS/EDC framework.

The model tests whether measurable synchronization can emerge, be retained, and operationally support endogenous structural coherence in a nonlinear dissipative system.

This simulation does not treat synchronization as identical to coherence.

R(t) measures synchronization.

C(t) measures general endogenous structural coherence.

Real dynamic stability remains governed by:

C(t) > P(t)

## 2. Model

Use a Kuramoto-type system:

dφᵢ/dt = ωᵢ + (K/N) Σⱼ sin(φⱼ − φᵢ) + F_ext sin(ω_ext t − φᵢ) + η

where:

- φᵢ(t) — phase of the i-th oscillator;
- ωᵢ — natural frequency of the i-th oscillator;
- K — coupling strength;
- F_ext — external coherent forcing amplitude;
- ω_ext — external forcing frequency;
- η — stochastic operational noise / phase dispersion.

## 3. Initialization

- N = 100–1000 oscillators;
- ωᵢ sampled from a normal distribution;
- φᵢ(0) uniformly random in [0, 2π].

## 4. Parameters

- K: 0.1 → 5.0;
- F_ext: 0 → small forcing range, for example 0.1–1.0;
- ω_ext ≈ mean(ωᵢ);
- η: small noise, for example 0.01–0.1.

## 5. Measurement

Compute:

R(t) = |(1/N) Σ exp(iφᵢ)|

Track:

- R(t);
- convergence time t_conv;
- retention time t_ret;
- phase dispersion;
- response after forcing removal.

Operational meaning:

- R(t) measures synchronization of subsystem phases;
- R(t) is a measurable synchronization proxy;
- R(t) may indicate operational support for C(t);
- R(t) is not identical to C(t);
- synchronization is not identical to coherence.

C(t) remains the parameter of general endogenous structural coherence determining the level of structural integrity and dynamic stability over time.

## 6. Procedure

1. Run baseline:

F_ext = 0

2. Run with forcing:

F_ext > 0

3. Compare:

- R(t);
- t_conv;
- R_max;
- phase dispersion.

4. Turn off forcing and measure:

t_ret

where:

t_ret — duration during which R(t) remains above the selected synchronization threshold after forcing removal.

## 7. Expected Behavior

Expected synchronization-layer behavior:

- with forcing → faster synchronization;
- higher R_max;
- lower effective phase dispersion;
- longer retention after forcing removal;
- broader synchronization accessibility under suitable coupling and noise conditions.

Operational interpretation:

- synchronization may become accessible faster than destabilizing phase dispersion disrupts it;
- retained synchronization may persist after forcing removal;
- retained synchronization may support endogenous structural coherence;
- retained synchronization does not itself prove real dynamic stability.

The EDS criterion remains:

C(t) > P(t)

## 8. Interpretation

R(t) serves as a measurable synchronization proxy and support indicator.

Within this framework:

C(t)

represents:

- general endogenous structural coherence;
- coherence of internal processes of structural self-organization;
- the parameter determining structural integrity and dynamic stability over time.

Structural regeneration is a continuous endogenous process of restoring and maintaining structural integrity and coherence over time.

Regeneration supports C(t), but is not identical to C(t).

Synchronization may support C(t), but is not identical to C(t).

The observed synchronization behavior maps to the support layer of:

C(t) > P(t)

Operational interpretation:

- synchronization may support endogenous structural coherence;
- retained synchronization may reduce effective phase dispersion;
- real dynamic stability requires general endogenous structural coherence to exceed destabilizing pressure;
- R(t) alone does not prove C(t) > P(t).

## 9. Minimal Visualization

Plot:

- R(t) vs time;
- φᵢ(t) phase distribution;
- baseline R(t) vs forced R(t);
- t_conv vs forcing frequency;
- t_ret after forcing removal.

## 10. EDS/EDC Interpretation

EDS:

C(t) > P(t)

defines real dynamic stability over time.

EDC:

C(t) ≈ P(t)

defines the critical boundary where the system becomes sensitive to parameter drift, forcing, noise, and regime transition.

In this simulation:

R(t)

is used only as a measurable synchronization indicator.

It can support the interpretation of synchronization accessibility, but it does not replace C(t).

## 11. Conclusion

This simulation demonstrates:

- emergence of synchronization;
- increased synchronization accessibility under coherent forcing;
- reduced convergence time;
- possible retention of synchronized dynamics after forcing removal;
- dependence on forcing, coupling, and noise.

EDS/EDC is supported through observable synchronization behavior only at the synchronization-support layer.

The central condition remains:

C(t) > P(t)

meaning:

general endogenous structural coherence exceeds destabilizing structural pressure over operational time.

Final distinction:

R(t) measures synchronization.

C(t) measures general endogenous structural coherence.

Regeneration supports C(t), but is not identical to C(t).

Synchronization may support C(t), but is not identical to C(t).

Real dynamic stability over time remains governed by:

C(t) > P(t)
