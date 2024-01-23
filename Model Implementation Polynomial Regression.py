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
import datetime
#reading our csv file and printing the head of our preprocessed and 
#normalized data
data=pd.read_csv('Daily Prices Normalized.csv')

#Extracting date from the database:
date=[]
for i in data['Date']:
    i=i.replace("-","/")
    date.append(i)


# Assuming mean and std_dev are the mean and standard deviation used during normalization
mean_price = 754.3
std_dev_price = 529.5
#Extracting USD from the database:
final=[]
for i in data['USD']:
    final_price=(i*std_dev_price)+mean_price
    final.append(round(final_price,5))

x = np.arange(len(data))
y = np.array(data['USD'])

def modelCall(x,y):
    # Split the data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    # Transform the features to polynomial features
    poly = PolynomialFeatures(degree=6)
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

    # Plot the original data and the best-fitting curve

    x_next_year=np.arange(11731, 12096)
    x_next_year_poly=poly.fit_transform(x_next_year.reshape(-1, 1))
    y_fit_next_year = model.predict(x_next_year_poly)

 
    # Convert normalized values back to original scale
    y_fit_next_year_original = (y_fit_next_year * std_dev_price) + mean_price

    # Print the original values
    return (y_fit_next_year_original)
next1=modelCall(x,y)

start_date = datetime.date(2022, 12, 16)
end_date = datetime.date(2023, 12, 15)
while start_date <= end_date:
    formatted_date = start_date.strftime("%d/%m/%Y")
    date.append(str(formatted_date))
    start_date += datetime.timedelta(days=1)  # Increment start date by one day

final.extend(next1)
#Creating the final Database:
data={
    'Date':date,
    'USD':final
    }
df=pd.DataFrame(data)
df.to_csv('Final Daily Prices.csv',index=False)
print("You can check the final output file in Final Daily Prices.csv!!")
