# Make predictions
predicted_prices = model.predict(X_test)
predicted_prices = scaler.inverse_transform(predicted_prices)

# Compare with actual prices
actual_prices = scaler.inverse_transform(y_test.reshape(-1, 1))

# Plot the results (example)
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 7))
plt.plot(actual_prices, color='red', label='Actual Prices')
plt.plot(predicted_prices, color='blue', label='Predicted Prices')
plt.title('Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()
plt.show()

print("Prediction completed!")