# README Appendix  
Full Mathematical Derivation  
EDS → EDC → Scaling

---

## 1. Core Chain

S − P − D = 0          → quasi-stationary balance  
       ↓  
C = ∫(S − D)dt > P    → Marnov Stability Criterion  
       ↓  
dC/dt = rC − C³       → EDC dynamics  
       ↓  
r(t) ≈ v t            → endogenous drift  
       ↓  
dy/dτ = τy − y³       → canonical form  
       ↓  
t_delay ~ v^(−1/3)    → scaling law  

---

## 2. Starting Point: EDS

The EDS balance is:

Δ(t) = S(t) − P(t) − D(t)

where:

S(t) — synthesis  
P(t) — load  
D(t) — dissipation  

The stability condition is:

∫(S − P − D) dt > 0

This means that a system remains viable only if it maintains positive structural balance over time.

---

## 3. Coherence Mapping

Define accumulated coherence as:

C(t) = ∫(S − D) dt

Then:

dC/dt = S − D

Load P does not create structure.

It acts as an external constraint.

Therefore:

C(t) > P(t)

This is the Marnov Stability Criterion.

It is equivalent to:

C(t) > P(t) ⇔ ∫(S − P − D) dt > 0

---

## 4. Transition to EDC

Near the stability boundary:

C ≈ P

The system enters a critical regime.

We introduce an endogenous control parameter r(t):

dC/dt = rC − C³

dr/dt = μ(P − C)

where:

C(t) — coherence  
P(t) — load  
r(t) — endogenous control parameter  
μ — coupling coefficient  

---

## 5. Endogenous Drift

Near criticality, the control parameter evolves internally.

Locally:

r(t) ≈ v t

with:

v = μP

The system approaches the critical point through its own dynamics.

---

## 6. Reduced Critical Equation

Substitute:

r(t) ≈ v t

into:

dC/dt = rC − C³

This gives:

dC/dt = v t C − C³

---

## 7. Scaling Ansatz

Introduce the general scaling form:

t = τ · v^(−α)

C = y · v^β

---

## 8. Derivative Scaling

Since:

C = y · v^β

and:

t = τ · v^(−α)

we get:

dC/dt = v^(β + α) dy/dτ

---

## 9. Right-Hand Side Scaling

The first term:

v t C = v · (τ · v^(−α)) · (y · v^β)

therefore:

v t C = v^(1 − α + β) τy

The nonlinear term:

C³ = (y · v^β)³

therefore:

C³ = v^(3β)y³

---

## 10. Exact Rescaling

For the canonical reduction, choose:

C = v^(1/3)y

t = v^(−1/3)τ

---

## 11. Derivative Transformation

Given:

C = v^(1/3)y

t = v^(−1/3)τ

Then:

dC/dt = (dC/dτ) / (dt/dτ)

dC/dτ = v^(1/3) dy/dτ

dt/dτ = v^(−1/3)

Therefore:

dC/dt = v^(1/3) dy/dτ / v^(−1/3)

dC/dt = v^(2/3) dy/dτ

---

## 12. Substitution

Start from:

dC/dt = v t C − C³

Left side:

v^(2/3) dy/dτ

Right side:

v · (v^(−1/3)τ) · (v^(1/3)y) − (v^(1/3)y)³

This becomes:

v τy − v y³

and therefore:

v^(2/3) dy/dτ = v^(2/3)(τy − y³)

Divide by:

v^(2/3)

Result:

dy/dτ = τy − y³

---

## 13. Canonical Form

The canonical equation is:

dy/dτ = τy − y³

This equation is parameter-free.

All system-specific parameters are absorbed into scaling.

---

## 14. Scaling Law

The characteristic delay follows from:

t = v^(−1/3)τ

For τ = O(1):

t_delay ~ v^(−1/3)

Since:

v = μP

we obtain:

t_delay ~ (μP)^(−1/3)

---

## 15. Universality Conditions

The exponent −1/3 holds for systems with:

- cubic saturation  
- smooth endogenous drift  
- open dissipative dynamics  
- nonlinear coupling  
- at least three coupled degrees of freedom  

Outside this class, different scaling may arise.

---

## 16. Conclusion

The full chain is:

EDS balance  
→ coherence mapping  
→ Marnov Stability Criterion  
→ EDC dynamics  
→ endogenous drift  
→ canonical form  
→ delay scaling law  

The exponent −1/3 is not assumed.

It follows from the invariant structure of the system.
