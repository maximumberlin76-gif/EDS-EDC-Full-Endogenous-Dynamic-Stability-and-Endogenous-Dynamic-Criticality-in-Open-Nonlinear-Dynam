# README Appendix

Full Mathematical Derivation: EDS → EDC → Scaling

## Operational Parameter Definitions

Δ(t) — instantaneous operational structural balance of the system at time t.

S(t) — instantaneous intensity of synthesis of positive structural work at time t.

W_S(T) — accumulated positive structural work over an operational time interval T.

P(t) — destabilizing structural pressure, operational load, fragmentation pressure, or operational destabilization at time t.

D(t) — irreversible structural losses and entropy-producing degradation at time t.

C(t) — parameter of general endogenous structural coherence determining the level of structural integrity and dynamic stability over time.

r(t) — endogenous operational control parameter.

μ — operational coupling coefficient.

v_eff — effective endogenous drift rate.

t — operational time variable.

τ — dimensionless rescaled operational time variable.

y — dimensionless rescaled endogenous coherence variable.

Structural regeneration is a continuous endogenous process of restoring and maintaining structural integrity and coherence over time.

Regeneration supports C(t), but is not identical to C(t).

Coherence, synchronization, resonance, regeneration, and recursive continuity are treated as operational mechanisms or processes that may support C(t), but they are not identical to C(t).

Synchronization must not be equated with coherence.

## 1. Core Chain

| Step | Operational Form | Meaning |
|---:|---|---|
| 1 | Δ(t) = S(t) − P(t) − D(t) | instantaneous structural balance |
| 2 | ∫[t₀ → t₁] Δ(t)dt > 0 | accumulated structural balance supporting formal structural existence |
| 3 | W_S(T) = ∫[t₀ → t₁] S(t)dt | accumulated positive structural work |
| 4 | C(t) > P(t) | EDS criterion of real dynamic stability over time |
| 5 | C(t) ≈ P(t) | EDC critical boundary |
| 6 | dC/dt = rC − C³ | reduced EDC dynamic regime |
| 7 | r(t) ≈ v_eff t | endogenous operational drift |
| 8 | dy/dτ = τy − y³ | canonical critical form |
| 9 | t_delay ~ v_eff^(−1/2) | critical delay scaling law |

## 2. Starting Point: EDS

The EDS instantaneous structural balance is:

Δ(t) = S(t) − P(t) − D(t)

where:

- S(t) — instantaneous intensity of synthesis of positive structural work;
- P(t) — destabilizing structural pressure;
- D(t) — irreversible structural losses.

Operational interpretation:

- Δ(t) > 0 supports formal structural existence;
- Δ(t) = 0 describes quasi-stationary operational balance;
- Δ(t) < 0 describes structural degradation and fragmentation.

The accumulated structural balance over an operational time interval is:

∫[t₀ → t₁] Δ(t)dt = ∫[t₀ → t₁] [S(t) − P(t) − D(t)]dt

Operational interpretation:

- positive accumulated structural balance supports formal structural existence over operational time;
- it does not by itself prove real dynamic stability over time.

Accumulated positive structural work is:

W_S(T) = ∫[t₀ → t₁] S(t)dt

Operational interpretation:

- W_S(T) describes the accumulated positive structural work synthesized over operational time;
- W_S(T) may support structural integrity, self-organization, and endogenous structural coherence;
- W_S(T) is not identical to C(t);
- W_S(T) does not replace the criterion C(t) > P(t).

## 3. EDS Stability Criterion

The EDS criterion of real dynamic stability over time is:

C(t) > P(t)

where:

- C(t) — parameter of general endogenous structural coherence determining the level of structural integrity and dynamic stability over time;
- P(t) — destabilizing structural pressure.

Operational interpretation:

- real dynamic stability over time exists only while general endogenous structural coherence exceeds destabilizing structural pressure;
- a system may preserve formal structural existence while already losing real dynamic stability if C(t) ≤ P(t).

Therefore:

Δ(t) > 0 ≠ C(t) > P(t)

The first condition describes formal structural existence.

The second condition describes real dynamic stability over time.

## 4. Regeneration and C(t)

Structural regeneration is a continuous endogenous process of restoring and maintaining structural integrity and coherence over time.

Regeneration supports C(t), but is not identical to C(t).

If endogenous processes are decoherent in phase, amplitude, accumulation rate, connection quality, or functional contribution, the structure loses the capacity to regenerate structural integrity faster than dissipation destroys it.

Therefore:

decoherence of endogenous processes → reduction of regenerative capacity → dissipation exceeds regeneration → decrease of C(t) → disruption of dynamic stability over time.

Operational interpretation:

- regeneration is one of the internal processes supporting endogenous structural coherence;
- C(t) expresses the general level of endogenous structural coherence;
- when dissipation exceeds the structure’s capacity for self-regeneration over time, C(t) decreases.

## 5. Transition to EDC

Near the EDS stability boundary:

C(t) ≈ P(t)

the system enters a critical operational regime.

