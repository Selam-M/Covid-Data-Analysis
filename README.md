#  COVID-19 Data Analysis Project – Summary

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

nginx
Copy
Edit

THE COVID PROJECT.ipynb
Run all cells step-by-step to reproduce the analysis.

