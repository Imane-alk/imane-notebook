import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(df, education_levels):
    """
    Plot wage distribution by education level.

    Parameters:
        df (pd.DataFrame): The DataFrame containing wage data.
        education_levels (list): List of education level columns.
    """
    plt.figure(figsize=(10, 6))
    for level in education_levels:
        sns.kdeplot(df[level], fill=True, label=level)

    plt.title("Distribution of Wages by Education Level")
    plt.xlabel("Wage")
    plt.ylabel("Density")
    plt.legend()
    plt.show()

def plot_wage_trends(df, education_levels):
    """
    Plot wage trends over time by education level.

    Parameters:
        df (pd.DataFrame): The DataFrame containing wage data.
        education_levels (list): List of education level columns.
    """
    plt.figure(figsize=(12, 6))
    for level in education_levels:
        plt.plot(df['year'], df[level], label=level)

    plt.title("Wage Trends Over Time by Education Level")
    plt.xlabel("Year")
    plt.ylabel("Wages")
    plt.legend()
    plt.grid(True)
    plt.show()