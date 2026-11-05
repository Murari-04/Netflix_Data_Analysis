# ==========================================
# TASK 3: COUNTRY-WISE NETFLIX CONTENT ANALYSIS
# ==========================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Define project paths
BASE_DIR = Path(__file__).resolve().parent.parent
TASK_DIR = Path(__file__).resolve().parent

dataset_path = BASE_DIR / "Task 1" / "cleaned_netflix.csv"

df = pd.read_csv(dataset_path)

print("Dataset loaded successfully!")

print("Dataset Shape:", df.shape)

print("\nCountry Column:")
print(df["country"].head(10))

# Select required columns
country_df = df[["show_id", "title", "type", "country"]].copy()

# Remove records with missing or Unknown countries
country_df = country_df.dropna(subset=["country"])

country_df = country_df[
    country_df["country"].str.strip().str.casefold() != "unknown"
]

# Split multiple countries
country_df["country"] = country_df["country"].str.split(",")

# Expand each country into a separate row
country_df = country_df.explode("country")

# Remove extra spaces
country_df["country"] = country_df["country"].str.strip()

# Remove empty country values
country_df = country_df[
    country_df["country"].ne("")
]

print("\nCleaned Country Data:")
print(country_df.head(10))
print("\nTotal Country Records:", len(country_df))

# Group content by country
country_counts = (
    country_df.groupby("country")["show_id"]
    .nunique()
    .sort_values(ascending=False)
)
print("\nTop 10 Countries by Netflix Content:")
print(country_counts.head(10))

# Get top 10 countries
top_countries = country_counts.head(10)

print("\nTop 10 Content Producing Countries:")

for country, count in top_countries.items():
    print(f"{country}: {count}")

# Create top 10 country chart
plt.figure(figsize=(12, 7))

sns.barplot(
    x=top_countries.values,
    y=top_countries.index
)
plt.title(
    "Top 10 Countries by Netflix Content",
    fontsize=16,
    fontweight="bold"
)
plt.xlabel("Number of Titles")
plt.ylabel("Country")

# Display values
for i, value in enumerate(top_countries.values):
    plt.text(
        value + 5,
        i,
        str(value),
        va="center"
    )

plt.tight_layout()
# Save chart
plt.savefig(
    TASK_DIR / "top_10_countries.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# Country-wise content type analysis
country_type = (
    country_df.groupby(["country", "type"])["show_id"]
    .nunique()
    .reset_index(name="count")
)

# Filter top 10 countries
top_country_names = top_countries.index

country_type_top10 = country_type[
    country_type["country"].isin(top_country_names)
]

# Create grouped bar chart
plt.figure(figsize=(14, 7))

sns.barplot(
    data=country_type_top10,
    x="country",
    y="count",
    hue="type"
)
plt.title(
    "Movies vs TV Shows Across Top 10 Countries",
    fontsize=15,
    fontweight="bold"
)
plt.xlabel("Country")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45, ha="right")

plt.legend(title="Content Type")

plt.tight_layout()

plt.savefig(
    TASK_DIR / "country_content_comparison.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
# Generate business insights

top_country = country_counts.index[0]
top_country_count = country_counts.iloc[0]

report = f"""
NETFLIX COUNTRY-WISE CONTENT ANALYSIS
Auspify Technologies Internship
====================================

Dataset Overview:
Original Records: {len(df)}
Country Records After Expansion: {len(country_df)}
Countries Represented: {country_counts.shape[0]}

TOP 10 COUNTRIES BY CONTENT:

{top_countries.to_string()}

BUSINESS INSIGHTS:

1. {top_country} has the highest number
   of Netflix titles in this dataset,
   with {top_country_count} titles.

2. Netflix content is distributed
   across multiple countries.

3. Different countries contribute
   to the platform's content library.

4. Movies and TV Shows can be compared
   across countries to understand
   content distribution patterns.

CONCLUSION:

The analysis identifies the leading
countries contributing to Netflix's
content library and provides insights
into country-wise content distribution.
====================================
Task 3 Completed Successfully!
"""
# Save report
report_path = TASK_DIR / "task3_country_analysis_report.txt"

with open(report_path, "w", encoding="utf-8") as file:
    file.write(report)
print(report)
print("Country analysis report saved successfully!")
