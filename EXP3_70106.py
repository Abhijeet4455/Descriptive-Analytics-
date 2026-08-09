import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

n = 10
p = 0.5
trials = 10000

results = np.random.binomial(n, p, trials)

mean = np.mean(results)
variance = np.var(results)
std_dev = np.std(results)
minimum = np.min(results)
maximum = np.max(results)

print("\nBinomial Distribution Statistics")
print("--------------------------------")
print("Experimental Mean      :", round(mean, 3))
print("Experimental Variance  :", round(variance, 3))
print("Standard Deviation     :", round(std_dev, 3))
print("Minimum Heads          :", minimum)
print("Maximum Heads          :", maximum)

print("\nTheoretical Values")
print("-------------------")
print("Mean               :", n * p)
print("Variance           :", n * p * (1 - p))

print("\nFrequency Table")
print("----------------")

values, counts = np.unique(results, return_counts=True)

for v, c in zip(values, counts):
    print(f"Heads = {v} : {c} times")

plt.figure(figsize=(9, 6))

sns.histplot(
    results,
    bins=np.arange(-0.5, n + 1.5, 1),
    stat="probability",
    color="skyblue",
    edgecolor="black",
)

plt.axvline(
    mean,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Mean = {mean:.2f}",
)

plt.title("Binomial Distribution of Coin Toss")
plt.xlabel("Number of Heads in 10 Coin Tosses")
plt.ylabel("Probability")
plt.legend()
plt.grid(alpha=0.4)

plt.savefig("binomial_distribution.png", dpi=300)
plt.show()

plt.figure(figsize=(8, 5))

plt.bar(
    values,
    counts,
    color="orange",
    edgecolor="black",
)

plt.title("Frequency of Number of Heads")
plt.xlabel("Number of Heads")
plt.ylabel("Frequency")
plt.grid(axis="y", alpha=0.3)

plt.savefig("frequency_chart.png", dpi=300)

plt.show()