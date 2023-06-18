import pandas as pd

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'

# Read the dataset and set 'user_id' as the index
users = pd.read_csv(url, sep='|', index_col='user_id')

# Display the first 10 entries
print("--------First 10 entries-------")
print(users.head(10))

# Display the last 10 entries
print("--------Last 10 entries-------")
print(users.tail(10))

# Number of observations in the dataset
print("Number of Observations:", len(users))

# Number of columns in the dataset
print("Number of Columns:", len(users.columns))

# Print the name of all the columns
print("Column Names:")
print(users.columns)

# How is the dataset indexed
print("Dataset Index:")
print(users.index)

# Data type of each column
print("Data Types:")
print(users.dtypes)

# Print only the 'occupation' column
print("Occupation Column:")
print(users['occupation'])

# Number of different occupations
print("Number of Different Occupations:", users['occupation'].nunique())

# Most frequent occupation
print("Most Frequent Occupation:")
print(users['occupation'].mode())

# DataFrame info
print("DataFrame Info:")
print(users.info())

# Describe all columns
print("Describe All Columns:")
print(users.describe())

# Summarize only the 'occupation' column
print("Summarize 'occupation' Column:")
print(users['occupation'].value_counts())

# Mean age of users
print("Mean Age of Users:", users['age'].mean())

# Age with least occurrence
print("Age with Least Occurrence:", users['age'].value_counts().idxmin())