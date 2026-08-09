import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = [31, 33, 32, 35, 34, 38, 35]

average = sum(temperature) / len(temperature)
highest = max(temperature)
lowest = min(temperature)

highest_day = days[temperature.index(highest)]
lowest_day = days[temperature.index(lowest)]

plt.figure(figsize=(9, 5))
plt.plot(days, temperature, marker='o', linewidth=2)

for day, temp in zip(days, temperature):
    plt.text(day, temp + 0.3, f"{temp}°C", ha="center")

plt.axhline(average, linestyle="--",
            label=f"Average = {average:.1f}°C")

plt.title("7-Day Weather Temperature Analysis")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")

plt.grid(True, alpha=0.3)
plt.legend()

plt.show()

print("----- Weather Analysis -----")
print(f"Average Temperature : {average:.1f}°C")
print(f"Highest Temperature : {highest}°C on {highest_day}")
print(f"Lowest Temperature  : {lowest}°C on {lowest_day}")

if temperature[-1] > temperature[0]:
    print("Overall Trend: Temperature increased during the week.")
elif temperature[-1] < temperature[0]:
    print("Overall Trend: Temperature decreased during the week.")
else:
    print("Overall Trend: Temperature remained almost the same.")