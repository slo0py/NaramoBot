import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV data
df = pd.read_csv('trainingdata.csv')

# Clean data: remove rows with missing or non-numeric values
df = df.dropna()
df = df[pd.to_numeric(df['Heat'], errors='coerce').notnull()]
df = df[pd.to_numeric(df['Excess'], errors='coerce').notnull()]

# Convert to integers
df['Heat'] = df['Heat'].astype(int)
df['Excess'] = df['Excess'].astype(int)

x = df['Heat']
y = df['Excess']

# Calculate linear regression coefficients
slope, intercept = np.polyfit(x, y, 1)
trendline = slope * x + intercept


# Start plot
plt.figure(figsize=(8,6))
plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, trendline, color='red', label=f'Trendline: y = {slope:.2f}x + {intercept:.2f}')
plt.title('Heat vs Excess with Linear Regression Trendline')
plt.xlabel('Heat')
plt.ylabel('Excess')
plt.grid(True)
plt.legend()

# Auto-zoom with 10% margin
x_margin = (x.max() - x.min()) * 0.1
y_margin = (y.max() - y.min()) * 0.1
plt.xlim(x.min() - x_margin, x.max() + x_margin)
plt.ylim(y.min() - y_margin, y.max() + y_margin)


plt.show()
