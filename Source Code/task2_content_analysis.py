# ==========================================
# TASK 2: CONTENT TYPE ANALYSIS DASHBOARD
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Define project paths
BASE_DIR = Path(__file__).resolve().parent.parent
TASK_DIR = Path(__file__).resolve().parent

# Load cleaned dataset from Task 1
dataset_path = BASE_DIR / "Task 1" / "cleaned_netflix.csv"

df = pd.read_csv(dataset_path)

print("Dataset loaded successfully!")

print("Dataset Shape:", df.shape)

print("\nFirst 5 Records:")
print(df.head())

# Count Movies and TV Shows
content_counts = df["type"].value_counts()

print("\nContent Type Distribution:")
print(content_counts)

# Calculate total content
total_content = len(df)

# Calculate percentages
content_percentages = (
    content_counts / total_content
) * 100

print("\nContent Percentages:")
print(content_percentages)

print("\nTotal Netflix Content:", total_content)

# Create bar chart
plt.figure(figsize=(9, 6))

sns.barplot(
    x=content_counts.index,
    y=content_counts.values
)

plt.title(
    "Netflix Content Distribution: Movies vs TV Shows",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Content Type")
plt.ylabel("Number of Titles")

# Display values above bars
for i, value in enumerate(content_counts.values):
    plt.text(
        i,
        value + 100,
        str(value),
        ha="center",
        fontsize=11
    )

plt.tight_layout()

# Save chart
plt.savefig(
    TASK_DIR / "content_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# Create pie chart
plt.figure(figsize=(8, 8))

plt.pie(
    content_counts.values,
    labels=content_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    explode=(0.05, 0),
    shadow=True
)

plt.title(
    "Netflix Content Type Percentage Distribution",
    fontsize=14,
    fontweight="bold"
)

plt.tight_layout()

# Save chart
plt.savefig(
    TASK_DIR / "content_type_pie_chart.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# Generate business insights

movie_count = content_counts.get("Movie", 0)
tv_count = content_counts.get("TV Show", 0)

movie_percentage = (
    movie_count / total_content
) * 100

tv_percentage = (
    tv_count / total_content
) * 100

report = f"""
NETFLIX CONTENT TYPE ANALYSIS
Auspify Technologies Internship
================================

Dataset Overview:
Total Content: {total_content}

Content Distribution:
Movies: {movie_count}
TV Shows: {tv_count}

Percentage Distribution:
Movies: {movie_percentage:.2f}%
TV Shows: {tv_percentage:.2f}%

BUSINESS INSIGHTS:
1. Movies account for {movie_percentage:.2f}% of
   the Netflix dataset.

2. TV Shows account for {tv_percentage:.2f}% of
   the Netflix dataset.

3. Movies represent the larger content category.

4. Netflix's catalog in this dataset has a
   greater representation of movies than TV shows.

CONCLUSION:
The analysis indicates that movies form the
majority of Netflix's available content in
the provided dataset.

================================
Task 2 Completed Successfully!
"""

# Save report
report_path = TASK_DIR / "task2_analysis_report.txt"

with open(report_path, "w", encoding="utf-8") as file:
    file.write(report)

print(report)

print("Analysis report saved successfully!")