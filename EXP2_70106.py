import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Roll No": [106, 105, 104, 103, 102],
    "Name": ["Abhijeet", "Deepak", "Lakshya", "Priya", "Karan"],
    "Marks": [89, 92, 78, 92, 88]
}

df = pd.DataFrame(data)

df["Rank"] = df["Marks"].rank(method="dense", ascending=False).astype(int)

df = df.sort_values(by="Marks", ascending=False)

print("\nStudent Dataset\n")
print(df)

print("\nClass Statistics")
print("----------------")
print("Average Marks :", round(df["Marks"].mean(),2))
print("Highest Marks :", df["Marks"].max())
print("Lowest Marks  :", df["Marks"].min())

colors = ["gold" if m == df["Marks"].max() else "skyblue" for m in df["Marks"]]

plt.figure(figsize=(8,5))
bars = plt.bar(df["Name"], df["Marks"], color=colors)

plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")

for bar in bars:
    plt.text(bar.get_x()+bar.get_width()/2,
             bar.get_height()+0.5,
             str(int(bar.get_height())),
             ha='center')

plt.ylim(0,100)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()

plt.figure(figsize=(7,5))

plt.scatter(df["Roll No"],
            df["Marks"],
            s=180,
            c=df["Marks"],
            cmap="viridis")

for i in range(len(df)):
    plt.text(df["Roll No"].iloc[i],
             df["Marks"].iloc[i]+0.5,
             df["Name"].iloc[i],
             fontsize=9)

plt.title("Roll Number vs Marks")
plt.xlabel("Roll Number")
plt.ylabel("Marks")
plt.colorbar(label="Marks")
plt.grid(True)
plt.show()

plt.figure(figsize=(7,5))

plt.plot(df["Roll No"],
         df["Marks"],
         marker="o",
         linewidth=3)

plt.fill_between(df["Roll No"],
                 df["Marks"],
                 alpha=0.2)

plt.title("Marks Trend")
plt.xlabel("Roll Number")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

plt.figure(figsize=(6,6))

plt.pie(df["Marks"],
        labels=df["Name"],
        autopct="%1.1f%%",
        startangle=90,
        shadow=True)

plt.title("Contribution of Marks")
plt.show()