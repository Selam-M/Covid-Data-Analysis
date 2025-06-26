#  COVID-19 Data Analysis Project – Summary
##  Project Overview

This COVID‑19 Data Analysis project fetches up‑to‑date global case figures, transforms raw data with feature engineering, and generates key visualizations to understand pandemic trends. It helps identify:
- Countries with highest cases & mortality
- How active cases relate to total cases and recoveries
- Regional differences by continent

It's a practical showcase of end-to-end data analytics: API fetch → clean → analyze → visualize.
##  What This Project Does

This project performs a full analysis pipeline for global COVID-19 data:

-  Fetches live data from an external API
-  Cleans and prepares the dataset
-  Performs Exploratory Data Analysis (EDA) to reveal trends
-  Adds new features:
  - `Mortality_Rate = Total_Deaths / Total_Cases`
  - `Active_Cases = Total_Cases - Total_Deaths`
-  Generates visualizations:
  - Bar chart of Top 10 countries by Total Cases
  - Scatter plot of Total Cases vs Total Deaths
  - Pie chart of Total Cases grouped by continent

All plots are saved in the `images/` folder.

---

##  Key Learnings

- **Modularization**: Broke down logic into reusable, clean modules
- **EDA Skills**: Used `.head()`, `.info()`, `.describe()`, and value counts
- **Debugging & Fixes**: Used `print()` and column inspection to solve issues
- **Data Visualization**: Practiced with `pandas`, `matplotlib`, and `seaborn`

---

##  Challenges Overcome

- ❗ `KeyErrors` due to inconsistent column names (e.g. `'Deaths'` vs `'Total_Deaths'`)
- ❗ `NoneType` errors from functions that didn’t return values
- ❗ Module import issues from misorganized folders

---

##  Installation

Install all required Python libraries:

```bash
pip install -r requirements.txt
## How to Run
Launch Jupyter Lab or Notebook and open:
```
nginx
Copy
Edit

THE COVID PROJECT.ipynb
Run all cells step-by-step to reproduce the analysis.

## Tools and Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook
- API Requests (for data fetching)
- Git and GitHub

## Sample Visualizations

Bar chart of top 10 countries by total cases:

![Top 10 Countries by Cases](images/top_10_cases_bar.png)


## How to Run

1. Clone the repo  
2. Install dependencies  
```bash
pip install -r requirements.txt
```


## Key Results / Insights

- Countries with the highest mortality rates differ from those with the highest total cases
- Some continents showed much lower case counts despite high population
- Active cases formed the majority of total cases in most regions


## 📊 View the Project

- 👉 [Run in Google Colab](https://colab.research.google.com/github/Selam-M/Covid-Data-Analysis/blob/main/THE%20COVID%20PROJECT.ipynb)
- 👀 [View in nbviewer](https://nbviewer.org/github/Selam-M/Covid-Data-Analysis/blob/main/THE%20COVID%20PROJECT.ipynb)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Selam-M/Covid-Data-Analysis/blob/main/THE%20COVID%20PROJECT.ipynb)
