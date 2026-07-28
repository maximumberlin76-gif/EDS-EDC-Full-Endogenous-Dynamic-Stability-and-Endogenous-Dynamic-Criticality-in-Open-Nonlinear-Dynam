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

The characteristic delay follows from:

t = v_eff^(−1/2) τ

For:

τ = O(1)

the delay scales as:

t_delay ~ v_eff^(−1/2)

If the simplified approximation:

v_eff ≈ μP

is used, then:

t_delay ~ (μP)^(−1/2)

Operational interpretation:

- slower endogenous drift produces longer delayed transitions;

- faster endogenous drift produces shorter delayed transitions;

- stronger destabilizing pressure may increase effective drift and accelerate critical transition accessibility.

## 4J — Interpretation

The exponent:

−1/2

defines the scaling regime of the reduced cubic critical equation under the following operational conditions:

- cubic saturation dominates nonlinear critical dynamics;

- endogenous drift evolves smoothly;

- r(t) ≈ v_eff t near the critical regime;

- the system remains open, dissipative, nonlinear, and dynamically coupled;

- the reduced EDC dynamics remain valid within the analyzed critical window.

Outside this operational domain, alternative scaling behavior may emerge.
