import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
import matplotlib.pyplot as plt

# Directory where CSV files are stored
data_dir = "data/"

# Construct the CSV file path
file_path = os.path.join(data_dir, "combined_stock_data_with_features.csv")

try:
    # Load combined data
    combined_data = pd.read_csv(file_path)

    # Scale the data
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(combined_data[['Close', 'SMA_50', 'EMA_20', 'RSI']].dropna())

    # Function to prepare data for LSTM
    def prepare_data(data, n_features):
        X, y = [], []
        for i in range(n_features, len(data)):
            X.append(data[i-n_features:i])
            y.append(data[i, 0])  # Predicting the 'Close' price
        return np.array(X), np.array(y)

    n_features = 60  # Number of past days to consider
    X, y = prepare_data(scaled_data, n_features)

    # Split the data into training and testing sets
    split = int(0.8 * len(X))
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    # Build the LSTM model
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(n_features, X.shape[2])))
    model.add(LSTM(units=50))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X_train, y_train, epochs=25, batch_size=32)

    print("Model trained successfully!")

    # Save the trained model
    model.save('trained_model.h5')
    
    # Load the trained model
    model = load_model('trained_model.h5')

    # Make predictions
    predicted_prices = model.predict(X_test)
    predicted_prices = scaler.inverse_transform(predicted_prices)

    # Compare with actual prices
    actual_prices = scaler.inverse_transform(y_test.reshape(-1, 1))

    # Plot the restults
    plt.figure(figsize=(14, 7))
    plt.plot(actual_prices, color='red', label='Actual Prices')
    plt.plot(predicted_prices, color='blue', label='Predicted Prices')
    plt.title('Stock Price Prediction')
    plt.xlable('Time')
    plt.ylable('Stock Price')
    plt.legend() 
    plt.show()

    print("Prediction completed!")
except FileNotFoundError as e:
    print(f"Error: File '{file_path}' not found. {e}")

except ValueError as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"Error: An unexpected error has occurred: {e}")
