# Simulation Results

Kuramoto Synchronization under External Forcing

## 1. Setup

System:

- N = 300 oscillators
- K = 1.2
- η = 0.04
- ω ~ Normal(1.0, 0.15)

Comparison:

- Baseline: F_ext = 0
- Forced: F_ext = 0.6

Measured quantity:

R(t) = |(1/N) Σ exp(iφⱼ)|

where R(t) is the Kuramoto synchronization order parameter.

Important distinction:

R(t) measures phase synchronization.

R(t) is not identical to C(t).

C(t) is the parameter of general endogenous structural coherence determining the level of structural integrity and dynamic stability over time.

Synchronization may support C(t), but synchronization does not define C(t).

Real dynamic stability remains governed by:

C(t) > P(t)

## 2. Observed Metrics

### Baseline

- Final synchronization: R ≈ 0.85–0.92
- Max synchronization: R_max ≈ 0.90–0.95
- Convergence time: slower or less stable

### Forced

- Final synchronization: R ≈ 0.95–0.99
- Max synchronization: R_max ≈ 0.98–1.00
- Convergence time: significantly reduced

## 3. Key Effects

### Acceleration

Convergence time decreases under coherent forcing.

### Synchronization Gain

Higher R(t) values are achieved in the forced regime.

### Retention

The system remains synchronized more consistently during the observed interval.

### Reduced Phase Dispersion

External coherent forcing reduces effective phase dispersion and improves access to synchronized operational regimes.

## 4. Interpretation

R(t) serves as a measurable synchronization proxy and support indicator.

Observed effect:

- forcing increases R(t);
- forcing reduces convergence time;
- forcing improves synchronization accessibility;
- forcing may support retained operational coherence.

This supports the synchronization-support layer of EDS/EDC.

It does not prove that R(t) = C(t).

It does not by itself prove full real dynamic stability.

The EDS condition remains:

C(t) > P(t)

Operational interpretation:

measurable synchronization may support endogenous structural coherence, but real dynamic stability over time requires general endogenous structural coherence to exceed destabilizing structural pressure.

## 5. Structural Meaning

External forcing does not mechanically impose structural stability.

It reshapes the operational phase dynamics such that:

- synchronized states become more accessible;
- incoherent phase dispersion is reduced;
- retained synchronization attractors become more accessible;
- operational support for endogenous structural coherence may increase.

However:

- synchronization is not identical to coherence;
- R(t) is not identical to C(t);
- retained synchronization does not replace the EDS criterion.

Real dynamic stability over time still requires:

C(t) > P(t)

## 6. EDS Interpretation

Within EDS:

Δ(t) = S(t) − P(t) − D(t)

describes formal structural existence through instantaneous structural balance.

S(t) is the instantaneous intensity of synthesis of positive structural work.

Accumulated positive structural work is:

W_S(T) = ∫[t₀ → t₁] S(t) dt

C(t) describes general endogenous structural coherence.

Synchronization may support C(t), but does not replace C(t).

Therefore:

positive synchronization results support the operational possibility of retained coherence, but the stability criterion remains:

C(t) > P(t)

## 7. EDC Interpretation

Within EDC:

the system approaches a critical regime when:

C(t) ≈ P(t)

Near this boundary, small changes in synchronization, forcing, dispersion, or coupling may produce disproportionate regime effects.

Coherent forcing may shift the system toward a more synchronized regime.

But the quality of this transition depends on the direction and quality of endogenous drift.

A synchronization window is not automatically a positive structural transition.

It becomes positive only if it supports endogenous structural coherence and retained dynamic stability over time.

## 8. Conclusion

The simulation confirms:

- synchronization emerges naturally under coupling;
- coherent forcing enhances synchronization accessibility;
- convergence toward synchronized phase dynamics becomes faster;
- the nonlinear system shifts toward a more retained synchronized operational regime.

This provides a minimal computational validation of the synchronization-support layer of EDS/EDC:

EDS → real dynamic stability condition:

C(t) > P(t)

EDC → transition dynamics near:

C(t) ≈ P(t)

Synchronization layer → measurable proxy:

R(t)

Final distinction:

R(t) measures synchronization.

C(t) measures general endogenous structural coherence.

Synchronization may support C(t), but is not identical to C(t).

Real dynamic stability over time remains governed by:

C(t) > P(t)
