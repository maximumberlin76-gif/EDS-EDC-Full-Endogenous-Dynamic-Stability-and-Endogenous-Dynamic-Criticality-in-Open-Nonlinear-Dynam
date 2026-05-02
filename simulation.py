import numpy as np

# ------------------------------------------------------------
# Minimal Kuramoto Simulation for EDS/EDC
# ------------------------------------------------------------
# Goal:
# Compare baseline synchronization with externally forced synchronization.
# R(t) is used as an operational proxy for coherence C(t).
# ------------------------------------------------------------

N = 300
T = 20.0
dt = 0.01
steps = int(T / dt)

K = 1.2
eta = 0.04

F_ext_baseline = 0.0
F_ext_forced = 0.6
omega_ext = 1.0

np.random.seed(42)

omega = np.random.normal(loc=1.0, scale=0.15, size=N)


def order_parameter(phi):
    return np.abs(np.mean(np.exp(1j * phi)))


def run_simulation(F_ext):
    phi = np.random.uniform(0, 2 * np.pi, N)
    R_values = []

    for step in range(steps):
        t = step * dt

        phase_diff = phi[None, :] - phi[:, None]
        coupling = np.sum(np.sin(phase_diff), axis=1) / N

        forcing = F_ext * np.sin(omega_ext * t - phi)
        noise = eta * np.random.randn(N)

        dphi = omega + K * coupling + forcing + noise
        phi = phi + dphi * dt

        R_values.append(order_parameter(phi))

    return np.array(R_values)


baseline = run_simulation(F_ext_baseline)
forced = run_simulation(F_ext_forced)


def convergence_time(R, threshold=0.7):
    idx = np.where(R >= threshold)[0]
    if len(idx) == 0:
        return None
    return idx[0] * dt


print("=== Kuramoto EDS/EDC Simulation ===")
print("Baseline final R:", round(float(baseline[-1]), 4))
print("Forced final R:", round(float(forced[-1]), 4))
print("Baseline max R:", round(float(np.max(baseline)), 4))
print("Forced max R:", round(float(np.max(forced)), 4))
print("Baseline convergence time:", convergence_time(baseline))
print("Forced convergence time:", convergence_time(forced))

print("\nInterpretation:")
print("R(t) serves as measurable proxy for coherence C(t).")
print("If forcing increases R and reduces convergence time,")
print("the system moves toward the EDS stable regime: C(t) > P(t).")
