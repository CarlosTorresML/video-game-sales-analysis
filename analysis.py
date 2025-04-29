import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_csv('dataset_games.csv')

# Display the first 5 rows to inspect the data
print(df.head())

# Replace commas with dots in the 'Global_Sales' column to prepare for float conversion
df['Global_Sales'] = df['Global_Sales'].str.replace(',', '.')

# Convert 'Global_Sales' from string to float
df['Global_Sales'] = df['Global_Sales'].astype(float)

# Check for missing values in each column
print(df.isnull().sum())

# Count the number of games released per platform
print(df['Platform'].value_counts())

# Display the average global sales per platform, from highest to lowest
print(df.groupby('Platform')['Global_Sales'].mean().sort_values(ascending=False))

# Display the total global sales per genre, from highest to lowest (Top 5)
print(df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False).head(5))

# Display the most common genres by number of games released (Top 5)
print(df['Genre'].value_counts().head(5))
