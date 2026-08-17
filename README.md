# 🇮🇳 Indian Air Quality Analytics Dashboard

An interactive Tableau project analyzing air pollution patterns across major Indian cities using air quality data from 2015 to 2020.

## 📊 Project Overview

The objective of this project is to analyze air pollution patterns across Indian cities using Tableau.

The project transforms daily air quality data into interactive visualizations that help identify pollution hotspots, seasonal pollution patterns, AQI trends, pollutant relationships, and city-wise pollution rankings.

The analysis focuses on:

- Air Quality Index (AQI) distribution
- City-wise AQI comparison
- Geographic pollution hotspots
- Seasonal and monthly pollution trends
- Year-over-year AQI comparison
- Weekly pollution patterns
- PM2.5 and PM10 concentration trends
- Relationship between PM2.5 and AQI
- SO2 concentration across cities
- AQI health-category distribution

---

## 📁 Dataset

**Source:** [Kaggle – Air Quality Data in India (2015–2020)](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india)

**Format:** CSV

**Granularity:** Daily observations across multiple Indian cities.

The dataset contains air quality measurements including:

- City
- Date
- PM2.5
- PM10
- NO
- NO2
- NOx
- NH3
- SO2
- CO
- O3
- Benzene
- Toluene
- AQI
- AQI Bucket

The original dataset was cleaned and prepared before visualization.

---

## 🧹 Data Cleaning

The data preprocessing was performed using Python and Pandas.

Main preprocessing steps included:

1. Converted the `Date` column to datetime format.
2. Removed the `Xylene` column because of a high percentage of missing values.
3. Performed city-specific median imputation for numeric pollution and AQI columns.
4. Used global median imputation for remaining missing numeric values.
5. Filled missing `AQI_Bucket` values using forward-fill and backward-fill within cities.
6. Exported the cleaned dataset as `city_day_cleaned.csv`.

The cleaning code is available in:

`preprocessing/data_cleaning.py`

---

## 🔗 Tableau Public

View the interactive dashboards on Tableau Public:

[🇮🇳 India Air Pollution Analysis Dashboard](https://public.tableau.com/views/IndiaAirPollutionAnalysisDashboard/GeographicSeasonalTrends?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## 📊 Tableau Dashboards

The project contains two main interactive dashboards.

### 1. Geographic & Seasonal Trends

This dashboard focuses on geographical and time-based patterns in air pollution.

It includes:

- AQI geographic map
- Weekly activity analysis
- Seasonal heatmap
- AQI trend from 2015 to 2020
- Year-over-year AQI comparison
- City-wise filtering

### 2. Pollutant Science & City Rankings

This dashboard focuses on pollutant relationships and city-level comparisons.

It includes:

- AQI category distribution
- Overall average AQI
- Percentage of poor AQI days
- Worst-day AQI
- AQI ranking by city
- PM2.5 and PM10 concentration trends
- PM2.5 vs AQI relationship
- Median SO2 city ranking
- Pollutant contribution analysis

---

## 🔍 Key Insights

### 🌍 Geographic Pollution Hotspots

The analysis identifies Northern India as a major pollution hotspot, with cities such as Delhi showing high average AQI values compared with several coastal regions.

### 🏙️ Most Polluted Cities

Based on average AQI, the analysis identifies the following cities among the highest-ranking pollution locations:

- Ahmedabad
- Delhi
- Patna
- Gurugram
- Lucknow

### 📈 AQI Trend Over Time

The AQI trend from 2015 to 2020 shows significant year-over-year variation, with an overall decrease toward 2020.

### ❄️ Seasonal Pollution Pattern

The seasonal analysis highlights a strong winter pollution spike, particularly during November and December.

### 🦠 2020 Pollution Dip

The year-over-year analysis shows a noticeable decline in pollution during the spring months of 2020, corresponding with the COVID-19 lockdown period.

### 📅 Weekly Pattern

The weekly analysis shows a slight reduction in pollution on weekends in several cities, particularly on Sundays.

### 🌫️ PM2.5 and PM10

PM2.5 and PM10 concentrations show similar seasonal patterns, with both pollutants increasing during periods of higher pollution.

### 📊 PM2.5 and AQI

The analysis shows a strong relationship between PM2.5 concentration and AQI, highlighting PM2.5 as an important contributor to overall air quality conditions.

### 🏭 SO2 City Comparison

The city-wise SO2 analysis highlights differences in pollutant concentrations across cities and provides an indication of locations with stronger industrial pollution signatures.

---

## 📌 Key KPIs

The dashboard highlights important air-quality indicators including:

- Overall Average AQI
- Worst Day AQI
- Percentage of Poor AQI Days

---

## 🖼️ Dashboard Preview

### Geographic & Seasonal Trends

![Geographic & Seasonal Trends](screenshots/Geographical&Seasonal_Trends.png)

### Pollutant Science & City Rankings

![Pollutant Science & City Rankings](screenshots/PollutantScience&cityRankings_.png)

---

## 🛠️ Tools & Technologies

- Tableau Desktop
- Tableau Public
- Python
- Pandas
- CSV
- Data Visualization
- Exploratory Data Analysis

---

## 📂 Project Structure

```text
india-air-pollution-tableau/
│
├── data/
│   └── city_day_cleaned.csv
│
├── preprocessing/
│   └── data_cleaning.py
│
├── screenshots/
│   ├── Geographical&Seasonal_Trends.png
│   └── PollutantScience&cityRankings_.png
│
└── tableau/
    └── India_Air_Pollution_Analysis.twbx
```

---

## 🎯 Conclusion

This project demonstrates how data visualization can transform complex environmental data into meaningful insights.

By combining AQI analysis, pollutant concentrations, seasonal trends, geographic visualization, and city-wise rankings, the dashboards provide a comprehensive view of air quality across Indian cities.

The project demonstrates practical skills in data cleaning, exploratory data analysis, Tableau dashboard development, and communicating data-driven environmental insights.

---

## 👤 Author

**Jinu TS**

B.Voc Data Science

St. Thomas College (Autonomous), Thrissur

---

## 📚 Dataset Attribution

The original dataset was obtained from Kaggle.

The cleaned dataset included in this repository is a processed version used specifically for this Tableau analysis.
