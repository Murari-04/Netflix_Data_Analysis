# ==========================================
# TASK 5: CONTENT RATING & GENRE ANALYSIS
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from pathlib import Path

# Define project paths
BASE_DIR = Path(__file__).resolve().parent.parent
TASK_DIR = Path(__file__).resolve().parent

# Load cleaned dataset
dataset_path = BASE_DIR / "Task 1" / "cleaned_netflix.csv"

df = pd.read_csv(dataset_path)

print("Dataset loaded successfully!")

print("Dataset Shape:", df.shape)

print("\nDataset Columns:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head())
# ==========================================
# RATING CATEGORY ANALYSIS
# ==========================================

# Check rating values
print("\nRating Categories:")
print(df["rating"].value_counts())

# Handle missing and blank ratings
rating_df = df[
    df["rating"].notna()
].copy()

rating_df["rating"] = (
    rating_df["rating"]
    .astype(str)
    .str.strip()
)

rating_df = rating_df[
    rating_df["rating"] != ""
]

# Calculate rating distribution
rating_counts = (
    rating_df["rating"]
    .value_counts()
    .sort_values(ascending=False)
)

print("\nRating Distribution:")
print(rating_counts)

# Export rating analysis
rating_counts.to_csv(
    TASK_DIR / "rating_distribution.csv",
    header=["Total_Titles"]
)

print("\nRating analysis completed!")
# ==========================================
# GENRE ANALYSIS
# ==========================================

# Select required columns
genre_df = df[
    ["show_id", "title", "type", "listed_in"]
].copy()

# Remove missing genres
genre_df = genre_df.dropna(
    subset=["listed_in"]
)

# Split multiple genres
genre_df["listed_in"] = (
    genre_df["listed_in"].str.split(",")
)

# Expand genres into separate rows
genre_df = genre_df.explode("listed_in")

# Remove extra spaces
genre_df["listed_in"] = (
    genre_df["listed_in"].str.strip()
)

# Count unique titles by genre
genre_counts = (
    genre_df.groupby("listed_in")["show_id"]
    .nunique()
    .sort_values(ascending=False)
)

print("\nTop 15 Netflix Genres:")
print(genre_counts.head(15))

# Export genre analysis
genre_counts.to_csv(
    TASK_DIR / "genre_distribution.csv",
    header=["Total_Titles"]
)

print("\nGenre analysis completed!")
# ==========================================
# INTERACTIVE RATING CHART
# ==========================================

rating_chart_data = (
    rating_counts
    .reset_index()
)

rating_chart_data.columns = [
    "Rating",
    "Total Titles"
]

fig = px.bar(
    rating_chart_data,
    x="Rating",
    y="Total Titles",
    color="Rating",
    title="Netflix Content Distribution by Rating",
    text="Total Titles",
    template="plotly_white"
)

fig.update_layout(
    xaxis_title="Content Rating",
    yaxis_title="Number of Titles",
    showlegend=False
)

fig.write_html(
    TASK_DIR / "interactive_rating_chart.html"
)

fig.show()
# ==========================================
# INTERACTIVE GENRE DISTRIBUTION CHART
# ==========================================

top_genres = genre_counts.head(15).reset_index()

top_genres.columns = [
    "Genre",
    "Total Titles"
]

fig_genre = px.bar(
    top_genres.sort_values("Total Titles"),
    x="Total Titles",
    y="Genre",
    orientation="h",
    color="Total Titles",
    text="Total Titles",
    title="Top 15 Netflix Genres",
    template="plotly_white"
)

fig_genre.update_layout(
    xaxis_title="Number of Titles",
    yaxis_title="Genre"
)

fig_genre.write_html(
    TASK_DIR / "interactive_genre_chart.html"
)

fig_genre.show()
# ==========================================
# RATING DISTRIBUTION BY CONTENT TYPE
# ==========================================

rating_type = (
    rating_df.groupby(["rating", "type"])["show_id"]
    .nunique()
    .reset_index(name="Total Titles")
)

print("\nRating Distribution by Content Type:")
print(rating_type.head(20))

fig_rating_type = px.bar(
    rating_type,
    x="rating",
    y="Total Titles",
    color="type",
    barmode="group",
    title="Content Ratings: Movies vs TV Shows",
    template="plotly_white"
)

fig_rating_type.update_layout(
    xaxis_title="Content Rating",
    yaxis_title="Number of Titles",
    legend_title="Content Type"
)

fig_rating_type.write_html(
    TASK_DIR / "rating_by_content_type.html"
)

fig_rating_type.show()
# ==========================================
# GENRE DISTRIBUTION BY CONTENT TYPE
# ==========================================

genre_type = (
    genre_df.groupby(["listed_in", "type"])["show_id"]
    .nunique()
    .reset_index(name="Total Titles")
)

top_genre_names = genre_counts.head(10).index

genre_type_top10 = genre_type[
    genre_type["listed_in"].isin(top_genre_names)
]

fig_genre_type = px.bar(
    genre_type_top10,
    x="listed_in",
    y="Total Titles",
    color="type",
    barmode="group",
    title="Top 10 Genres: Movies vs TV Shows",
    template="plotly_white"
)

fig_genre_type.update_layout(
    xaxis_title="Genre",
    yaxis_title="Number of Titles",
    xaxis_tickangle=-35
)

fig_genre_type.write_html(
    TASK_DIR / "genre_by_content_type.html"
)

fig_genre_type.show()
# ==========================================
# BUSINESS INSIGHTS REPORT
# ==========================================

top_rating = rating_counts.idxmax()
top_rating_count = rating_counts.max()

top_genre = genre_counts.idxmax()
top_genre_count = genre_counts.max()

total_rated_titles = rating_df["show_id"].nunique()
total_genres = genre_counts.shape[0]

report = f"""
NETFLIX CONTENT RATING AND GENRE ANALYSIS
Auspify Technologies Internship
==========================================

DATASET OVERVIEW:

Total Netflix Titles: {len(df)}
Titles with Rating Information: {total_rated_titles}
Total Genres Identified: {total_genres}

RATING ANALYSIS:

Most Common Rating: {top_rating}
Number of Titles: {top_rating_count}

TOP 10 RATINGS:

{rating_counts.head(10).to_string()}

GENRE ANALYSIS:

Most Common Genre: {top_genre}
Number of Titles: {top_genre_count}

TOP 10 GENRES:

{genre_counts.head(10).to_string()}

BUSINESS INSIGHTS:

1. {top_rating} is the most frequently
   occurring content rating.

2. {top_genre} is the most frequently
   occurring genre in the dataset.

3. Rating distribution helps understand
   the audience classification of content.

4. Genre distribution provides insights
   into Netflix's content variety.

5. Comparing ratings and genres across
   Movies and TV Shows helps identify
   differences in content distribution.

CONCLUSION:

The analysis explores Netflix content
ratings, genre distribution and content
type comparisons to understand the
composition of its content library.

==========================================
TASK 5 COMPLETED SUCCESSFULLY!
"""

report_path = TASK_DIR / "task5_rating_genre_report.txt"

with open(report_path, "w", encoding="utf-8") as file:
    file.write(report)

print(report)

print("Task 5 report saved successfully!")