import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# User Input

trials = int(input("Enter number of coin flips: "))

heads = 0
tails = 0

prob_heads = []
prob_tails = []

# Flip multiple coins per frame (for smooth animation)
flips_per_frame = 20
frames = trials // flips_per_frame

# Create Figure

fig, ax = plt.subplots(figsize=(10,6))

ax.set_xlim(0, trials)
ax.set_ylim(0, 1)

ax.set_title("Animated Coin Flip Simulation\n(Law of Large Numbers)")
ax.set_xlabel("Number of Trials")
ax.set_ylabel("Probability")

line_heads, = ax.plot([], [], label="Probability of Heads")
line_tails, = ax.plot([], [], label="Probability of Tails")

ax.axhline(y=0.5, linestyle='--', label="Theoretical Probability = 0.5")
ax.legend()

ax.grid(True)

# Update Function

def update(frame):
    global heads, tails

    for _ in range(flips_per_frame):

        flip = random.randint(0, 1)

        if flip == 1:
            heads += 1
        else:
            tails += 1

        current_trial = heads + tails

        prob_heads.append(heads / current_trial)
        prob_tails.append(tails / current_trial)

    line_heads.set_data(range(len(prob_heads)), prob_heads)
    line_tails.set_data(range(len(prob_tails)), prob_tails)

    return line_heads, line_tails

# Run Animation
ani = FuncAnimation(
    fig,
    update,
    frames=frames,
    interval=10,
    repeat=False
)

plt.show()

experimental_heads = heads / trials
experimental_tails = tails / trials

print("\n========== ANALYSIS ==========")
print("Theoretical Probability :", 0.5)
print("Experimental Heads      :", round(experimental_heads, 6))
print("Experimental Tails      :", round(experimental_tails, 6))

print("\nThis demonstrates the Law of Large Numbers.")
print("As trials increase, probabilities approach 0.5.")

