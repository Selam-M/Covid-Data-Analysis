import pandas as pd

def fetch_covid_data():
    data = {
        'Country': ['A', 'B', 'C'],
        'Total_Cases': [1000, 2000, 3000],
        'Total_Deaths': [50, 100, 150],
        'Continent': ['Asia', 'Europe', 'Africa']
    }
    return pd.DataFrame(data)