  # Appendix — Stability and Bifurcation Analysis

(EDS / EDC Dynamical Structure)

---

## Operational Parameter Definitions

C(t) — structural regeneration, retained structural continuity, and restorative structural capacity at time t.

P(t) — structural dissipation pressure, destabilizing operational load, and fragmentation pressure at time t.

r(t) — endogenous operational control parameter.

μ — operational coupling coefficient, μ > 0.

t — operational time variable.

τ — memory timescale / relaxation timescale.

R(t) — auxiliary retained operational response variable in the extended memory-coupled system.

s — external or endogenous source term for the auxiliary response variable.

ρ — decay coefficient of the auxiliary response variable.

χ — coupling coefficient between C(t) and R(t).

λ — eigenvalue of the Jacobian matrix.

J — Jacobian matrix of the local dynamical system.

V(C,r) — Lyapunov candidate functional.

Δφ — operational phase mismatch / synchronization deviation.

Coherence, synchronization, and resonance are treated as operational mechanisms supporting C(t), not as identical to structural integrity itself.

---

## 1. Dynamical System

The base EDC system is defined by:

dC/dt = rC − C³

dr/dt = μ(P − C), μ > 0

where:

- C(t) — structural regeneration, retained structural continuity, and restorative structural capacity;

- r(t) — endogenous operational control parameter;

- P(t) — structural dissipation pressure, treated here as constant or slowly varying;

- μ — operational coupling coefficient.

---

## 2. Equilibrium Point

Set:

dC/dt = 0

dr/dt = 0

From:

rC − C³ = 0

therefore:

C(r − C²) = 0

Non-trivial solution:

C* = P

Then:

r* = P²

Thus the non-trivial equilibrium is:

(C*, r*) = (P, P²)

Operational interpretation:

- the equilibrium corresponds to a retained operational regime where structural regeneration balances structural dissipation pressure.

---

## 3. Jacobian Matrix

General Jacobian:

J =
[ ∂/∂C (rC − C³)      ∂/∂r (rC − C³) ]

[ ∂/∂C μ(P − C)       ∂/∂r μ(P − C)  ]

Compute:

J =
[ r − 3C²      C ]

[ −μ           0 ]

At equilibrium:

(C*, r*) = (P, P²)

the Jacobian becomes:

J* =
[ −2P²      P ]

[ −μ        0 ]

---

## 4. Eigenvalues

The characteristic equation is:

|J − λI| = 0

Therefore:

λ² + 2P²λ + μP = 0

where:

- λ — eigenvalue of the Jacobian matrix.

---

## 5. Stability Conditions

Trace:

Tr(J*) = −2P² < 0

Determinant:

Det(J*) = μP > 0

Therefore:

- eigenvalues have negative real parts under the analyzed positive-parameter regime;

- the non-trivial equilibrium is locally asymptotically stable.

Operational interpretation:

- small perturbations near the retained operational regime decay locally;

- structural regeneration remains locally bounded relative to structural dissipation pressure;

- local operational continuity remains accessible.

---

## 6. Phase Interpretation

The base system:

- converges toward (C*, r*);

- does not exhibit local divergence in the analyzed positive-parameter regime;

- has locally bounded trajectories near equilibrium.

Depending on parameter values, the equilibrium may behave as:

- a stable node;

or:

- a stable focus.

Operational interpretation:

- the base EDC system describes local approach toward retained operational balance;

- it does not by itself represent unrestricted oscillatory dynamics.

---

## 7. Lyapunov Structure

Consider candidate functional:

V(C,r) = (1/4)C⁴ − (1/2)rC² + (μ/2)(C − P)²

Compute derivative:

dV/dt is not strictly ≤ 0 globally.

Conclusion:

- the system is dissipative;

- the system is not strictly gradient;

- the candidate functional does not establish global monotonic energy minimization.

This is important:

the dynamics is not purely energy-minimizing.

Operational interpretation:

- local stability can exist without the system being globally gradient-driven;

- retained operational continuity is dynamically maintained rather than simply minimized through a single scalar potential.

---

## 8. Absence of Self-Sustained Oscillations in the Base Formulation

The base formulation is two-dimensional:

(C,r)

Within the present base model and analyzed parameter domain:

