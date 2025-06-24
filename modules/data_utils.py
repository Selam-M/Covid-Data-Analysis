# modules/data_utils.py

def clean_data(df):
    """
    Drop any rows with missing values.
    """
    return df.dropna()