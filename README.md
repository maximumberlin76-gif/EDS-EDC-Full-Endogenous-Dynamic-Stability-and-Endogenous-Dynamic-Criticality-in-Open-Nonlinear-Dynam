Endogenous Dynamic Criticality (EDC)

Overview

Endogenous Dynamic Criticality (EDC) defines a class of nonlinear open dissipative systems in which the control parameter is not externally imposed, but generated internally through system dynamics.

In such systems, structure, stability, and critical behavior emerge from the balance between coherence (organization) and dissipative consumption (loss).

This framework unifies nonlinear dynamics, open-system thermodynamics, and information-based structure formation.

---

System Class

EDC applies strictly to:

- Nonlinear systems
- Open systems (exchange with environment)
- Dissipative systems (irreversible loss present)

Without these three conditions, the model is not valid.

---

Core Dynamics

The system is defined by the coupled equations:

dC/dt = rC − C^3
dr/dt = μ(P − C)

Where:

- C(t) — coherence (degree of structural organization)
- P(t) — dissipative consumption (loss/extraction)
- r(t) — control parameter (internally generated)
- μ — coupling coefficient

Interpretation:

- Growth term: rC → amplification of structure
- Saturation: −C^3 → nonlinear stabilization
- Feedback: μ(P − C) → endogenous parameter drift

---

Endogenous Drift

Unlike classical systems:

- r is not external
- r evolves dynamically

Near criticality:

r(t) ≈ v t
v = μP

This creates a self-driven approach to the critical point.

---

Universal Scaling Law

EDC systems exhibit delayed transition behavior:

t_delay ~ v^(-1/3)

This scaling emerges from:

- cubic nonlinearity
- slow internal drift

This is a universal signature of endogenous critical systems.

---

Stability Criterion (Marnov Criterion)

A necessary condition for structural persistence:

C(t) > P(t)

Where:

- C = coherence (organized structure)
- P = dissipation (loss/destruction)

Implications:

- C > P → structure is maintained
- C = P → critical boundary
- C < P → structural collapse

This is the minimum condition for dynamic stability.

---

Meaning (M)

Meaning is defined as:

M = stable informational attractor

That is:

A reproducible, coherent configuration of the system that persists over time.

Meaning exists if and only if:

C > P

Thus, meaning is not abstract — it is a physical property of stable structure.

---

Interpretation

EDC reframes structure formation as:

- balance between organization and dissipation
- emergence of stable attractors
- internally driven critical transitions

This connects:

- nonlinear dynamics
- thermodynamics of open systems
- information and structure

---

Repository Structure

/docs — core theory (single source of truth)
/old  — deprecated materials

---

Status

This repository is a clean reinitialization.

All previous fragmented versions are deprecated.

The current version is the canonical baseline.

---
