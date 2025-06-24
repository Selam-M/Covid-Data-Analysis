# modules/plots.py

import matplotlib.pyplot as plt

def plot_bar_top_countries(df, column):
    """
    Plot a bar chart of top 10 countries based on a specified column.
    """
    top10 = df.sort_values(by=column, ascending=False).head(10)
    plt.figure(figsize=(10,6))
    plt.bar(top10['Country'], top10[column])
    plt.xticks(rotation=45)
    plt.title(f"Top 10 Countries by {column}")
    plt.tight_layout()
    plt.savefig('images/bar_top_countries.png')
    plt.close()

def plot_scatter(df, x_col, y_col):
    """
    Plot a scatter plot of two columns.
    """
    plt.figure(figsize=(8,6))
    plt.scatter(df[x_col], df[y_col], alpha=0.5)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{y_col} vs {x_col}")
    plt.tight_layout()
    plt.savefig('images/scatter_plot.png')
    plt.close()

def plot_pie_by_group(df, group_col, value_col):
    """
    Plot a pie chart grouping by group_col summing value_col.
    """
    data = df.groupby(group_col)[value_col].sum()
    plt.figure(figsize=(8,8))
    plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
    plt.title(f"{value_col} distribution by {group_col}")
    plt.savefig('images/pie_chart.png')
    plt.close()