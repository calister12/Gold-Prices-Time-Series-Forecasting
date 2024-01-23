#importing all the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score

#reading our csv file and printing the head of our preprocessed and
#normalized data
data=pd.read_csv('Daily Prices Normalized.csv')
# print(data.head())

x = np.arange(len(data))
y = np.array(data['INR'])

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

degrees = np.arange(1, 20)  # You can adjust the range of degrees

mse_values = []
r2_values=[]
for degree in degrees:
    # Transform the features to polynomial features
    poly = PolynomialFeatures(degree=degree)
    x_poly_train = poly.fit_transform(x_train.reshape(-1, 1))

    # Fit a linear regression model
    model = LinearRegression()
    model.fit(x_poly_train, y_train)

    # Make predictions on the test set
    x_poly_test = poly.transform(x_test.reshape(-1, 1))
    y_pred = model.predict(x_poly_test)

    # Calculate Mean Squared Error
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    mse_values.append(mse)
    r2_values.append(r2)
    print("MSE for Degree",degree,":",round(mse,4))
    print("R2 for Degree",degree,":",round(r2,4)*100,'\n')

# Find the degree with the minimum MSE
best_degree = degrees[np.argmax(r2_values)]
plt.bar(degrees,mse_values)
plt.xlabel('Degrees')
plt.ylabel('MSE')
plt.xticks(degrees)
plt.show()
poly = PolynomialFeatures(degree=best_degree)
x_poly_train = poly.fit_transform(x_train.reshape(-1, 1))

    # Fit a linear regression model
model = LinearRegression()
model.fit(x_poly_train, y_train)
# Make predictions on the test set
x_poly_test = poly.transform(x_test.reshape(-1, 1))
y_pred = model.predict(x_poly_test)

# Calculate Mean Squared Error
r2 = r2_score(y_test, y_pred)
print("R2 Score of Polynomial regression model with degree 15 : ",round(r2,5)*100)
print("mse of Polynomial regression model with degree 15 : ",round(mean_squared_error(y_test,y_pred),4))

# Plot the original data and the best-fitting curve

x_next_year=np.arange(11731,12906)
x_next_year_poly=poly.fit_transform(x_next_year.reshape(-1, 1))
y_fit_next_year = model.predict(x_next_year_poly)

# Assuming mean and std_dev are the mean and standard deviation used during normalization
mean_price = 754.3
std_dev_price = 529.5

# Convert normalized values back to original scale
y_fit_next_year_original = (y_fit_next_year * std_dev_price) + mean_price

# Print the original values

plt.plot(x, y, label='Original Data')
plt.plot(x_next_year_poly, y_fit_next_year, label=f'Best Fit (Degree {best_degree})', color='red')
plt.legend()
#plt.show()
