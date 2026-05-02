# Appendix: Dynamic Coherence, Synchronization and Regime Formation

---

## A1. Order Parameter and Coherence

The degree of synchronization in a nonlinear oscillator system is quantified by the Kuramoto order parameter:

R(t) = |(1/N) Σⱼ exp(iφⱼ(t))|

Where:

- R(t) ∈ [0, 1]  
- R → 1 indicates global phase synchronization  
- R → 0 indicates incoherent dynamics  

In the EDS framework:

C(t) ≈ R(t)

R(t) serves as an operational proxy for coherence C,
providing a measurable representation of system-wide phase alignment.

---

## A2. Phase Dynamics Model

The system is modeled as an ensemble of coupled nonlinear oscillators:

dφᵢ/dt = ωᵢ + (K/N) Σⱼ sin(φⱼ − φᵢ) + F_ext sin(ω_ext t − φᵢ) + η

Where:

- φᵢ — phase of the i-th oscillator  
- ωᵢ — natural frequency distribution  
- K — coupling strength  
- F_ext — external coherent forcing  
- ω_ext — forcing frequency  
- η — stochastic noise  

---

## A3. Convergence Dynamics

Define convergence time:

t_conv = min { t : R(t) ≥ R_threshold }

Where:

R_threshold ≈ 0.7 (phase-locked regime)

Observation:

- Without forcing → slower convergence  
- With forcing → accelerated synchronization  

---

## A4. Retention After Forcing

After removing external forcing:

F_ext → 0

Define retention time:

t_ret = duration where R(t) ≥ R_threshold

Interpretation:

- large t_ret → stable attractor  
- small t_ret → transient regime  

---

## A5. Effective Dissipation

Noise η introduces phase dispersion:

η ↑ → R ↓

External forcing reduces effective dispersion:

η_eff = η − f(F_ext, ω_ext)

Thus:

C(t) increases while effective dissipation decreases

EDS condition:

C(t) > P(t)

---

## A6. Resonance Synchronization Window

Define detuning:

Δω = |ω_ext − ω_mean|

Synchronization occurs within:

|Δω| ≤ Δω_lock

Where Δω_lock depends on:

- coupling strength K  
- noise level η  
- frequency spread  

Within window:

R → 1 (phase locking)

---

## A7. Regime Transition Criterion

Stable regime condition:

dR/dt > 0 and R → 1

Consistent with the EDS stability condition:

C(t) > P(t)

---

## A8. Experimental Results (Simulation)

### Plasma Parameters

- Electron density: n_e = 1×10¹⁷ m⁻³  
- Electron temperature: T_e ≈ 10⁴ K  
- Ion temperature: T_i ≈ 10³ K  
- Gas: Argon (m = 40 amu)  
- Plasma frequency: ~2.85 GHz  
- Ion-acoustic frequency: ~5.76 MHz  

---

### Results

| Scenario        | R_final | R_max | Convergence Time |
|----------------|--------|-------|------------------|
| Baseline       | 0.980  | 0.980 | 3.35             |
| Resonance      | 0.997  | 0.997 | 1.42             |
| Off-resonance  | 0.996  | 0.996 | 1.38             |
| Pulsed         | 0.986  | 0.992 | —                |

---

### Observations

1. Convergence acceleration:
   3.35 → 1.42 (~2.4× faster)

2. Coherence increase:
   0.980 → 0.997

3. High intrinsic coupling already present in baseline

4. Broad synchronization window (off-resonance remains effective)

---

## A9. Interpretation

External coherent forcing:

- accelerates phase alignment  
- reduces phase noise  
- drives system into stable attractor  

Thus:

C(t) increases  
P(t) effectively decreases  

EDS condition is satisfied:

C(t) > P(t)

---

## A10. Key Result

A nonlinear plasma system can be driven into a highly coherent state through external oscillatory forcing, with measurable:

- faster convergence  
- increased coherence  
- stable regime formation  

---

## A11. Open Validation Steps

To fully confirm the model:

- frequency sweep around ω_ext  
- noise robustness testing  
- retention time measurement after forcing removal  

---

## A12. Conclusion

The oscillator model provides a measurable realization of:

EDS → stability condition  
EDC → transition dynamics  

Abstract theory is directly mapped to:

observable synchronization behavior in physical systems
