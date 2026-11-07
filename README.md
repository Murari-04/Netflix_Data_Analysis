# 🎬 Netflix Data Analysis & Business Intelligence Dashboard

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas" />
  <img src="https://img.shields.io/badge/Plotly-Visualization-3F4F75?logo=plotly" />
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit" />
  <img src="https://img.shields.io/badge/Status-Completed-success" />
</p>

<p align="center">
  <b>End-to-End Data Analytics | Exploratory Data Analysis | Interactive Dashboard | Business Intelligence</b>
</p>

---

## 📌 Project Overview

Netflix Data Analysis & Business Intelligence is an end-to-end data analytics project developed as part of the **Auspify Technologies Data Analytics Internship**.

The project explores Netflix's content catalogue to identify patterns, trends, and insights related to content distribution, countries, genres, ratings, and release years.

It includes six analytical tasks, starting with data cleaning and preprocessing and progressing to an interactive Business Intelligence dashboard built using Python and Streamlit.

The final dashboard provides interactive visualizations, key performance indicators (KPIs), automated business insights, and downloadable analytical reports.

## 🎯 Project Objectives

- Perform data cleaning and preprocessing.
- Analyze Movies and TV Shows distribution.
- Identify top countries contributing Netflix content.
- Examine historical content release trends.
- Analyze content ratings and genre distribution.
- Develop an interactive Business Intelligence dashboard.
- Generate actionable business insights and recommendations.

## 🛠️ Technologies & Tools

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn, Plotly |
| Dashboard Development | Streamlit |
| Interactive Charts | Plotly Express |
| Report Generation | ReportLab |
| Development Environment | VS Code |
| Version Control | Git, GitHub |

## 📂 Project Structure

```text
Netflix_Data_Analysis/
│
├── Datasets/
│   └── Netflix Dataset
│
├── Source Code/
│   ├── Task 1 - Data Cleaning/
│   ├── Task 2 - Content Analysis/
│   ├── Task 3 - Country Analysis/
│   ├── Task 4 - Trend Analysis/
│   ├── Task 5 - Rating and Genre Analysis/
│   └── Task 6 - Business Intelligence/
│
├── Results/
│   
│
├── Reports/
│   ├── Task Reports/
│   └── Business Intelligence Report/
│
├── Screenshots/
│   ├── task1_data_cleaning.png/
│   ├── task2_content_analysis.png/
│   ├── task3_country_analysis.png/
│   └── task4_trend_analysis.png/
│
└── README.md
```

## 📊 Tasks & Implementation

### Task 1 – Data Cleaning and Preprocessing

- Loaded and explored the Netflix dataset.
- Handled missing values.
- Standardized data types.
- Cleaned and transformed dataset columns.
- Generated a data quality report.
- Exported the cleaned dataset.

### Task 2 – Content Type Analysis

- Analyzed Movies and TV Shows distribution.
- Calculated content percentages.
- Created content distribution visualizations.
- Identified key content patterns.

### Task 3 – Country-Wise Content Analysis

- Extracted individual countries from multiple-country records.
- Applied Pandas `split()` and `explode()`.
- Calculated country-wise content counts.
- Identified the top 10 content-producing countries.
- Compared Movies and TV Shows across countries.

### Task 4 – Release Year Trend Analysis

- Analyzed content distribution by release year.
- Compared yearly Movies and TV Shows releases.
- Calculated yearly content growth rates.
- Identified peak content release years.
- Created historical trend visualizations.

### Task 5 – Content Rating and Genre Analysis

- Examined Netflix content rating categories.
- Identified popular genres.
- Compared ratings across Movies and TV Shows.
- Analyzed genre distribution by content type.
- Created interactive Plotly visualizations.

### Task 6 – Netflix Business Intelligence Dashboard

Developed an interactive dashboard using Streamlit.

**Dashboard Features:**

- Interactive content type filter.
- Release year range filter.
- Dynamic KPI cards.
- Movies vs TV Shows distribution.
- Top 10 countries analysis.
- Popular genre analysis.
- Release-year trend visualization.
- Content rating distribution.
- Automated business insights.
- Actionable business recommendations.
- Downloadable PDF, CSV, and TXT reports.

## 📈 Key Findings

The following findings were obtained from the analyzed Netflix dataset:

| Metric | Result |
|---|---:|
| Total Netflix Titles | 8,790 |
| Movies | 6,126 |
| TV Shows | 2,664 |
| Countries Represented | 86 |
| Movies Distribution | 69.69% |
| TV Shows Distribution | 30.31% |
| Leading Country | United States |
| United States Content Count | 3,240 |
| Leading Genre | International Movies |
| International Movies Count | 2,752 |
| Peak Release Year | 2018 |
| Titles Released in Peak Year | 1,146 |

*Note: Country and genre counts may overlap because individual titles can be associated with multiple countries and genres.*

## 📸 Dashboard Preview

The project includes visualizations and an interactive Streamlit dashboard.

Add your actual dashboard screenshots to the `Screenshots/` folder and use the following references:

### 1. Dashboard Overview

![Netflix Dashboard Overview](Screenshots/dashboard_overview.png)

### 2. Content Distribution Analysis

![Content Distribution](Screenshots/content_analysis.png)

### 3. Country-Wise Analysis

![Country Analysis](Screenshots/country_analysis.png)

### 4. Genre and Rating Analysis

![Genre and Rating Analysis](Screenshots/genre_rating_analysis.png)

### 5. Business Insights

![Business Insights](Screenshots/business_insights.png)

## 🚀 Installation and Execution

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/Murari-04/Netflix_Data_Analysis.git
```

### 2. Navigate to the project directory

```bash
cd Netflix_Data_Analysis
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

For Windows:

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn plotly streamlit reportlab
```

### 6. Run the Streamlit dashboard

Navigate to the location of `task6_business_insights.py` and execute:

```bash
streamlit run task6_business_insights.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## 📁 Project Deliverables

The repository contains the following types of deliverables:

- Original and cleaned datasets.
- Data quality reports.
- Python source code for all six tasks.
- Country-wise and content distribution analysis.
- Release-year trend visualizations.
- Interactive rating and genre charts.
- Streamlit Business Intelligence dashboard.
- Executive Business Intelligence PDF report.
- Downloadable CSV and TXT reports.

## 💡 Business Insights & Recommendations

Based on the catalogue analysis:

1. **Content Portfolio:** Evaluate the balance between Movies and TV Shows when planning content acquisitions.
2. **Geographical Opportunities:** Study content opportunities across leading countries and emerging markets.
3. **Genre Strategy:** Evaluate popular genres when planning future content investments.
4. **Release Planning:** Use historical release trends to support content planning and acquisition decisions.

## ⚠️ Data Limitations

This analysis focuses on Netflix catalogue information.

The dataset does not contain actual viewer watch time, subscription revenue, customer engagement, or audience preference information.

Therefore, the findings represent content catalogue patterns and should not be interpreted as direct measures of viewer behaviour or business performance.

## 👨‍💻 Author

**L. Murari**

B.Tech – Computer Science Engineering

- **GitHub:** [Murari-04](https://github.com/Murari-04)
- **Project Repository:** [Netflix_Data_Analysis](https://github.com/Murari-04/Netflix_Data_Analysis)
- **LinkedIn:** [linga-murari](https://www.linkedin.com/in/linga-murari/)

---

<p align="center">
  <b>Developed as part of the Auspify Technologies Data Analytics Internship.</b>
</p>

<p align="center">
  ⭐ If you find this project interesting, consider giving the repository a star!
</p>
