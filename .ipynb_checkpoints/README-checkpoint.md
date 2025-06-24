Covid-19 Data Analysis Project – Summary

* What This Script Does

This project performs a complete analysis pipeline for COVID-19 data:
 • Fetches live data from an external API.
 • Cleans and prepares the dataset (e.g., selecting relevant columns).
 • Performs Exploratory Data Analysis (EDA) to understand the data distribution and spot trends.
 • Adds new features like:
 • Mortality_Rate = Total_Deaths / Total_Cases
 • Active_Cases = Total_Cases - Total_Deaths
 • Generates visualizations:
 • Bar chart of top 10 countries by total cases.
 • Scatter plot of Total Cases vs Total Deaths.
 • Pie chart of total cases grouped by continent.

All plots are saved in the images/ folder.

⸻

* Key Learnings
 • ✅ Modularization: Broke down tasks into reusable, well-organized modules (api_fetch, data_utils, features, plots).
 • ✅ Exploratory Data Analysis (EDA): Learned how to inspect data with .head(), .info(), .describe(), and value counts.
 • ✅ Debugging & Error Handling: Used print statements and column inspection to track and fix bugs.
 • ✅ Data Visualization: Practiced using pandas and matplotlib for real-world insights.

⸻

* Challenges Overcome
 • ** KeyErrors caused by mismatched column names (e.g. 'Deaths' vs 'Total_Deaths').
 • ** Function Failures: Handled NoneType errors from functions not returning DataFrames.
 • ** Modular confusion: Solved import path and organization issues.