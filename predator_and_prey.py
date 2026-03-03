import numpy as np
import matplotlib.pyplot as plt

# Given Parameters

alpha = 0.5     # Prey growth rate
beta = 0.02     # Predation rate
gamma = 0.3     # Predator death rate
delta = 0.01    # Predator reproduction rate

x0 = 40   # Initial prey
y0 = 9    # Initial predator

# Time Settings

t_start = 0
t_end = 100
dt = 0.1

t = np.arange(t_start, t_end, dt)

# Create arrays

x = np.zeros(len(t))
y = np.zeros(len(t))

x[0] = x0
y[0] = y0

# Define Differential Equations

def dx_dt(x, y):
    return alpha * x - beta * x * y

def dy_dt(x, y):
    return delta * x * y - gamma * y

# RK4 Method
for i in range(len(t) - 1):

    k1x = dt * dx_dt(x[i], y[i])
    k1y = dt * dy_dt(x[i], y[i])

    k2x = dt * dx_dt(x[i] + k1x/2, y[i] + k1y/2)
    k2y = dt * dy_dt(x[i] + k1x/2, y[i] + k1y/2)

    k3x = dt * dx_dt(x[i] + k2x/2, y[i] + k2y/2)
    k3y = dt * dy_dt(x[i] + k2x/2, y[i] + k2y/2)

    k4x = dt * dx_dt(x[i] + k3x, y[i] + k3y)
    k4y = dt * dy_dt(x[i] + k3x, y[i] + k3y)

    x[i+1] = x[i] + (k1x + 2*k2x + 2*k3x + k4x) / 6
    y[i+1] = y[i] + (k1y + 2*k2y + 2*k3y + k4y) / 6


# Plot 1: Population vs Time

plt.figure(figsize=(10,6))
plt.plot(t, x, label="Prey Population")
plt.plot(t, y, label="Predator Population")

plt.title("Lotka–Volterra Model\nPopulation vs Time")
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend()
plt.grid(True)

plt.annotate(
    "Oscillatory behavior:\nPrey rises first,\nPredator follows.",
    xy=(20, max(x)*0.7),
    fontsize=9
)

plt.show()

# Plot 2: Phase Plot

plt.figure(figsize=(8,6))
plt.plot(x, y)

plt.title("Phase Space Diagram (Predator vs Prey)")
plt.xlabel("Prey Population")
plt.ylabel("Predator Population")
plt.grid(True)

plt.annotate(
    "Closed loop indicates\ncyclic interaction.",
    xy=(x0, y0),
    fontsize=9
)

plt.show()

# Analysis

print("\n========== ANALYSIS ==========")
print("Initial Prey Population     :", x0)
print("Initial Predator Population :", y0)

print("\nObservations:")
print("- Prey population increases initially due to natural growth.")
print("- Predator population increases after prey grows.")
print("- Increased predators reduce prey population.")
print("- When prey decreases, predator population declines.")
print("- This leads to cyclic oscillations.")
print("- Phase plot shows closed orbit indicating periodic behavior.")