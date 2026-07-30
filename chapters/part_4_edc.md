# PART IV — Endogenous Dynamic Criticality (EDC)

## 4A — Concept

Endogenous Dynamic Criticality (EDC) describes systems in which the critical control parameter is generated internally by the system’s own dynamics.

Unlike externally tuned systems, critical behavior emerges through endogenous drift, internal feedback, coherence degradation, destabilizing pressure, and nonlinear saturation.

EDC complements EDS.

EDS defines real dynamic stability over time:

C(t) > P(t)

EDC describes how the system approaches, enters, delays, and undergoes transition near the critical boundary:

C(t) ≈ P(t)

where:

C(t) — parameter of general endogenous structural coherence determining structural integrity and dynamic stability over time.

P(t) — destabilizing pressure, operational load, fragmentation pressure, or degradation pressure.

Important distinction:

C(t) is not regeneration.

C(t) is not synchronization.

C(t) is general endogenous structural coherence.

Regeneration may support C(t), but is not identical to C(t).

Synchronization may support C(t), but is not identical to C(t).

## 4A.1 — Dissipative Nonlinear Nature

The system belongs to the class of open nonlinear dissipative systems.

It is characterized by:

- nonlinear self-interaction;

- cubic saturation term −C³;

- continuous exchange of energy, matter, information, or constraints with the environment;

- destabilizing pressure;

- irreversible losses;

- internal feedback;

- endogenous parameter drift;

- critical transition accessibility.

The dynamics does not generally conserve internal operational energy:

dE/dt ≠ 0

Instead, retained stability is maintained through the interaction between:

- synthesis of positive structural work;

- destabilizing pressure;

- irreversible losses;

- endogenous structural coherence;

- regenerative support processes;

- internal feedback.

This places the system within the general framework of nonequilibrium open dissipative structures.

## 4B — Minimal Dynamical Model

The reduced EDC model describes the critical dynamics of endogenous structural coherence near the stability boundary.

The base system is:

dC/dt = rC − C³

dr/dt = μ(P − C),  μ > 0

where:

C(t) — general endogenous structural coherence in the reduced critical regime;

r(t) — endogenous operational control parameter;

P(t) — destabilizing pressure, treated here as constant or slowly varying;

μ — operational coupling coefficient.

The cubic term:

−C³

ensures nonlinear saturation and prevents unbounded growth.

This equation does not redefine C(t) as regeneration.

C(t) remains the endogenous structural coherence variable.

## 4C — Equilibrium

At equilibrium:

dC/dt = 0

dr/dt = 0

From:

rC − C³ = 0

we obtain:

C(r − C²) = 0

For the non-trivial branch:

C ≠ 0

therefore:

r = C²

From:

μ(P − C) = 0

we obtain:

C* = P

Therefore:

r* = P²

The non-trivial equilibrium is:

(C*, r*) = (P, P²)

Operational interpretation:

the equilibrium corresponds to a retained local regime where endogenous structural coherence is balanced against destabilizing pressure.

## 4D — Stability Analysis

The Jacobian matrix is:

J =
[ r − 3C²    C ]

[ −μ         0 ]

At equilibrium:

(C*, r*) = (P, P²)

the Jacobian becomes:

J* =
[ −2P²    P ]

[ −μ      0 ]

The characteristic equation is:

λ² + 2P²λ + μP = 0

The eigenvalues are:

λ = −P² ± √(P⁴ − μP)

## 4E — Stability Condition

For:

P > 0

and:

μ > 0

we obtain:

Trace(J*) = −2P² < 0

Determinant(J*) = μP > 0

Therefore:

the non-trivial equilibrium is locally asymptotically stable in the analyzed positive-parameter regime.

Operational interpretation:

- small perturbations near the retained local regime decay locally;

- endogenous structural coherence remains locally bounded relative to destabilizing pressure;

- local dynamic retention remains accessible.

Important distinction:

local asymptotic stability of the reduced EDC model does not replace the EDS criterion:

C(t) > P(t)

## 4F — Absence of Self-Sustained Oscillations in the Base Formulation

In the analyzed two-dimensional base system:

(C, r)

self-sustained oscillations do not arise as the primary operational behavior in the positive-parameter local regime.

The base system locally approaches the retained equilibrium.

No Hopf bifurcation is produced by the base formulation.

This statement applies to the analyzed base EDC formulation.

It does not claim that all two-dimensional nonlinear systems cannot exhibit limit cycles.

The base formulation is dissipative and non-gradient.

It is not a purely conservative oscillator.

## 4G — Drift Toward Criticality

Near the critical regime, the endogenous control parameter may be locally approximated as:

r(t) ≈ v_eff t

where:

v_eff — effective endogenous drift rate.

The reduced critical equation becomes:

dC/dt ≈ v_eff t C − C³

Operational interpretation:

- the system approaches criticality through internally generated parameter drift;

- v_eff may depend on destabilizing pressure, coherence degradation, irreversible losses, and internal regime dynamics;

- the transition is endogenous, not merely externally imposed.

## 4H — Scaling Behavior

Start from:

dC/dt = v_eff t C − C³

Introduce the rescaling:

t = v_eff^(−1/2) τ

C = v_eff^(1/4) X

Then:

dC/dt = v_eff^(3/4) dX/dτ

Substitution gives:

v_eff^(3/4) dX/dτ = v_eff^(3/4)(τX − X³)

Dividing by:

v_eff^(3/4)

we obtain the canonical critical form:

dX/dτ = τX − X³

Operational interpretation:

- the system-specific drift rate is absorbed into the rescaled variables;

- the reduced critical dynamics become parameter-free within the defined universality domain;

- this describes the EDC transition layer near the critical boundary.

## 4I — Delay Scaling

For τ = O(1):

t_delay ~ v_eff^(−1/2)

If v_eff ≈ μP is used, then:

t_delay ~ (μP)^(−1/2)

Slower endogenous drift produces longer delayed transitions; faster drift produces shorter delays.

## 4J — Generalized Ramp-Scaling Lemma

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

## 4K — Geometric Dimensional Closure

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

## 4L — Interpretation and Universality

The generalized exponent −1/2 applies when a finite saturation gC^n with n > 1 is present, endogenous drift is smooth, r(t) ≈ v_eff t near criticality, and the reduced EDC model remains valid at τ = O(1). The cubic specialization additionally assumes n = d = 3 through full-volume geometric closure, or another independent mechanism selecting cubic saturation.

Outside this operational domain, alternative scaling behavior may emerge.
