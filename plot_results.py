import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Plot Kuramoto Simulation Results for EDS/EDC
# ------------------------------------------------------------
# This script reproduces baseline and forced synchronization
# and visualizes R(t), the operational proxy for coordinated
# structural coherence C(t).
#
# In the EDS framework:
#
# C(t) does not represent simple synchronization alone.
#
# C(t) represents:
# - coordinated subsystem dynamics
# - retained structural coherence
# - synchronized operational continuity
# - regenerative alignment of interacting components
#
# R(t) is used here as an experimentally measurable proxy
# for the synchronization component of C(t).
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

omega = np.random.normal(
    loc=1.0,
    scale=0.15,
    size=N
)


def order_parameter(phi):
    """
    Kuramoto global order parameter.

    R(t) ∈ [0, 1]

    R → 1 :
        strong phase synchronization

    R → 0 :
        incoherent regime

    In EDS/EDC:
        R(t) serves as an operationally measurable
        synchronization proxy for C(t).
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

        # ----------------------------------------------------
        # Coupling dynamics
        # ----------------------------------------------------

        phase_diff = phi[None, :] - phi[:, None]

        coupling = np.sum(
            np.sin(phase_diff),
            axis=1
        ) / N

        # ----------------------------------------------------
        # External coherent forcing
        # ----------------------------------------------------

        forcing = F_ext * np.sin(
            omega_ext * t - phi
        )

        # ----------------------------------------------------
        # Stochastic noise
        # ----------------------------------------------------

        noise = eta * np.random.randn(N)

        # ----------------------------------------------------
        # Full phase dynamics
        # ----------------------------------------------------

        dphi = (
            omega
            + K * coupling
            + forcing
            + noise
        )

        phi = phi + dphi * dt

        # ----------------------------------------------------
        # Record synchronization metric
        # ----------------------------------------------------

        R_values.append(order_parameter(phi))

    return np.array(R_values)


# ------------------------------------------------------------
# Run simulations
# ------------------------------------------------------------

baseline = run_simulation(F_ext_baseline)

forced = run_simulation(F_ext_forced)

time = np.arange(steps) * dt

# ------------------------------------------------------------
# Plot results
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    time,
    baseline,
    label="Baseline (F_ext = 0)"
)

plt.plot(
    time,
    forced,
    label="Forced (F_ext = 0.6)"
)

plt.axhline(
    0.7,
    linestyle="--",
    label="R_threshold = 0.7"
)

plt.xlabel("Time")

plt.ylabel("Synchronization Proxy R(t)")

plt.title(
    "Kuramoto Synchronization: Baseline vs Forced"
)

plt.legend()

plt.grid(True)

plt.savefig(
    "kuramoto_results.png",
    dpi=300
)

plt.show()

print("Plot saved as kuramoto_results.png")
