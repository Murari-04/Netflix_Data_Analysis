# ==========================================
# TASK 1: NETFLIX DATA CLEANING & PREPARATION
# ==========================================

import pandas as pd
import numpy as np
from pathlib import Path

# Define project paths
BASE_DIR = Path(__file__).resolve().parent.parent
TASK_DIR = Path(__file__).resolve().parent

dataset_path = BASE_DIR / "Dataset.csv"

# Load dataset
df = pd.read_csv(dataset_path)

print("Dataset loaded successfully!")
print("Dataset Shape:", df.shape)

print("\nFirst 5 Records:")
print(df.head())

# Dataset information
print("\nDataset Information:")
df.info()

# Statistical summary
print("\nStatistical Summary:")
print(df.describe(include="all"))

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Unique values
print("\nUnique Values:")
print(df.nunique())

# Check missing values before cleaning
missing_before = df.isnull().sum()

print("\nMissing values before cleaning:")
print(missing_before)

# Handle categorical missing values
categorical_cols = df.select_dtypes(
    include="object"
).columns

for col in categorical_cols:
    df[col] = df[col].fillna("Unknown")

# Handle numerical missing values
numerical_cols = df.select_dtypes(
    include="number"
).columns

for col in numerical_cols:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].median())

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Remove duplicate records
duplicates_before = df.duplicated().sum()

df.drop_duplicates(inplace=True)

print("Duplicates before cleaning:", duplicates_before)
print("Duplicates after cleaning:", df.duplicated().sum())

# Remove leading and trailing spaces
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

print("\nFormatting inconsistencies handled.")

# Standardize Type
df["type"] = df["type"].str.title()

# Standardize Rating
df["rating"] = df["rating"].str.upper()

# Standardize Country names and whitespace
def clean_country(value):
    if value == "Unknown":
        return value

    countries = value.split(",")

    countries = [
        country.strip().title()
        for country in countries
    ]

    return ", ".join(countries)

df["country"] = df["country"].apply(clean_country)

print("\nStandardized Type:")
print(df["type"].unique())

print("\nStandardized Ratings:")
print(df["rating"].unique())

print("\nCountry Standardization Completed.")

# Convert date_added into datetime format
df["date_added"] = pd.to_datetime(
    df["date_added"],
    format="mixed",
    errors="coerce"
)

# Export cleaned dataset
output_path = TASK_DIR / "cleaned_netflix.csv"

df.to_csv(output_path, index=False)

print("\nCleaned dataset exported successfully!")
print("Saved location:", output_path)
print("Final Dataset Shape:", df.shape)

# Generate data quality report
quality_report = pd.DataFrame({
    "Column": df.columns,
    "Data_Type": df.dtypes.astype(str).values,
    "Missing_Values": df.isnull().sum().values,
    "Unique_Values": df.nunique().values
})

report_path = TASK_DIR / "data_quality_report.csv"

quality_report.to_csv(report_path, index=False)

print("\nData Quality Report:")
print(quality_report)

print("\nTask 1 Completed Successfully!")