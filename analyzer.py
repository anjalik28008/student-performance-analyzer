import pandas as pd
import matplotlib.pyplot as plt

# Student data
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry"],
    "Math": [85, 42, 78, 95, 60, 55, 88, 73],
    "Science": [90, 38, 82, 88, 72, 48, 91, 65],
    "English": [78, 55, 70, 92, 65, 60, 85, 80]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate total and average
df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Average"] = (df["Total"] / 3).round(2)
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 50 else "Fail")

# Display results
print("===== Student Performance Report =====\n")
print(df[["Name", "Math", "Science", "English", "Average", "Result"]].to_string(index=False))

# Summary
print(f"\n--- Summary ---")
print(f"Total Students : {len(df)}")
print(f"Passed         : {len(df[df['Result'] == 'Pass'])}")
print(f"Failed         : {len(df[df['Result'] == 'Fail'])}")
print(f"Class Average  : {df['Average'].mean().round(2)}")
print(f"Topper         : {df.loc[df['Average'].idxmax(), 'Name']} ({df['Average'].max()})")

# Bar chart
df.plot(x="Name", y=["Math", "Science", "English"], kind="bar", figsize=(10, 6), color=["#4e79a7", "#f28e2b", "#59a14f"])
plt.title("Student Performance Chart")
plt.xlabel("Students")
plt.ylabel("marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
