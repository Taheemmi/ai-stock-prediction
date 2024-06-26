import yfinance as yf
import pandas as pd

# Define the stocks and the time period
tickers = [
    "AAPL", "MSFT", "NVDA", "AMD", "INTC", "GOOGL", "FB", "TSLA", "AMZN", "NFLX",
    "ATVI", "TTWO", "EA", "UBSFY", "TCEHY", "NTDOY", "SNE", "NVDA", "AMD", "INTC",
    "TWTR", "SNAP", "CRM", "PYPL", "ROKU", "SQ", "SHOP", "NET", "DOCU", "OKTA",
    "FSLY", "ZM", "CRWD", "PD", "UPWK", "U", "TWLO", "MDB", "DATA", "DDOG", "ZS",
    "SEDG", "ENPH", "TTD", "PINS", "MELI", "LULU", "SPOT", "DKNG", "U", "BILI"
]



for ticker in tickers:
    # download historical data
    data = yf.download(ticker, start="2023-04-01", end="2024-04-01")
    
    # Save to a CSV file with ticker name
    data.to_csv(f"{ticker}_historical.csv")
    print(f"Data for {ticker} scraped successfully!")

print("All data scraped successfully!")


