import pandas as pd  # Importing pandas library

print("Pandas imported successfully!")

# Creating sample dataset
data = {
    "Roll No": [101, 102, 103, 104, 105],
    "Name": ["Abhijeet", "Riya", "Rahul", "Priya", "Karan"],
    "Marks": [85, 92, 78, 92, 88]
}

# Converting dictionary to DataFrame
df = pd.DataFrame(data)

# Displaying the DataFrame
print("Sample Dataset:")
print(df)
print("-" * 30)

# Calculating descriptive statistics
mean_score = df['Marks'].mean()
median_score = df['Marks'].median()
mode_score = df['Marks'].mode()[0]
variance_score = df['Marks'].var()
std_score = df['Marks'].std()

# Printing results
print(f"Mean (Average) Score: {mean_score:.2f}")
print(f"Median (Middle) Score: {median_score:.2f}")
print(f"Mode (Most Frequent) Score: {mode_score}")
print(f"Variance (Spread): {variance_score:.2f}")
print(f"Standard Deviation: {std_score:.2f}")

