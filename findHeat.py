import pandas as pd
import numpy as np
import math

# Load and clean data
file_path = 'trainingdata.csv'
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: '{file_path}' not found.")
    exit()

# Drop rows with missing data or non-numeric values
df = df.dropna()
df = df[pd.to_numeric(df['Heat'], errors='coerce').notnull()]
df = df[pd.to_numeric(df['Excess'], errors='coerce').notnull()]
df['Heat'] = df['Heat'].astype(int)
df['Excess'] = df['Excess'].astype(int)

# Fit a linear model (Excess = slope * Heat + intercept)
x = df['Heat']
y = df['Excess']
slope, intercept = np.polyfit(x, y, 1)

# Heat MOE calculation
x_heat = df['Heat'].values
y_excess = df['Excess'].values
a, b = np.polyfit(x_heat, y_excess, 1)

# Take user input
try:
    target_excess = float(input("Enter desired Excess value: "))
except ValueError:
    print("Invalid input. Please enter a numeric Excess value.")
    exit()

# Estimate the corresponding Heat

estimated_heat = (target_excess - intercept) / slope
rounded_heat = math.ceil(estimated_heat)
target_excess = math.ceil(target_excess)
delta_excess = 1000 # rough assumed excess fluctuations. update later

delta_heat = delta_excess / abs(a)
print(f"Estimated Heat for Excess {target_excess} is approximately {rounded_heat} K. (±{math.ceil(delta_heat)}K)")
