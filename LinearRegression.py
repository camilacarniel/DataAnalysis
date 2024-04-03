import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Get the number of data points
times = int(input("How many data points does the exercise have?"))

# Initialize lists to store data points
data_x = []
data_y = []

# Input data points
for point in range(times):
    x, y = map(float, input(f"Enter data point {point + 1} (x y) separating the x and y with a space: ").split())
    data_x.append(x)
    data_y.append(y)

# Convert lists to numpy arrays
data_x = np.array(data_x).reshape(-1, 1)
data_y = np.array(data_y).reshape(-1, 1)

# Perform linear regression
linear_reg = LinearRegression().fit(data_x, data_y)
predicted_y = linear_reg.predict(data_x)

# Plot the graph
plt.scatter(data_x, data_y, color='red')
plt.plot(data_x, predicted_y, color='blue')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Linear Regression')
plt.grid(True)
plt.show()

# Print the equation of the linear regression line
slope = linear_reg.coef_[0][0]
intercept = linear_reg.intercept_[0]
print(f"Equation of the linear regression line: y = {slope:.2f}x + {intercept:.2f}")

# Print the correlation coefficient
correlation = np.corrcoef(data_x.squeeze(), data_y.squeeze())[0][1]
print(f"Correlation between the data: {correlation:.2f}")
