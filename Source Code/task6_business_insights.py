
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from pathlib import Path

# Define project paths
BASE_DIR = Path(__file__).resolve().parent.parent
TASK_DIR = Path(__file__).resolve().parent

# Streamlit configuration
st.set_page_config(
    page_title="Netflix Business Intelligence Dashboard",
    page_icon="🎬",
    layout="wide"
)

# Load cleaned dataset
dataset_path = BASE_DIR / "Task 1" / "cleaned_netflix.csv"

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

df = load_data(str(dataset_path))

# Standardize content type values
df["type"] = (
    df["type"]
    .astype(str)
    .str.strip()
    .str.lower()
    .map({
        "movie": "Movie",
        "tv show": "TV Show"
    })
)

# Dashboard title
st.title("🎬 Netflix Business Intelligence Dashboard")

st.markdown(
    "### Comprehensive Data Analysis & Business Insights"
)

st.caption("Auspify Technologies | Internship Task 6")

st.divider()

# Dataset overview
st.subheader("Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Records", f"{len(df):,}")

with col2:
    st.metric(
        "Total Columns",
        len(df.columns)
    )

with col3:
    st.metric(
        "Unique Titles",
        df["show_id"].nunique()
    )

st.divider()

# Dataset information
st.subheader("Dataset Preview")

st.dataframe(
    df.head(10),
    width='stretch'
)

# Data quality analysis
st.subheader("Data Quality Analysis")

quality_report = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str).values,
    "Missing Values": df.isnull().sum().values,
    "Unique Values": df.nunique().values
})

st.dataframe(
    quality_report,
    width='stretch'
)

st.success("Dataset loaded successfully!")
# ==========================================
# INTERACTIVE FILTERS
# ==========================================

st.sidebar.title("Dashboard Filters")

# Content type filter
content_types = ["All"] + sorted(
    df["type"].dropna().unique().tolist()
)

selected_type = st.sidebar.selectbox(
    "Select Content Type",
    content_types
)

# Release year filter
min_year = int(df["release_year"].min())
max_year = int(df["release_year"].max())

