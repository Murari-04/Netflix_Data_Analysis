# ==========================================
# TASK 4: NETFLIX TREND ANALYSIS BY RELEASE YEAR
# Internship: Auspify Technologies
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Define project paths
BASE_DIR = Path(__file__).resolve().parent.parent
TASK_DIR = Path(__file__).resolve().parent

# Load cleaned dataset
dataset_path = BASE_DIR / "Task 1" / "cleaned_netflix.csv"

df = pd.read_csv(dataset_path)

print("Dataset loaded successfully!")

print("Dataset Shape:", df.shape)

print("\nRelease Year Information:")
print(df["release_year"].describe())
# Check missing values
print("\nMissing Release Years:")
print(df["release_year"].isnull().sum())

# Remove missing release years
df = df.dropna(subset=["release_year"]).copy()

# Convert release year to integer
df["release_year"] = df["release_year"].astype(int)

# Group content by release year
yearly_content = (
    df.groupby("release_year")["show_id"]
    .nunique()
    .sort_index()
)

print("\nYearly Content Distribution:")
print(yearly_content)
# Group by release year and content type
yearly_type = (
    df.groupby(["release_year", "type"])["show_id"]
    .nunique()
    .unstack(fill_value=0)
)

print("\nYearly Movies and TV Shows:")
print(yearly_type.tail(15))
# Calculate yearly growth
yearly_growth = yearly_content.pct_change() * 100

print("\nYearly Content Growth (%):")
print(yearly_growth.tail(15))

# Identify highest content release year
highest_year = yearly_content.idxmax()

highest_count = yearly_content.max()

print("\nHighest Content Release Year:", highest_year)
print("Number of Titles:", highest_count)

# Identify lowest content release year
lowest_year = yearly_content.idxmin()

lowest_count = yearly_content.min()

print("\nLowest Content Release Year:", lowest_year)
print("Number of Titles:", lowest_count)
# Create yearly trend line chart
plt.figure(figsize=(14, 6))

sns.lineplot(
    x=yearly_content.index,
    y=yearly_content.values,
    marker="o"
)

plt.title(
    "Netflix Content Release Trends by Year",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig(
    TASK_DIR / "yearly_content_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# Create comparison line chart
plt.figure(figsize=(14, 7))

for content_type in yearly_type.columns:

    plt.plot(
        yearly_type.index,
        yearly_type[content_type],
        marker="o",
        label=content_type
    )

plt.title(
    "Yearly Movies vs TV Shows Release Trends",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.legend(title="Content Type")

plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig(
    TASK_DIR / "movies_vs_tvshows_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
# Remove missing growth values
growth_data = yearly_growth.dropna()

plt.figure(figsize=(14, 6))

sns.barplot(
    x=growth_data.index,
    y=growth_data.values
)

plt.title(
    "Yearly Netflix Content Growth Rate",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Release Year")
plt.ylabel("Growth Rate (%)")

plt.xticks(rotation=45)

plt.axhline(
    y=0,
    linestyle="--"
)

plt.tight_layout()

plt.savefig(
    TASK_DIR / "yearly_growth_rate.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
# Generate business insights

average_content = yearly_content.mean()

top_5_years = yearly_content.nlargest(5)

latest_year = yearly_content.index.max()

latest_count = yearly_content.loc[latest_year]

report = f"""
NETFLIX RELEASE YEAR TREND ANALYSIS
Auspify Technologies Internship
==================================

DATASET OVERVIEW:

Total Titles Analyzed: {len(df)}

Years Covered:
{yearly_content.index.min()} - {yearly_content.index.max()}

Average Annual Content Releases:
{average_content:.2f}

HIGHEST CONTENT RELEASE YEAR:

Year: {highest_year}
Titles: {highest_count}

LOWEST CONTENT RELEASE YEAR:

Year: {lowest_year}
Titles: {lowest_count}

LATEST RELEASE YEAR:

Year: {latest_year}
Titles: {latest_count}

TOP 5 YEARS BY CONTENT RELEASES:

{top_5_years.to_string()}

BUSINESS INSIGHTS:

1. Netflix content releases vary across
   different release years.

2. The highest content release year was
   {highest_year}, with {highest_count} titles.

3. Yearly growth rates help identify
   periods of content growth and decline.

4. Comparing Movies and TV Shows helps
   understand historical content patterns.

CONCLUSION:

The analysis provides insights into
Netflix's historical content release
patterns and yearly distribution trends.
==================================
Task 4 Completed Successfully!
"""

# Save report
report_path = TASK_DIR / "task4_trend_analysis_report.txt"

with open(report_path, "w", encoding="utf-8") as file:
    file.write(report)

print(report)

print("Trend analysis report saved successfully!")