Introduce an endogenous operational control parameter:

r(t)

The reduced EDC dynamics are represented as:

dC/dt = rC − C³

dr/dt = μ(P − C)

where:

- C(t) — general endogenous structural coherence in the reduced critical regime;
- P(t) — destabilizing structural pressure;
- r(t) — endogenous operational control parameter;
- μ — operational coupling coefficient.

This equation does not redefine C(t) as regeneration.

C(t) remains the endogenous coherence variable.

Operational interpretation:

- endogenous structural coherence evolves under the influence of the control parameter r(t);
- nonlinear saturation is represented by −C³;
- destabilizing pressure enters through the endogenous drift equation for r(t);
- the system approaches the EDC critical regime when C(t) approaches P(t).

## 6. Endogenous Drift

Near criticality, the operational control parameter evolves internally.

Locally:

r(t) ≈ v_eff t

where:

v_eff — effective endogenous drift rate.

Operational interpretation:

- the system approaches the critical operational regime through its own endogenous dynamics;
- v_eff may depend on destabilizing pressure, coherence degradation, accumulated losses, and internal regime dynamics;
- v_eff is not treated as a purely external forcing parameter.

## 7. Reduced Critical Equation

Substitute:

r(t) ≈ v_eff t

into:

dC/dt = rC − C³

This yields:

dC/dt = v_eff t C − C³

Operational interpretation:

- general endogenous structural coherence evolves under slowly varying endogenous drift and nonlinear saturation;
- the system approaches a critical transition through its own internal parameter drift;
- this reduced equation describes the critical EDC layer, not the full EDS balance.

## 8. Scaling Ansatz

Introduce the general operational scaling form:

t = τ · v_eff^(−α)

C = y · v_eff^β

where:

- α — temporal scaling exponent;
- β — endogenous coherence amplitude scaling exponent;
- τ — rescaled operational time;
- y — rescaled endogenous coherence variable.

## 9. Derivative Scaling

Since:

C = y · v_eff^β

and:

t = τ · v_eff^(−α)

we obtain:

dC/dt = v_eff^(β + α) dy/dτ

## 10. Right-Hand Side Scaling

Start from:

dC/dt = v_eff t C − C³

First term:

v_eff t C

Substitute:

v_eff · (τ · v_eff^(−α)) · (y · v_eff^β)

Therefore:

v_eff t C = v_eff^(1 − α + β) τy

Nonlinear term:

C³ = (y · v_eff^β)³

Therefore:

C³ = v_eff^(3β)y³

## 11. Scaling Exponent Matching

For canonical reduction, the derivative term, drift term, and cubic saturation term must scale equally:

β + α = 1 − α + β = 3β

From:

β + α = 1 − α + β

we obtain:

α = 1/2

From:

β + α = 3β

we obtain:

α = 2β

Therefore:

β = 1/4

The consistent operational rescaling is:

C = v_eff^(1/4)y

t = v_eff^(−1/2)τ

This rescaling absorbs v_eff from the reduced cubic critical equation.

## 12. Exact Rescaling

Choose:

C = v_eff^(1/4)y

t = v_eff^(−1/2)τ

Operational interpretation:

- the scaling absorbs system-dependent operational parameters into dimensionless variables;
- the critical regime becomes comparable across systems within the defined universality domain.

## 13. Derivative Transformation

Given:

C = v_eff^(1/4)y

t = v_eff^(−1/2)τ

Then:

dC/dt = (dC/dτ) / (dt/dτ)

Compute:

dC/dτ = v_eff^(1/4) dy/dτ

dt/dτ = v_eff^(−1/2)

Therefore:

dC/dt = v_eff^(3/4) dy/dτ

## 14. Substitution

Start from:

dC/dt = v_eff t C − C³

Left-hand side:

v_eff^(3/4) dy/dτ

Right-hand side:

v_eff · (v_eff^(−1/2)τ) · (v_eff^(1/4)y) − (v_eff^(1/4)y)³

This becomes:

v_eff^(3/4)(τy − y³)

Therefore:

v_eff^(3/4) dy/dτ = v_eff^(3/4)(τy − y³)

Divide by:

v_eff^(3/4)

Result:

dy/dτ = τy − y³

## 15. Canonical Form

The canonical operational equation is:

dy/dτ = τy − y³

This equation is parameter-free.

All system-specific operational parameters are absorbed into scaling.

Operational interpretation:

- the critical operational dynamics become universal within the defined scaling domain;
- microscopic implementation details are suppressed into the rescaled variables;
- the resulting canonical equation describes the reduced critical EDC regime.

## 16. Scaling Law

For τ = O(1), the characteristic operational delay is:

t_delay ~ v_eff^(−1/2)

The exponent −1/2 belongs to the linearly ramped EDC transition class and is not unique to cubic saturation.

## 17. Generalized Ramp-Scaling Lemma

For the nonnegative endogenous coherence variable C ≥ 0, consider:

dC/dt = v_eff t C − g C^n

with v_eff > 0, g > 0, and n > 1.

