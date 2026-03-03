import random
import matplotlib.pyplot as plt

# ----------------------------------
# 1. USER INPUTS
# ----------------------------------
start_capital = int(input("Enter starting capital: "))
target_capital = int(input("Enter target capital: "))
bet_size = int(input("Enter bet size per round: "))
prob_win = float(input("Enter probability of winning (e.g., 0.5): "))
num_simulations = int(input("Enter number of simulations: "))

# Basic validation
if start_capital <= 0 or target_capital <= 0:
    print("Capital values must be positive.")
    exit()

if start_capital >= target_capital:
    print("Starting capital must be less than target capital.")
    exit()

if bet_size <= 0:
    print("Bet size must be positive.")
    exit()

if not (0 <= prob_win <= 1):
    print("Probability must be between 0 and 1.")
    exit()

# ----------------------------------
# 2. SIMULATION FUNCTION
# ----------------------------------
def simulate_gambler(start, target, bet, p, max_steps=100000):
    capital = start
    history = [capital]
    steps = 0

    while capital > 0 and capital < target and steps < max_steps:
        if random.random() < p:
            capital += bet
        else:
            capital -= bet

        history.append(capital)
        steps += 1

    return capital, history


# ----------------------------------
# 3. PLOT SAMPLE TRAJECTORIES
# ----------------------------------
plt.figure(figsize=(10, 6))

for i in range(5):   # Only 5 sample gamblers for visualization
    final_capital, history = simulate_gambler(
        start_capital, target_capital, bet_size, prob_win
    )
    plt.plot(history)

plt.title("Gambler's Ruin: Sample Capital Trajectories")
plt.xlabel("Number of Bets")
plt.ylabel("Capital")

plt.axhline(0, linestyle="--", label="Ruin Level (0)")
plt.axhline(target_capital, linestyle="--", label="Target Level")

plt.legend()
plt.grid(True)

plt.annotate(
    "Each line represents one gambler.\n"
    "Capital fluctuates randomly until\n"
    "reaching 0 (ruin) or target.",
    xy=(10, start_capital),
    fontsize=9
)

plt.show()


# ----------------------------------
# 4. CALCULATE PROBABILITY OF RUIN
# ----------------------------------
ruin_count = 0

for i in range(num_simulations):
    final_capital, _ = simulate_gambler(
        start_capital, target_capital, bet_size, prob_win
    )

    if final_capital <= 0:
        ruin_count += 1

prob_ruin = ruin_count / num_simulations


# ----------------------------------
# 5. THEORETICAL PROBABILITY (ONLY IF p = 0.5)
# ----------------------------------
if prob_win == 0.5:
    theoretical_ruin = 1 - (start_capital / target_capital)
else:
    theoretical_ruin = None


# ----------------------------------
# 6. PRINT ANALYSIS
# ----------------------------------
print("\n========== ANALYSIS ==========")
print("Starting Capital       :", start_capital)
print("Target Capital         :", target_capital)
print("Bet Size               :", bet_size)
print("Winning Probability p  :", prob_win)
print("Number of Simulations  :", num_simulations)

print("\nExperimental Probability of Ruin:", round(prob_ruin, 4))

if theoretical_ruin is not None:
    print("Theoretical Probability of Ruin :", round(theoretical_ruin, 4))

print("\nObservations:")
print("- Capital behaves like a random walk with absorbing boundaries.")
print("- Smaller starting capital increases risk of ruin.")
print("- Larger bet size increases volatility and speeds up ruin.")
print("- For fair game (p = 0.5), experimental results should")
print("  be close to theoretical value 1 - (S/T).")