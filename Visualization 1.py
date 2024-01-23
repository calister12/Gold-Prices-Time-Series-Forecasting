import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset from the CSV file
df = pd.read_csv('Daily Prices Preprocessed.csv')

# Assuming the 'Date' column is present, set it as the index
df.set_index('Date', inplace=True)

# Select the top 5 countries based on the mean gold prices
top_countries = df.mean().sort_values(ascending=False).head(5).index

# Plot a line chart for the top 5 countries
plt.figure(figsize=(10, 6))

for country in top_countries:
    plt.plot(df.index, df[country], label=country)

plt.title('Gold Prices per Troy Ounce - Top 5 Countries')
plt.xlabel('Date')
plt.ylabel('Gold Price ($)')
plt.legend()
plt.grid(True)
plt.show()
