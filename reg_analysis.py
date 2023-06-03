import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data
X = np.array([1, 2, 3, 4, 5]).reshape((-1, 1))  # Explanatory variable
y = np.array([100, 150, 200, 250, 300])  # Dependent variable

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Print the slope and intercept of the regression line
print("Intercept:", model.intercept_)
print("Slope:", model.coef_[0])

# Make predictions
new_X = np.array([6, 7]).reshape((-1, 1))
predicted_y = model.predict(new_X)
print("Predicted sale prices:", predicted_y)