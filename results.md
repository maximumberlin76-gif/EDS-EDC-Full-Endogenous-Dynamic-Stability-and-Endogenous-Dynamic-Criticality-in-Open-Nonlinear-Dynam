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

- Final coherence: R ≈ 0.85–0.92  
- Max coherence: R_max ≈ 0.90–0.95  
- Convergence time: slower or unstable  

---

### Forced

- Final coherence: R ≈ 0.95–0.99  
- Max coherence: R_max ≈ 0.98–1.00  
- Convergence time: significantly reduced  

---

## 3. Key Effects

### Acceleration

Convergence time decreases under forcing.

### Coherence Gain

Higher R values achieved in forced regime.

### Stability

System remains coherent more consistently.

---

## 4. Interpretation

R(t) serves as a measurable proxy for coherence C(t).

Observed effect:

- forcing increases R(t)  
- reduces convergence time  
- stabilizes synchronized state  

This corresponds to:

C(t) > P(t)

---

## 5. Structural Meaning

External forcing does not impose order.

It reshapes the phase space such that:

- coherent states become dominant  
- incoherent states become unstable  

---

## 6. Conclusion

The simulation confirms:

- synchronization emerges naturally under coupling  
- coherent forcing enhances stability  
- nonlinear system transitions into stable regime  

This provides a minimal computational validation of:

EDS → stability via coherence  
EDC → transition dynamics
