def add_mortality_rate(df):
    """
    Adds a Mortality_Rate column calculated as Total_Deaths / Total_Cases.
    """
    df['Mortality_Rate'] = df['Total_Deaths'] / df['Total_Cases']
    return df

def add_active_cases(df):
    """
    Adds an Active_Cases column calculated as Total_Cases - Total_Deaths.
    """
    df['Active_Cases'] = df['Total_Cases'] - df['Total_Deaths']
    return df