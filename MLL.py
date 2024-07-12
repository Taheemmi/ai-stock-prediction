import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler
# May show as could not be resolved but it works *shrug*
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

# Directory where CSV files are stored
data_dir = "data/"

# Construct the CSV file path
file_path = os.path.join(data_dir, "combined_stock_data_with_features.csv")

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
