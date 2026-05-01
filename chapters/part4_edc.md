PART IV — Endogenous Dynamic Criticality (EDC)

---

4A — Concept

Endogenous Dynamic Criticality describes systems in which
the control parameter is generated internally.

Unlike externally tuned systems,
critical behavior emerges through internal dynamics.

---

4A.1 — Dissipative Nonlinear Nature

The system belongs to the class of open nonlinear dissipative systems.

It is characterized by:

- nonlinear self-interaction (−C³ term)
- continuous energy exchange with the environment
- presence of dissipation and irreversible processes

The dynamics does not conserve energy:

dE/dt ≠ 0

Instead, stability is maintained through balance between:

- energy/structure input
- dissipative losses
- internal feedback

This places the system within the general framework of
nonequilibrium dissipative structures.

---

4B — Minimal Dynamical Model

Let:

dC/dt = rC − C³
dr/dt = μ(P − C),  μ > 0

where:

C(t) — coherence
r(t) — internal control parameter
P(t) — dissipative load

---

4C — Equilibrium

At equilibrium:

C* = P
r* = P²

---

4D — Stability Analysis

Jacobian:

J = [ r − 3C²   ,   C ]
[ −μ        ,   0 ]

At equilibrium:

J* = [ −2P²   ,   P ]
[ −μ     ,   0 ]

Characteristic equation:

λ² + 2P² λ + μP = 0

---

4E — Stability Condition

For:

P > 0, μ > 0

we obtain:

Trace < 0
Determinant > 0

⇒ the equilibrium is locally asymptotically stable

---

4F — Absence of Oscillations

In the 2D system:

no self-sustained oscillations arise

This is consistent with gradient-like dynamics.

---

4G — Drift Toward Criticality

Near r ≈ 0:

dC/dt ≈ v_eff t C − C³

where:

v_eff = μP

---

4H — Scaling Behavior

After rescaling:

t = v_eff^(−1/3) τ
C = v_eff^(1/3) X

we obtain:

dX/dτ = τX − X³

---

4I — Delay Scaling

The characteristic delay scales as:

t_delay ~ (μP)^(−1/3)

---

4J — Interpretation

The −1/3 exponent defines a robust scaling regime
under the following conditions:

- cubic nonlinearity dominates
- control parameter evolves smoothly
- higher-order terms remain subdominant

---

4K — Limitations

This result:

- does not define a universal law
- depends on model structure
- may change under different nonlinearities

---

Conclusion

EDC provides a minimal mechanism for internally driven approach to criticality.

It complements the EDS framework by describing how systems
approach stability boundaries through internal dynamics.
