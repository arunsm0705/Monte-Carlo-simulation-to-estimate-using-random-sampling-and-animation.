import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# Ask user for number of points

total_points = int(input("Enter number of random points: "))

inside = 0
total_generated = 0

x_inside = []
y_inside = []
x_outside = []
y_outside = []

# Create Figure

fig, ax = plt.subplots(figsize=(7,7))

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

ax.set_title("Animated Monte Carlo Estimation of π\n(Law of Large Numbers Demonstration)")
ax.set_xlabel("X Coordinate")
ax.set_ylabel("Y Coordinate")

# Draw unit circle
circle = plt.Circle((0, 0), 1, fill=False, linewidth=2)
ax.add_patch(circle)

# Scatter plots
inside_scatter = ax.scatter([], [], s=5, label="Points Inside Circle")
outside_scatter = ax.scatter([], [], s=5, label="Points Outside Circle")

ax.legend(loc="upper right")

# Text inside graph
info_text = ax.text(-0.95, 0.85, "", fontsize=11)

# Annotation
ax.annotate(
    "Monte Carlo Method:\n"
    "π ≈ 4 × (Inside Points / Total Points)\n"
    "As trials increase, estimate converges to true π.",
    xy=(-0.95, -0.75),
    fontsize=9
)

# Update Function

def update(frame):
    global inside, total_generated

    points_per_frame = 100

    for _ in range(points_per_frame):

        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        total_generated += 1

        if x*x + y*y <= 1:
            x_inside.append(x)
            y_inside.append(y)
            inside += 1
        else:
            x_outside.append(x)
            y_outside.append(y)

    inside_scatter.set_offsets(np.column_stack((x_inside, y_inside)))
    outside_scatter.set_offsets(np.column_stack((x_outside, y_outside)))

    if total_generated > 0:
        pi_estimate = 4 * inside / total_generated

        info_text.set_text(
            f"Estimated π = {pi_estimate:.6f}\n"
            f"Total Points = {total_generated}\n"
            f"Inside Points = {inside}"
        )

# Run Animation

ani = FuncAnimation(
    fig,
    update,
    frames=total_points // 100,
    interval=1,
    repeat=False
)

plt.grid(True)
plt.show()

# Final Analysis Section

if total_generated > 0:

    experimental_pi = 4 * inside / total_generated
    theoretical_pi = np.pi

    absolute_error = abs(theoretical_pi - experimental_pi)
    percentage_error = (absolute_error / theoretical_pi) * 100

    print("\n========== ANALYSIS ==========")
    print("Theoretical Value of π  :", round(theoretical_pi, 6))
    print("Experimental Value of π :", round(experimental_pi, 6))
    print("Absolute Error           :", round(absolute_error, 6))
    print("Percentage Error (%)     :", round(percentage_error, 4))

    print("\nExplanation:")
    print("This simulation uses random sampling to estimate π using the Monte Carlo method.")
    print("As predicted by the Law of Large Numbers, the experimental value approaches")
    print("the theoretical value of π as the number of trials increases.")
    print("Small deviations occur due to randomness, but error decreases with more samples.")