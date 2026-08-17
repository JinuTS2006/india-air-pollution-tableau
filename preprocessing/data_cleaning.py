import pandas as pd

# --- 1. Load the original dataset ---
try:
    df = pd.read_csv("city_day.csv")
    print("File loaded successfully.")
except FileNotFoundError:
    print("Error: Make sure 'city_day.csv' is in the current directory.")
    exit()

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop the 'Xylene' column (over 60% missing data)
df = df.drop(columns=['Xylene'])
print("Dropped 'Xylene' column.")

# --- 2. Define Numeric Columns for Imputation ---
# Explicitly define columns that contain pollutants and AQI (must be numeric)
numeric_cols = [
    'PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO',
    'SO2', 'O3', 'Benzene', 'Toluene', 'AQI'
]

# --- 3. Impute Numeric Columns (Two Passes) ---

# First Pass: City-Specific Median Imputation
for col in numeric_cols:
    # Use .loc to avoid the SettingWithCopyWarning and ensure assignment works correctly
    df.loc[:, col] = df.groupby('City')[col].transform(lambda x: x.fillna(x.median()))

# Second Pass: Global Median Imputation for remaining NaNs
for col in numeric_cols:
    global_median = df[col].median()
    df.loc[:, col] = df[col].fillna(global_median)

# --- 4. Impute Categorical Column (AQI_Bucket) ---
# Use forward-fill and then backward-fill for day-to-day continuity
# This section is crucial to avoid the TypeError in the median step
df['AQI_Bucket'] = df.groupby('City')['AQI_Bucket'].ffill().bfill()

# --- 5. Final Check and Save ---

# Final check
print("\nFinal missing values check (Total NaN count):")
# Check the sum of missing values across the entire DataFrame
print(df.isnull().sum().sum())

# Save the cleaned DataFrame to a new CSV file
df.to_csv("city_day_cleaned.csv", index=False)
print("\nSuccessfully created 'city_day_cleaned.csv'.")
