import pandas as pd
import os

# Directory where CSV files are stored
data_dir = "data/"

# List of tickers
tickers = [
    "AAPL", "MSFT", "NVDA", "AMD", "INTC", "GOOGL", "FB", "TSLA", "AMZN", "NFLX",
    "ATVI", "TTWO", "EA", "UBSFY", "TCEHY", "NTDOY", "SNE", "TWTR", "SNAP", "CRM",
    "PYPL", "ROKU", "SQ", "SHOP", "NET", "DOCU", "OKTA", "FSLY", "ZM", "CRWD", "PD",
    "UPWK", "U", "TWLO", "MDB", "DATA", "DDOG", "ZS", "SEDG", "ENPH", "TTD", "PINS",
    "MELI", "LULU", "SPOT", "DKNG", "BILI"
]

combined_data = pd.DataFrame()

# Load data for each ticker
for ticker in tickers:
    try:
        # Construct the CSV file path
        file_path = os.path.join(data_dir, f"{ticker}_historical.csv")

        # Read the data from the CSV into a temporary DataFrame
        data = pd.read_csv(file_path)

        # Clean the data 
        data = data.dropna()
        data['Date'] = pd.to_datetime(data['Date'])

        data.columns = data.columns.str.replace(r'[^\w\s]+', '')

        # Convert numerical columns to appropriate data types
        numeric_columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        for column in numeric_columns:
            data[column] = data[column].astype(float)

        # Add a 'Ticker' column to identify which stock the data belings to
        data['Ticker'] = ticker

        combined_data = pd.concat([combined_data, data], ignore_index=True)

        print(f"Data loaded successfully for {ticker}")

    except FileNotFoundError:
        print(f"Error: file '{file_path}' not found. Skipping {ticker}")

    except Exception as e:
        print(f"Error loading data for {ticker}: {str(e)}")


# Save the combined and cleaned data to a CSV file
combined_data.to_csv("combined_stock_data.csv", index=False)

# Display the combined and cleaned data
print("\nCombined and cleaned data:")
print(combined_data.head())
print("\nShape of combined data: {combined_data.shape}")

   