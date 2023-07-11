import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Import the dataset using Pandas from the given URL
url = 'https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv'
df = pd.read_csv(url)

# 2. High Level Data Understanding
# a. Find no. of rows & columns in the dataset
rows, columns = df.shape
print("Number of rows:", rows)
print("Number of columns:", columns)

# b. Data types of columns
print("Data types of columns:")
print(df.dtypes)

# c. Info & describe of data in dataframe
print("Info:")
print(df.info())
print("Describe:")
print(df.describe())

# 3. Low Level Data Understanding
# a. Find count of unique values in the location column
unique_locations = df['location'].nunique()
print("Count of unique values in the location column:", unique_locations)

# b. Find which continent has the maximum frequency using value counts
continent_frequency = df['continent'].value_counts()
max_continent_frequency = continent_frequency.idxmax()
print("Continent with maximum frequency:", max_continent_frequency)

# c. Find maximum & mean value in 'total_cases'
max_total_cases = df['total_cases'].max()
mean_total_cases = df['total_cases'].mean()
print("Maximum value in 'total_cases':", max_total_cases)
print("Mean value in 'total_cases':", mean_total_cases)

# d. Find 25%, 50%, and 75% quartile value in 'total_deaths'
quartiles = df['total_deaths'].quantile([0.25, 0.5, 0.75])
print("25% Quartile value in 'total_deaths':", quartiles[0.25])
print("50% Quartile value in 'total_deaths':", quartiles[0.5])
print("75% Quartile value in 'total_deaths':", quartiles[0.75])

# e. Find which continent has the maximum 'human_development_index'
max_hdi_continent = df.loc[df['human_development_index'].idxmax(), 'continent']
print("Continent with the maximum 'human_development_index':", max_hdi_continent)

# f. Find which continent has the minimum 'gdp_per_capita'
min_gdp_continent = df.loc[df['gdp_per_capita'].idxmin(), 'continent']
print("Continent with the minimum 'gdp_per_capita':", min_gdp_continent)

# 4. Filter the dataframe with only specific columns and update the data frame
columns_to_keep = ['continent', 'location', 'date', 'total_cases', 'total_deaths', 'gdp_per_capita', 'human_development_index']
df = df[columns_to_keep]

# 5. Data Cleaning
# a. Remove all duplicate observations
df = df.drop_duplicates()

# b. Find missing values in all columns
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)

# c. Remove all observations where continent column value is missing
df = df.dropna(subset=['continent'])

# d. Fill all missing values with 0
df = df.fillna(0)

# 6. Date time format
# a. Convert date column to datetime format
df['date'] = pd.to_datetime(df['date'])

# b. Create a new column 'month' by extracting month data from the date column
df['month'] = df['date'].dt.month

# 7. Data Aggregation
# a. Find max value in all columns using groupby function on 'continent' column
df_groupby = df.groupby('continent').max().reset_index()

# 8. Feature Engineering
# Create a new feature 'total_deaths_to_total_cases' by ratio of 'total_deaths' column to 'total_cases'
df_groupby['total_deaths_to_total_cases'] = df_groupby['total_deaths'] / df_groupby['total_cases']

# 9. Data Visualization
# a. Perform Univariate analysis on 'gdp_per_capita' column by plotting histogram using seaborn dist plot
sns.displot(df['gdp_per_capita'], kde=False)
plt.title('Histogram of GDP per capita')
plt.show()

# b. Plot a scatter plot of 'total_cases' & 'gdp_per_capita'
plt.scatter(df['total_cases'], df['gdp_per_capita'])
plt.xlabel('Total Cases')
plt.ylabel('GDP per capita')
plt.title('Scatter plot: Total Cases vs GDP per capita')
plt.show()

# c. Plot Pairplot on df_groupby dataset
sns.pairplot(df_groupby)
plt.title('Pairplot of df_groupby dataset')
plt.show()

# d. Plot a bar plot of 'continent' column with 'total_cases'
sns.catplot(x='continent', y='total_cases', kind='bar', data=df_groupby)
plt.title('Bar plot: Continent vs Total Cases')
plt.show()

# 10. Save the df_groupby dataframe in your local drive using pandas.to_csv function
df_groupby.to_csv('df_groupby.csv', index=False)