selected_years = st.sidebar.slider(
    "Select Release Year Range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

# Apply filters
filtered_df = df.copy()

if selected_type != "All":
    filtered_df = filtered_df[
        filtered_df["type"] == selected_type
    ]

filtered_df = filtered_df[
    filtered_df["release_year"].between(
        selected_years[0],
        selected_years[1]
    )
]

st.sidebar.success(
    f"{len(filtered_df):,} titles selected"
)

# ==========================================
# BUSINESS KPI CARDS
# ==========================================

st.divider()

st.header("Business Performance Overview")

total_titles = filtered_df["show_id"].nunique()

total_movies = filtered_df[
    filtered_df["type"] == "Movie"
]["show_id"].nunique()

total_tv_shows = filtered_df[
    filtered_df["type"] == "TV Show"
]["show_id"].nunique()

total_countries = (
    filtered_df["country"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
    .nunique()
)

movie_percentage = (
    total_movies / total_titles * 100
    if total_titles > 0 else 0
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Titles",
    f"{total_titles:,}"
)

col2.metric(
    "Movies",
    f"{total_movies:,}"
)

col3.metric(
    "TV Shows",
    f"{total_tv_shows:,}"
)

col4.metric(
    "Countries",
    f"{total_countries:,}"
)

st.caption(
    f"Movies account for {movie_percentage:.2f}% "
    "of the filtered content."
)

# ==========================================
# CONTENT TYPE DISTRIBUTION
# ==========================================

st.divider()

st.header("Content Type Analysis")

content_counts = (
    filtered_df["type"]
    .value_counts()
    .reset_index()
)

content_counts.columns = [
    "Content Type",
    "Total Titles"
]

fig_content = px.pie(
    content_counts,
    names="Content Type",
    values="Total Titles",
    hole=0.45,
    title="Movies vs TV Shows Distribution",
    color="Content Type",
    color_discrete_map={
        "Movie": "#E50914",
        "TV Show": "#5646A5"
    }
)

fig_content.update_traces(
    textinfo="label+percent"
)

st.plotly_chart(
    fig_content,
    width='stretch'
)

# ==========================================
# COUNTRY-WISE CONTENT ANALYSIS
# ==========================================

st.divider()

st.header("Geographical Content Distribution")

country_df = filtered_df[
    ["show_id", "country"]
].dropna().copy()

country_df["country"] = (
    country_df["country"].astype(str).str.split(",")
)

country_df = country_df.explode("country")

country_df["country"] = (
    country_df["country"].str.strip()
)

country_df = country_df[
    country_df["country"] != ""
]

country_counts = (
    country_df.groupby("country")["show_id"]
    .nunique()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

country_counts.columns = [
    "Country",
    "Total Titles"
]

fig_country = px.bar(
    country_counts.sort_values("Total Titles"),
    x="Total Titles",
    y="Country",
    orientation="h",
    color="Total Titles",
    title="Top 10 Countries by Netflix Content",
    template="plotly_dark",
    text="Total Titles"
)

st.plotly_chart(
    fig_country,
    width='stretch'
)

# ==========================================
# GENRE DISTRIBUTION
# ==========================================

st.divider()

st.header("Popular Netflix Genres")

genre_df = filtered_df[
    ["show_id", "listed_in"]
].dropna().copy()

genre_df["listed_in"] = (
    genre_df["listed_in"].str.split(",")
)

genre_df = genre_df.explode("listed_in")

genre_df["listed_in"] = (
    genre_df["listed_in"].str.strip()
)

genre_counts = (
    genre_df.groupby("listed_in")["show_id"]
    .nunique()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

genre_counts.columns = [
    "Genre",
    "Total Titles"
]

fig_genre = px.bar(
    genre_counts,
    x="Genre",
    y="Total Titles",
    color="Total Titles",
    title="Top 10 Netflix Genres",
    template="plotly_dark"
)

fig_genre.update_layout(
    xaxis_tickangle=-35
)

st.plotly_chart(
    fig_genre,
    width='stretch'
)
# ==========================================
# RELEASE YEAR TREND ANALYSIS
# ==========================================

st.divider()

st.header("Netflix Content Release Trends")

yearly_data = (
    filtered_df.groupby(
        ["release_year", "type"]
    )["show_id"]
    .nunique()
    .reset_index(name="Total Titles")
)

fig_trend = px.line(
    yearly_data,
    x="release_year",
    y="Total Titles",
    color="type",
    markers=True,
    title="Movies vs TV Shows – Release Year Trends",
    template="plotly_dark",
    color_discrete_map={
        "Movie": "#E50914",
        "TV Show": "#5646A5"
    }
)

fig_trend.update_layout(
    xaxis_title="Release Year",
    yaxis_title="Number of Titles",
    legend_title="Content Type"
)

st.plotly_chart(
    fig_trend,
    width='stretch'
)
# ==========================================
# CONTENT RATING ANALYSIS
# ==========================================

st.divider()

st.header("Content Rating Distribution")

rating_data = (
    filtered_df["rating"]
    .dropna()
    .value_counts()
    .reset_index()
)

rating_data.columns = [
    "Rating",
    "Total Titles"
]

fig_rating = px.bar(
    rating_data,
    x="Rating",
    y="Total Titles",
    color="Total Titles",
    title="Netflix Content by Rating",
    template="plotly_dark",
    text="Total Titles"
)

st.plotly_chart(
    fig_rating,
    width='stretch'
)
# ==========================================
# BUSINESS INSIGHTS & RECOMMENDATIONS
# ==========================================

st.divider()

st.header("Business Insights & Recommendations")

# 1. Content Type Insight

st.subheader("1. Content Type Insights")

if total_titles > 0:

    movie_pct = total_movies / total_titles * 100
    tv_pct = total_tv_shows / total_titles * 100

    st.info(
        f"Movies account for {movie_pct:.2f}% "
        f"of the Netflix content library, while "
        f"TV Shows account for {tv_pct:.2f}%."
    )

    if movie_pct > tv_pct:
        st.write(
            "Insight: Movies represent the larger "
            "share of the available content library."
        )


# 2. Country Insight

st.subheader("2. Geographical Insights")

if not country_counts.empty:

    top_country = country_counts.iloc[0]["Country"]
    top_country_count = country_counts.iloc[0]["Total Titles"]

    st.success(
        f"{top_country} is the leading country "
        f"with {top_country_count} titles "
        f"in the selected dataset."
    )


# 3. Genre Insight

st.subheader("3. Genre Insights")

if not genre_counts.empty:

    top_genre = genre_counts.iloc[0]["Genre"]
    top_genre_count = genre_counts.iloc[0]["Total Titles"]

    st.info(
        f"{top_genre} is the most represented genre "
        f"with {top_genre_count} titles."
    )


# 4. Release Year Insight

st.subheader("4. Release Year Insights")

if not filtered_df.empty:

    release_counts = (
        filtered_df.groupby("release_year")["show_id"]
        .nunique()
    )

    peak_year = int(release_counts.idxmax())
    peak_count = int(release_counts.max())

    st.success(
        f"{peak_year} was the year with the highest "
        f"number of content releases in the selected data, "
        f"with {peak_count} titles."
    )


# 5. Business Recommendations

st.divider()

st.subheader("Actionable Business Recommendations")

recommendations = [
    (
        "Content Portfolio",
        "Evaluate the balance between Movies and TV Shows "
        "when planning future content acquisitions."
    ),
    (
        "Geographical Expansion",
        f"Study audience demand and content opportunities "
        f"in leading markets such as {top_country if not country_counts.empty else 'top countries'}."
    ),
    (
        "Genre Strategy",
        f"Evaluate audience engagement and investment "
        f"opportunities in {top_genre if not genre_counts.empty else 'popular genres'}."
    ),
    (
        "Content Planning",
        "Use historical release-year trends to support "
        "content acquisition and release planning."
    )
]

for title, recommendation in recommendations:

    with st.expander(title):
        st.write(recommendation)


st.caption(
    "Note: These recommendations are based on content "
    "catalogue patterns. Actual audience demand, viewing "
    "hours and engagement data are not included."
)

# ==========================================
# FINAL EXECUTIVE REPORT & DOWNLOADS
# ==========================================

from io import BytesIO
from datetime import datetime
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from xml.sax.saxutils import escape

st.divider()

st.header("Final Executive Report & Downloads")

# Calculate report metrics
report_total = len(filtered_df)

report_movies = total_movies
report_tv = total_tv_shows

report_movie_pct = (
    report_movies / report_total * 100
    if report_total else 0
)

# Identify leading country
report_country = (
    str(country_counts.iloc[0]["Country"])
    if not country_counts.empty else "Not available"
)

report_country_count = (
    int(country_counts.iloc[0]["Total Titles"])
    if not country_counts.empty else 0
)

# Identify leading genre
report_genre = (
    str(genre_counts.iloc[0]["Genre"])
    if not genre_counts.empty else "Not available"
)

report_genre_count = (
    int(genre_counts.iloc[0]["Total Titles"])
    if not genre_counts.empty else 0
)

# Identify peak release year
if not filtered_df.empty:
    report_year_counts = (
        filtered_df.groupby("release_year")["show_id"]
        .nunique()
    )

    report_peak_year = int(report_year_counts.idxmax())
    report_peak_count = int(report_year_counts.max())
else:
    report_peak_year = "Not available"
    report_peak_count = 0

# Generate text report
report_text = f"""
NETFLIX BUSINESS INTELLIGENCE REPORT
Auspify Technologies Internship - Task 6

Generated On: {datetime.now().strftime("%d-%m-%Y %H:%M")}

1. DATASET OVERVIEW

Total Titles: {report_total}
Movies: {report_movies}
TV Shows: {report_tv}
Countries Represented: {total_countries}

2. CONTENT TYPE ANALYSIS

Movies Percentage: {report_movie_pct:.2f}%
TV Shows Percentage: {100 - report_movie_pct:.2f}%

3. GEOGRAPHICAL ANALYSIS

Leading Country: {report_country}
Number of Titles: {report_country_count}

4. GENRE ANALYSIS

Leading Genre: {report_genre}
Number of Titles: {report_genre_count}

5. RELEASE YEAR ANALYSIS

Peak Release Year: {report_peak_year}
Number of Titles: {report_peak_count}

6. BUSINESS RECOMMENDATIONS

1. Evaluate the balance between Movies and TV Shows.
2. Study content opportunities in leading geographical markets.
3. Evaluate investment opportunities in popular genres.
4. Use historical release trends for content planning.

7. CONCLUSION

The analysis provides insights into Netflix's content
distribution, geographical representation, genre patterns,
and historical release trends.

These insights can support data-driven content planning
and business strategy.

Note: This report analyzes catalogue data, not actual
viewer engagement or streaming performance.
"""

# Display report
st.subheader("Executive Report Preview")

st.text(report_text)

# Download TXT
st.download_button(
    label="Download Business Insights Report (TXT)",
    data=report_text,
    file_name="Netflix_Business_Insights_Report.txt",
    mime="text/plain"
)

# Download filtered dataset
csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Dataset (CSV)",
    data=csv_data,
    file_name="Netflix_Filtered_Dataset.csv",
    mime="text/csv"
)

st.success("All report downloads are ready!")
