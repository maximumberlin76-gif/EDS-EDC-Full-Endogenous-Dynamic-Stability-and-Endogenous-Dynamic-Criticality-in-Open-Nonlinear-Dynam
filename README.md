# Endogenous Dynamic Stability (EDS)  
## with Endogenous Dynamic Criticality (EDC)

---

## Overview

Endogenous Dynamic Stability (EDS) defines a universal condition for the viability of nonlinear open dissipative systems.

It formalizes stability as a dynamically maintained balance between synthesis, load, and dissipation.

Endogenous Dynamic Criticality (EDC) is the dynamical regime of the same system near the stability boundary, where internally generated dynamics drive the system toward a critical transition.

This is a single theoretical framework with two levels:

- **EDS** — structural stability condition  
- **EDC** — dynamic evolution near criticality  

---

## Core Principle (EDS)

The system is defined by:

Δ(t) = S(t) − P(t) − D(t)

Where:

- S(t) — synthesis (structure formation)  
- P(t) — load (external demand, extraction)  
- D(t) — dissipation (losses, entropy production)  

---

## Stability Condition

A system remains viable only if:

∫(S − P − D) dt > 0  

over a given time horizon.

Interpretation:

- Δ > 0 → growth  
- Δ = 0 → quasi-stationary state  
- Δ < 0 → degradation  

Time dependence is implicit: t denotes continuous time,
with discrete formulation given by Δt in the one-step stability condition.

---

## Transition to Dynamic Form

Define coherence:

C(t) ~ ∫(S − D) dt  

Then:

dC/dt ≈ S − D  

Load P remains external.

This yields the minimal stability condition:

C(t) > P(t)

(Marnov Stability Criterion)

This condition is equivalent to the integral form:

C(t) > P(t)
⇔
∫(S − P − D) dt > 0

Thus, the differential and integral formulations
define the same stability boundary.

---

## Dynamic Regime (EDC)

Near the stability boundary, the system enters a critical regime.

The dynamics are governed by:

dC/dt = rC − C³  

dr/dt = μ(P − C)

Where:

- C(t) — coherence  
- P(t) — load  
- r(t) — endogenous control parameter  
- μ — coupling coefficient  

---

## Endogenous Drift

The control parameter is internally generated:

r is not imposed externally.

Near criticality:

r(t) ≈ v t  

v = μP  

The system approaches the critical point through its own dynamics.

---

## Scaling Law (Core Result)

In the critical regime, the system reduces to:

dC/dt = v t C − C³  

This represents a slow passage through a bifurcation with an endogenous control parameter.

---

### Rescaling

Introduce dimensionless variables:

C = v^(1/3) y  

t = v^(−1/3) τ  

Compute derivative:

C = v^(1/3) y  

t = v^(−1/3) τ  

Then:

dC/dt = (dC/dτ) / (dt/dτ)

dC/dτ = v^(1/3) dy/dτ  

dt/dτ = v^(−1/3)

Thus:

dC/dt = v^(1/3) dy/dτ / v^(−1/3)  
= v^(2/3) dy/dτ

Substitution:

v^(2/3) dy/dτ = v^(2/3)(τy − y³)

Divide by v^(2/3):

dy/dτ = τy − y³  

---

### Universal Form

This universality holds under the following conditions:

- cubic saturation dominates nonlinear dynamics
- control parameter evolves smoothly (r ≈ vt)
- the system is open and dissipative

Outside these conditions, alternative scaling behavior may arise.

The equation:

dy/dτ = τy − y³  

is parameter-free.

All system-specific parameters are absorbed into scaling.

This establishes:

- universality  
- scale invariance  
- independence from microscopic details within the defined universality domain
  
---

## Delay Scaling

The transition delay follows:

t_delay ~ v^(−1/3)  

t_delay ~ (μP)^(−1/3)

---

## Physical Interpretation

- slower drift (v ↓) → longer delay  
- higher load (P ↑) → faster transition  
- response is nonlinear and delayed  

The exponent:

−1/3  

is the universal signature of endogenous dynamic criticality.

---

## Meaning (M)

Meaning is defined as:

M = stable informational attractor  

A configuration that:

- is reproducible  
- maintains coherence  
- persists over time  

Meaning exists if and only if:

C > P  

Thus, meaning is a physical property of stable structure.

---

## Interpretation

EDS defines whether a system remains viable.

EDC defines how the system approaches and undergoes transition.

Together they describe:

- formation of structure  
- maintenance of stability  
- loss of coherence  
- critical transformation  

---

## Scope

Applicable to:

- physical systems  
- biological systems  
- cognition  
- socio-economic systems  
- technological systems (including AI)  

---

## Appendix (Full Mathematical Derivation)

A complete and explicit derivation of scaling and rescaling,
including all intermediate steps, is provided in: 

[README_APPENDIX.md](README_APPENDIX.md)

---

## Status

Canonical formulation.

Includes full scaling law and dynamic regime.



