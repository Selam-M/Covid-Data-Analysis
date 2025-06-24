import pandas as pd
from modules.api_fetch    import fetch_covid_data
from modules.data_utils   import clean_data
from modules.features     import add_mortality_rate, add_active_cases
from modules.plots        import plot_bar_top_countries, plot_scatter, plot_pie_by_group

def main():
    df = fetch_covid_data()
    df = clean_data(df)
    df = add_mortality_rate(df)
    df = add_active_cases(df)

    plot_bar_top_countries(df, column='Total_Cases')
    plot_scatter(             df, x_col='Total_Cases', y_col='Total_Deaths')
    plot_pie_by_group(        df, group_col='Continent', value_col='Total_Cases')

    print("✅ All plots saved in the images/ folder.")

if __name__python == "__main__":
    main()