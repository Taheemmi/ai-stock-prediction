import pandas as pd
import os

# Directory where CSV files are stored
data_dir = "data/"

# Construct the CSV file path
file_path = os.path.join(data_dir, "combined_stock_data.csv")

# Load combined data
combined_data = pd.read_csv(file_path)

# Ensure 'Date' column is datetime type
combined_data['Date'] = pd.to_datetime(combined_data['Date'])


def create_sma(data, window):
    data[f'SMA_{window}'] = data['Close'].rolling(window=window).mean()
    return data


def create_ema(data, span):
    data[f'EMA_{span}'] = data['Close'].ewm(span=span, adjust=False).mean()
    return data


def create_rsi(data, window):
    delta = data['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data


# Apply feature engineering functions
combined_data = create_sma(combined_data, window=50)
combined_data = create_ema(combined_data, span=20)
combined_data = create_rsi(combined_data, window=14)

# Display the updated dataset with new features
print("Updated dataset with features:")
print(combined_data.head())

# Save the updated dataset to a CSV file 
combined_data.to_csv("combined_stock_data_with_features.csv", index=False)

print("\nFeature engineering completed and data saved!")