- self-sustained oscillatory regimes do not emerge as the primary operational behavior;

- no Hopf bifurcation is produced by the base formulation;

- the system locally approaches the retained operational regime.

Important clarification:

Two-dimensional systems can, in general, support limit cycles under appropriate nonlinear conditions.

The statement here applies to the analyzed base EDC formulation, not to all two-dimensional dynamical systems.

---

## 9. Memory Extension

Introduce relaxation / memory:

dr/dt = (1/τ)(μ(P − C) − r)

where:

- τ — memory timescale / relaxation timescale.

Operational interpretation:

- finite memory delays the response of the endogenous control parameter;

- delayed adjustment may allow oscillatory operational regimes to become accessible;

- retained structural dynamics become history-dependent.

---

## 10. Extended System

Introduce auxiliary variable R(t):

dC/dt = rC − C³

dr/dt = (1/τ)(μ(kR − C) − r)

dR/dt = s − ρR − χCR

where:

- R(t) — auxiliary retained operational response variable;

- τ — memory / relaxation timescale;

- k — coupling coefficient between R(t) and the dissipation-regeneration balance;

- s — source term;

- ρ — decay coefficient;

- χ — interaction coefficient between C(t) and R(t).

Operational interpretation:

- the extended system introduces memory-coupled structural response;

- oscillatory regimes become possible through delayed feedback and auxiliary retained dynamics;

- the system becomes capable of richer bifurcation behavior than the base formulation.

---

## 11. Hopf Bifurcation

For the extended system, oscillatory operational regimes may become accessible when the characteristic polynomial satisfies the standard Hopf condition.

For a cubic characteristic equation, the Hopf threshold is commonly expressed as:

a₁a₂ = a₃

with the additional requirement that:

- the real part of a conjugate eigenvalue pair approaches zero;

- the imaginary part remains non-zero.

Operationally:

Re(λ) → 0

Im(λ) ≠ 0

Therefore:

Hopf bifurcation becomes accessible.

Operational interpretation:

- Hopf bifurcation defines accessibility of oscillatory operational regimes;

- cyclic retained dynamics may emerge through memory-coupled feedback;

- structural regeneration may enter a periodic or quasi-periodic operational regime.

---

## 12. Oscillation Amplitude

Near the critical Hopf parameter:

|A| ~ √(μ − μ_c)

where:

- A — oscillation amplitude;

- μ_c — critical coupling value.

Operational interpretation:

- oscillatory amplitude grows gradually near the Hopf threshold;

- cyclic operational behavior emerges continuously under the appropriate bifurcation conditions.

---

## 13. Key Result

Base system:

- locally stable under the analyzed positive-parameter regime;

- non-gradient;

- dissipative;

- does not produce Hopf bifurcation in the base formulation.

Extended system with memory:

- may support oscillatory operational regimes;

- may produce Hopf bifurcation;

- may generate cyclic retained dynamics through delayed feedback.

---

## 14. Structural Insight

EDC dynamics separates into two operational regimes:

1. Base formulation without finite memory coupling

   τ → 0

   Operational behavior:

   - predominantly monotonic or locally damped convergence;

   - local approach toward retained operational balance;

   - no Hopf bifurcation in the base formulation.

2. Memory-coupled formulation

   τ finite

   Operational behavior:

   - delayed feedback becomes active;

   - oscillatory regimes become accessible;

   - Hopf bifurcation may emerge;

   - cyclic retained operational dynamics may form.

---

## 15. Conclusion

The full dynamical structure is:

EDS → defines the operational stability condition.

EDC → defines the approach toward criticality.

Jacobian → defines local sensitivity and local stability accessibility.

Eigenvalues → define local stability and bifurcation accessibility.

Lyapunov analysis → evaluates boundedness and stability accessibility.

Memory coupling → enables delayed feedback and richer operational dynamics.

Hopf bifurcation → defines accessibility of oscillatory operational regimes.

---

## 16. Final Statement

The base system is:

- structurally stable in the analyzed local regime;

- dissipative;

- non-gradient;

- locally non-oscillatory in its base formulation;

- capable of oscillatory operational regimes only through memory coupling or extended feedback structure.

This completes the dynamical analysis of the EDS / EDC base and extended systems.

