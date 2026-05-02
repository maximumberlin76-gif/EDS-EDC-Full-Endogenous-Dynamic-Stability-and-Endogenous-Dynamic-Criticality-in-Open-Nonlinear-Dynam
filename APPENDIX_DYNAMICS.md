# Appendix — Stability and Bifurcation Analysis
(EDS / EDC Dynamical Structure)

---

## 1. Dynamical System

The EDC system is defined by:

dC/dt = rC − C³  
dr/dt = μ(P − C),   μ > 0  

where:

C(t) — coherence  
r(t) — endogenous control parameter  
P — load (constant or slowly varying)  

---

## 2. Equilibrium Point

Set:

dC/dt = 0  
dr/dt = 0  

From:

rC − C³ = 0  ⇒  C(r − C²) = 0  

Non-trivial solution:

C* = P  

Then:

r* = P²  

Thus equilibrium:

(C*, r*) = (P, P²)

---

## 3. Jacobian Matrix

General Jacobian:

J = [ ∂/∂C (rC − C³)     ∂/∂r (rC − C³) ]
    [ ∂/∂C μ(P − C)      ∂/∂r μ(P − C)  ]

Compute:

J = [ r − 3C²     ,   C ]
    [   −μ        ,   0 ]

At equilibrium (C*, r*):

J* = [ −2P²   ,   P ]
     [ −μ     ,   0 ]

---

## 4. Eigenvalues

Characteristic equation:

|J − λI| = 0  

⇒

λ² + 2P² λ + μP = 0  

---

## 5. Stability Conditions

Trace:

Tr(J) = −2P² < 0  

Determinant:

Det(J) = μP > 0  

Thus:

- eigenvalues have negative real parts  
- equilibrium is locally asymptotically stable  

---

## 6. Phase Interpretation

The system:

- converges toward (C*, r*)  
- exhibits no divergence  
- has bounded trajectories  

Depending on parameters:

- stable node or  
- stable focus  

---

## 7. Lyapunov Structure (Important)

Consider candidate functional:

V(C, r) = (1/4)C⁴ − (1/2)rC² + (μ/2)(C − P)²  

Compute derivative:

dV/dt ≠ strictly ≤ 0 globally  

Conclusion:

- system is dissipative  
- but NOT strictly gradient  

This is critical:

the dynamics is not purely energy-minimizing

---

## 8. Absence of Oscillations (Base System)

The system is 2-dimensional:

(C, r)

Thus:

- no self-sustained oscillations  
- no limit cycles  
- no Hopf bifurcation in base model  

---

## 9. Memory Extension

Introduce relaxation (lag):

dr/dt = (1/τ)(μ(P − C) − r)

where:

τ — memory timescale  

Now system becomes effectively higher-dimensional.

---

## 10. Extended System (3D Form)

Introduce auxiliary variable R:

dC/dt = rC − C³  
dr/dt = (1/τ)(μ(kR − C) − r)  
dR/dt = s − ρR − χCR  

---

## 11. Hopf Bifurcation

Oscillations appear when:

a₁ a₂ = a₃  

(standard cubic characteristic condition)

Near threshold:

- real part of eigenvalues → 0  
- imaginary part ≠ 0  

⇒ Hopf bifurcation

---

## 12. Oscillation Amplitude

Near critical parameter:

|A| ~ √(μ − μ_c)

---

## 13. Key Result

Base system:

- stable  
- no oscillations  

Extended system (with memory):

- oscillations possible  
- Hopf bifurcation emerges  

---

## 14. Structural Insight

EDC dynamics splits into two regimes:

1. No memory (τ → 0)
   → monotonic convergence  

2. With memory (τ finite)
   → oscillatory dynamics possible  

---

## 15. Conclusion

The full dynamical structure is:

EDS → defines stability condition  
EDC → defines approach to criticality  
Jacobian → defines local stability  
Lyapunov → defines dissipative structure  
Memory → enables oscillations  
Hopf → defines transition to cyclic behavior  

---

## 16. Final Statement

The system is:

- structurally stable  
- dissipative  
- non-gradient  
- non-oscillatory in base form  
- capable of oscillations only via memory coupling  

This completes the dynamical analysis.
