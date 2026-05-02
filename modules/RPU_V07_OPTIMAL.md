# RPU v0.7 OPTIMAL  
Resonant Processing Unit for EDS/EDC

---

## Purpose

RPU v0.7 OPTIMAL is an experimental computational module connected to the EDS/EDC framework.

It is not the theorem itself.

It is an applied interface that demonstrates how EDS/EDC logic can be used for:

- coherence evaluation  
- structural filtering  
- non-parasitic allocation  
- future-debt control  
- stress and dissipation monitoring  

---

## Relation to EDS

EDS defines the structural stability condition:

C(t) > P(t)

or equivalently:

∫(S − P − D) dt > 0

RPU translates this into an allocation logic:

- projects that increase coherence receive support  
- projects that increase future debt or parasitic load are blocked  
- life-support and civilization-continuity floors are preserved  

---

## Relation to EDC

EDC describes critical dynamics near the stability boundary.

RPU does not replace EDC mathematics.

It uses EDS/EDC-inspired indicators to estimate whether a project or process moves the system toward:

- stable coherence  
- structural degradation  
- critical instability  

---

## Core Components

### EthicsGate

Evaluates:

- spectral entropy  
- resonance order  
- phase mismatch  
- future debt  
- time-domain coherence  

Purpose:

prevent allocation into structurally unstable or future-negative directions.

---

### AntiStressGate

Evaluates conflict pressure through:

- resource competition  
- inequality delta  
- externality damage  
- polarization score  

Purpose:

prevent excessive social or systemic stress.

---

### NonParasitismGate

Evaluates whether a project extracts more than it contributes.

Purpose:

block parasitic structures.

---

### TeleologicalAllocator

Allocates available energy/resources after preserving:

- E_BASE — life-support floor  
- E_CIV — civilization-continuity floor  

Only projects passing all gates can receive allocation.

---

### RPUCore

Optional resonant oscillator layer.

It provides:

- phase dynamics  
- ternary state control  
- resonant imprinting  
- oscillator-based internal structure  

---

## Output

The module produces:

- allocation report  
- blocked projects  
- diagnostic metrics  
- gate decisions  
- coherence-related indicators  

---

## Expected Behavior

Stable / constructive projects should receive allocation.

High-parasitism, high-conflict, low-coherence projects should be blocked.

Expected demo result:

- education / infrastructure projects receive energy  
- attention-drain / chaos projects are blocked or suppressed  

---

## How to Run

From repository root:

```bash
python modules/rpu_v07_optimal.py
```

Extended diagnostics:

```bash
python modules/rpu_v07_optimal.py --energy 150 --show-all
```

---

## Dependencies

```bash
pip install numpy
```

---

## Status

Experimental module.

It demonstrates how EDS/EDC principles can be translated into computational allocation logic.

It is not a final production system.

---

## License

Apache-2.0
