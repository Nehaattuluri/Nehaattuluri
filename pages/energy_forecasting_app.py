import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

# Sample data generation (replace with your actual data loading)
np.random.seed(0)
dates = pd.date_range('2023-01-01', periods=100)
energy_consumption = np.random.randn(100).cumsum() + 100
data = pd.DataFrame({'date': dates, 'energy_consumption': energy_consumption})

# Example: Replace with your actual model training and prediction
train_data = data.iloc[:80]
test_data = data.iloc[80:]
train_rmse = mean_squared_error(train_data['energy_consumption'], np.zeros(len(train_data))) ** 0.5
test_rmse = mean_squared_error(test_data['energy_consumption'], np.zeros(len(test_data))) ** 0.5

# Streamlit app
st.title("Energy Consumption Forecasting")

# Historical Data section
st.write("## Historical Data")
st.line_chart(data.set_index('date')['energy_consumption'])

# Model Performance section
st.write("## Model Performance")
st.write(f"Train RMSE: {train_rmse:.2f}")
st.write(f"Test RMSE: {test_rmse:.2f}")

# Future Energy Consumption Forecast section (example plot)
future_dates = pd.date_range('2023-05-01', periods=10)
future_predictions = np.random.randn(10) + 100  # Replace with your actual future predictions
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(data['date'], data['energy_consumption'], label='Historical Data')
ax.plot(future_dates, future_predictions, label='Predicted Energy Consumption', linestyle='--')
ax.set_xlabel('Date')
ax.set_ylabel('Energy Consumption')
ax.set_title('Energy Consumption Forecast')
ax.legend()

# Display the plot using Streamlit
st.write("## Future Energy Consumption Forecast")
st.pyplot(fig)
