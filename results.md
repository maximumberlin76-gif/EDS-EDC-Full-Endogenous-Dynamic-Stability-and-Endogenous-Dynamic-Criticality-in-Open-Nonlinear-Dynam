# Simulation Results

Kuramoto Synchronization under External Forcing

---

## 1. Setup

System:

- N = 300 oscillators
- K = 1.2
- η = 0.04
- ω ~ Normal(1.0, 0.15)

Comparison:

- Baseline: F_ext = 0
- Forced: F_ext = 0.6

---

## 2. Observed Metrics

### Baseline

- Final synchronization: R ≈ 0.85–0.92
- Max synchronization: R_max ≈ 0.90–0.95
- Convergence time: slower or unstable

### Forced

- Final synchronization: R ≈ 0.95–0.99
- Max synchronization: R_max ≈ 0.98–1.00
- Convergence time: significantly reduced

---

## 3. Key Effects

### Acceleration

Convergence time decreases under forcing.

### Synchronization Gain

Higher R(t) values are achieved in the forced regime.

### Stability

The system remains synchronized more consistently.

---

## 4. Interpretation

R(t) serves as a measurable synchronization proxy supporting C(t).

Observed effect:

- forcing increases R(t);
- reduces convergence time;
- stabilizes synchronized operational state.

This supports the EDS condition:

C(t) > P(t)

---

## 5. Structural Meaning

External forcing does not impose order mechanically.

It reshapes the operational phase space such that:

- synchronized states become more accessible;
- incoherent states become less stable;
- retained structural continuity receives stronger operational support.

---

## 6. Conclusion

The simulation confirms:

- synchronization emerges naturally under coupling;
- coherent forcing enhances synchronization accessibility;
- the nonlinear system transitions toward a more stable operational regime.

This provides a minimal computational validation of:

EDS → stability via retained structural continuity

EDC → transition dynamics
