# -----------------------------------------------------------
# Data Engineering Capstone: Stock Data Pipeline
# -----------------------------------------------------------

import pandas as pd
import os 

# --- Step 1: Load Dataset ---
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, '..', 'data', 'all_stocks_5yr.csv')

df = pd.read_csv(data_path)
print("\n--- Original Dataset ---")
print("Total rows:", len(df))


# --- Step 2: Filter Selected Companies ---
selected_companies = [
    'AAPL', 'MSFT', 'GOOG', 'AMZN', 'TSLA',
    'META', 'NVDA', 'NFLX', 'INTC', 'CSCO', 'ORCL'
]

df = df[df['Name'].isin(selected_companies)]

print("\n--- After Filtering Companies ---")
print("Rows:", len(df))


# --- Step 3: Data Cleaning ---
# Remove duplicates
df = df.drop_duplicates()

print("\n--- After Removing Duplicates ---")
print("Rows:", len(df))


# --- Step 4: Handling Missing Data ---

print("\n--- Missing Values BEFORE Handling ---")
print(df.isnull().sum())

# Drop missing values
df = df.dropna()

print("\n--- After Handling Missing Data ---")
print("Rows:", len(df))


# --- Step 5: Data Transformation ---
# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Sort values
df = df.sort_values(by=['Name', 'date'])

print("\n--- After Data Transformation ---")
print(df.head())


# --- Step 6: Feature Engineering ---
# Daily Return
df['daily_return'] = df.groupby('Name')['close'].pct_change()

print("\n--- After Feature Engineering ---")
print(df.head(10))

print("\n--- Missing Values AFTER Feature Engineering ---")
print(df.isnull().sum())

# 7-day Moving Average
df['moving_avg_7'] = df.groupby('Name')['close'].rolling(window=7).mean().reset_index(0, drop=True)

print("\n--- After Feature Engineering ---")
print(df.head(10))


# --- Step 7: Save Cleaned Data ---
output_path = os.path.join(base_dir, '..', 'output', 'cleaned_stock_data.csv')

df.to_csv(output_path, index=False)
print("\n Cleaned dataset saved as 'cleaned_stock_data.csv'")


# --- Step 8: Summary ---
print("\n--- Final Summary ---")
print("Final dataset rows:", len(df))
print("Columns:", df.columns)