Set:

t = v_eff^(−α) τ

C = g^(−1/(n−1)) v_eff^β y

The derivative, ramp, and saturation terms scale as:

β + α

1 − α + β

nβ

Canonical balance requires:

β + α = 1 − α + β = nβ

Therefore:

α = 1/2

β = 1/(2(n−1))

The exact rescaling is:

t = v_eff^(−1/2) τ

C = g^(−1/(n−1)) v_eff^(1/(2(n−1))) y

and the generalized parameter-free equation is:

dy/dτ = τy − y^n

Thus:

t_critical ~ v_eff^(−1/2)

t_delay ~ v_eff^(−1/2)

for every n > 1 in this linearly ramped class, while:

C_critical ~ g^(−1/(n−1)) v_eff^(1/(2(n−1)))

depends on the saturation order.

| n | amplitude exponent β | time exponent α |
|---:|---:|---:|
| 2 | 1/2 | 1/2 |
| 3 | 1/4 | 1/2 |
| 4 | 1/6 | 1/2 |
| 5 | 1/8 | 1/2 |

The temporal exponent is fixed by the derivative–ramp balance. Changing the saturation mechanism or order changes the amplitude exponent, but not the delay exponent, provided the critical ramp retains the form v_eff t C.

## 18. Geometric Dimensional Closure

Let a coherent endogenous structure have d independent characteristic linear extents C_i. Its coherent dimensional measure scales as:

V_coh,d ∝ ∏_(i=1)^d C_i

Under isotropy C_i ~ C:

V_coh,d ∝ C^d

When C is operationalized as a characteristic linear coherence extent and nonlinear saturation is closed by the coherent d-dimensional measure, the geometric hypothesis is:

n = d

For d > 1:

C_critical ~ g^(−1/(d−1)) v_eff^(1/(2(d−1)))

while:

t_delay ~ v_eff^(−1/2)

remains dimension-independent within the reduced ramp equation.

For the full-volume three-dimensional EDS realization:

V_coh,3 ∝ C_x C_y C_z

and under isotropy:

C_x ~ C_y ~ C_z ~ C

V_coh,3 ∝ C³

Therefore the cubic specialization gives:

C_critical ~ g^(−1/2) v_eff^(1/4)

t_delay ~ v_eff^(−1/2)

Geometric closure and symmetry closure are distinct model arguments. Geometric closure predicts a dimension-sensitive saturation order. For a signed scalar amplitude, the independent symmetry C → −C excludes even powers and selects cubic saturation as the leading nonlinear term. In the present nonnegative, full-volume three-dimensional EDS interpretation, geometric closure supplies the primary volumetric rationale, while the delay exponent remains independent of the saturation order.

A cross-dimensional realization can test the geometric component: changing effective dimension should change the amplitude exponent according to 1/(2(n−1)), while the delay exponent remains −1/2 as long as the ramp term remains v_eff t C.

## 19. Universality Conditions

The generalized temporal exponent −1/2 holds when:

- a finite saturation term gC^n with n > 1 is present;
- endogenous drift is smooth and r(t) ≈ v_eff t near criticality;
- the reduced EDC description remains valid in the analyzed critical window;
- the characteristic delay is evaluated at τ = O(1).

The cubic specialization additionally assumes n = d = 3 through full-volume geometric closure, or another independent mechanism selecting cubic saturation. Outside this domain, alternative scaling behavior may emerge.

## 20. Positive and Negative Critical Windows

A critical or resonance window is not automatically positive.

The quality of transition depends on the direction and quality of endogenous drift.

Positive drift may support:

- reorganization;
- structural renewal;
- increased endogenous coherence;
- transition to a more stable retained regime.

Negative drift may produce:

- fragmentation;
- loss of coherence;
- accelerated dissipation;
- degradation;
- collapse into a lower-order regime.

Therefore:

critical window ≠ automatically synthesis window.

The sign of the window is determined by the quality of endogenous drift and the retained level of C(t).

## 21. Conclusion

The full operational chain becomes:

EDS instantaneous structural balance → accumulated positive structural work → EDS stability criterion → EDC critical boundary → endogenous operational drift → reduced cubic critical dynamics → canonical critical form → delay scaling law

In symbolic form:

Δ(t) = S(t) − P(t) − D(t)

W_S(T) = ∫[t₀ → t₁] S(t)dt

C(t) > P(t)

C(t) ≈ P(t)

dC/dt = rC − C³

r(t) ≈ v_eff t

dy/dτ = τy − y³

t_delay ~ v_eff^(−1/2)

The exponent:

−1/2

is not postulated.

It emerges from the reduced critical structure of the EDC transition layer under the defined universality conditions.

## Final Distinction

Δ(t) describes formal structural existence.

W_S(T) describes accumulated positive structural work.

C(t) describes general endogenous structural coherence.

Structural regeneration supports C(t), but is not identical to C(t).

C(t) > P(t) defines real dynamic stability over time.

EDC describes the critical transition dynamics near C(t) ≈ P(t).
