import pandas as pd
import numpy as np
# pip3 install scikit-learn
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
# conda create -n vencoverenv python=3.4 numpy scipy scikit-learn tensorflow

# Load datasets
customers = pd.read_csv('carinsurance/Untitled spreadsheet - data inputs.csv')
claims = pd.read_csv('claims.csv')

# Merge data on Customer ID
data = pd.merge(customers, claims[['Customer ID', 'claim-cost', 'claim-date', 'policy-age']], on='Customer ID')

# Feature engineering
data['claim-year'] = pd.to_datetime(data['claim-date']).dt.year
data['claim-month'] = pd.to_datetime(data['claim-date']).dt.month
data['claim-day'] = pd.to_datetime(data['claim-date']).dt.day
data.drop(columns=['claim-date', 'Customer ID'], inplace=True)

# One-hot encode categorical columns
categorical_cols = ['Gender', 'Vehicle Type', 'ICE or EV', 'Location']
data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)

# Normalize numerical features
num_cols = ['Age', 'Employment (Years)', 'Accidents (Last 5 Years)', 'Vehicle Age (Years)', 'Annual Mileage']
scaler = StandardScaler()
data[num_cols] = scaler.fit_transform(data[num_cols])

# Define input and output
X = data.drop(columns=['claim-cost', 'policy-age', 'claim-year', 'claim-month', 'claim-day'])
y = data[['claim-cost', 'policy-age', 'claim-year', 'claim-month', 'claim-day']]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build neural network model
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(32, activation='relu'),
    layers.Dense(5)  # 5 output values: claim-cost, policy-age, year, month, day
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Train the model
model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))

# Evaluate the model
loss, mae = model.evaluate(X_test, y_test)
print("Mean Absolute Error:", mae)

# Save the model
model.save('insurance_claims_model.h5')