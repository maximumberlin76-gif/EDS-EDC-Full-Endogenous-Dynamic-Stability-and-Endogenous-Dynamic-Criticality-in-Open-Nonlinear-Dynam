import numpy as np

# ------------------------------------------------------------
# Minimal Kuramoto Simulation for EDS/EDC
# ------------------------------------------------------------
# Goal:
# Compare baseline synchronization with externally forced synchronization.
#
# R(t) is the Kuramoto synchronization order parameter.
#
# In EDS/EDC:
# - R(t) measures synchronization.
# - R(t) is not identical to C(t).
# - C(t) is the parameter of general endogenous structural coherence.
# - Synchronization may support C(t), but does not define C(t).
# - Real dynamic stability remains governed by:
#
#   C(t) > P(t)
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

R_THRESHOLD = 0.7

np.random.seed(42)

omega = np.random.normal(
    loc=1.0,
    scale=0.15,
    size=N
)


def order_parameter(phi):
    """
    Kuramoto global order parameter.

    R(t) ∈ [0, 1]

    R → 1:
        strong phase synchronization

    R → 0:
        incoherent phase regime

    EDS/EDC distinction:
        R(t) is a measurable synchronization proxy.
        R(t) may support C(t), but R(t) is not C(t).
        C(t) is general endogenous structural coherence.
    """
    return np.abs(np.mean(np.exp(1j * phi)))


def run_simulation(F_ext):
    """
    Run Kuramoto synchronization simulation.

    Parameters
    ----------
    F_ext : float
        External coherent forcing amplitude.

    Returns
    -------
    np.ndarray
        Time series of R(t).
    """

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


def convergence_time(R, threshold=R_THRESHOLD):
    """
    Return the first time when R(t) reaches the threshold.
    """

    idx = np.where(R >= threshold)[0]

    if len(idx) == 0:
        return None

    return idx[0] * dt


baseline = run_simulation(F_ext_baseline)
forced = run_simulation(F_ext_forced)

baseline_conv = convergence_time(baseline)
forced_conv = convergence_time(forced)

print("=== Kuramoto EDS/EDC Simulation ===")
print("Baseline final R:", round(float(baseline[-1]), 4))
print("Forced final R:", round(float(forced[-1]), 4))
print("Baseline max R:", round(float(np.max(baseline)), 4))
print("Forced max R:", round(float(np.max(forced)), 4))
print("Baseline convergence time:", baseline_conv)
print("Forced convergence time:", forced_conv)

print("\nInterpretation:")
print("R(t) measures synchronization, not C(t) itself.")
print("R(t) may serve as a measurable synchronization proxy and support indicator.")
print("If forcing increases R(t) and reduces convergence time,")
print("the synchronization-support layer becomes more accessible.")
print("Real dynamic stability still requires: C(t) > P(t).")
