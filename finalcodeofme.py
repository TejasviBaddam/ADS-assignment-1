import pandas as pd
import matplotlib.pyplot as plt


def read_csv(file_path):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)
    return df


def plot_energy_imports(df):
    # Drop rows with NaN values in any column
    df_cleaned = df.dropna()

    # Extract necessary columns for the plot
    countries = df_cleaned['Country Name']
    years = df_cleaned.columns[4:]  # Columns from 2001 to 2010

    # Create a line plot for each country with custom styles
    plt.figure(figsize=(12, 8))

    # Define a list of colors for the lines
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    for index, (row, color) in enumerate(zip(df_cleaned.iterrows(), colors)):
        plt.plot(years, row[1][4:], marker='o', color=color,
                 label=row[1]['Country Name'], linestyle='-', linewidth=2)

    plt.xlabel('Year', fontsize=16, labelpad=10)
    plt.ylabel('Energy Imports (% of Energy Use)', fontsize=14, labelpad=10)
    plt.title('Energy Imports as a Percentage of Energy Use (2001-2010)',
              fontsize=16, pad=15)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left',
               fontsize=12)  # Place legend outside the plot
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()


def visualize_energy_imports_by_countries(df, country1_name, country2_name, start_year, end_year):
    """
    Visualizes energy imports data as scatter plots for two specific countries over a range of years
    and calculates the correlation between their energy imports.

    Args:
        df (pd.DataFrame): DataFrame containing energy imports data for multiple countries.
        country1_name (str): Name of the first country to compare.
        country2_name (str): Name of the second country to compare.
        start_year (int): Start year for comparison.
        end_year (int): End year for comparison.
    """
    # Filter the DataFrame for the specific countries and range of years
    country1_data = df.loc[df['Country Name'] == country1_name, str(start_year):str(end_year)].values.flatten()
    country2_data = df.loc[df['Country Name'] == country2_name, str(start_year):str(end_year)].values.flatten()

    # Check if the specified years exist in the DataFrame for both countries
    if len(country1_data) < 5 or len(country2_data) < 5:
        print(
            f"Error: Insufficient data for comparison. Minimum 5 years of data required for both countries.")
        return

    # Calculate the correlation between energy imports data of the two countries
    correlation = pd.Series(country1_data).corr(pd.Series(country2_data))
    print(f"Correlation between {country1_name} and {country2_name} for the years {start_year}-{end_year}: {correlation:.2f}")

    # Print the data for visualization
    for year, (data1, data2) in zip(range(start_year, end_year + 1), zip(country1_data, country2_data)):
        print(f"Data for {country1_name} in {year}: {data1}%")
        print(f"Data for {country2_name} in {year}: {data2}%")
        print("---")

    # Create scatter plots for the specific countries and years with styles
    years = list(range(start_year, end_year + 1))
    plt.figure(figsize=(10, 6))
    plt.scatter(years, country1_data, color='green', label=country1_name, marker='o', edgecolors='black', s=100, alpha=0.7, linewidth=1)
    plt.scatter(years, country2_data, color='blue', label=country2_name, marker='o', edgecolors='black', s=100, alpha=0.7, linewidth=1)
    plt.xlabel('Year', fontsize=14, labelpad=10)
    plt.ylabel('Energy Imports (% of Energy Use)', fontsize=14, labelpad=10)
    plt.title(f'Energy Imports Comparison\n({country1_name} vs {country2_name})', fontsize=16, pad=15)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7, linewidth=0.5)
    plt.xticks(years, fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    
    # Add correlation value as text on the plot using f-string
    plt.text(0.5, 0.1, f'Correlation: {correlation:.2f}', transform=plt.gca().transAxes, fontsize=12, color='red')
    
    plt.show()


def visualize_energy_imports_boxplot_all_years_combined(df):
    """
    Visualizes energy imports data as a combined box plot for all years across multiple countries.

    Args:
        df (pd.DataFrame): DataFrame containing energy imports data for multiple countries.
    """
    # Extract years from the DataFrame columns
    years = df.columns[4:]

    # Extract energy imports data for all years and print the data
    for year in years:
        imports_data = df[year].dropna().values
        print(f"Data for {year}: {imports_data}")

    # Set styles
    plt.style.use('seaborn-darkgrid')
    plt.rcParams['font.size'] = 14
    plt.figure(figsize=(10, 6))

    # Create an empty list to store boxplot artist handles
    boxplot_handles = []

    # Iterate through years and create boxes for each year
    for index, year in enumerate(years):
        boxplot = plt.boxplot(df[year].dropna().values, positions=[
                              index], labels=[year], patch_artist=True)

        # Customize boxplot colors
        for box in boxplot['boxes']:
            box.set(facecolor=plt.cm.viridis(index / len(years)))

        # Store boxplot artist handle for creating legend
        boxplot_handles.append(boxplot["boxes"][0])

    # Add legend to the plot
    plt.legend(boxplot_handles, years, title='Year',
               loc='upper left', bbox_to_anchor=(1, 1))

    plt.xlabel('Year', labelpad=10)
    plt.ylabel('Energy Imports (% of Energy Use)', labelpad=10)
    plt.title('Combined Box Plot of Energy Imports for All Years', pad=18)
    plt.grid(True, linestyle='--', alpha=0.7, linewidth=0.5)
    plt.xticks(range(len(years)), years, rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    # Replace 'your_file.csv' with the actual path to your CSV file
    file_path = 'C:/Users/Energy imports, net (% of energy use).csv'
    df = read_csv(file_path)
    plot_energy_imports(df)
    # Print column names to identify how the years are represented in the dataset
    print(df.columns)

# Call the function with your DataFrame df, two country names, and the range of years for comparison
    visualize_energy_imports_by_countries(
        df, 'United Kingdom', 'United States', 2006, 2010)

# Call the function with your DataFrame df
    visualize_energy_imports_boxplot_all_years_combined(df)


if __name__ == "__main__":
    main()
