# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Assuming you have a DataFrame with date as the index and 'gold_price' as the target variable
# Load your dataset
# Replace 'your_dataset.csv' with the actual file path or URL to your dataset
df = pd.read_csv('Daily Prices Normalized.csv', parse_dates=['Date'], index_col='Date')

# Feature engineering if needed
# For example, you may want to add lag features or other indicators based on domain knowledge

# Split the data into features (X) and target variable (y)
X = df.drop('USD', axis=1)  # Features
y = df['USD']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build the Lasso regression model
lasso_model = Lasso(alpha=0.1)  # You can adjust the alpha parameter based on cross-validation
lasso_model.fit(X_train_scaled, y_train)

# Evaluate the model
train_score = lasso_model.score(X_train_scaled, y_train)
test_score = lasso_model.score(X_test_scaled, y_test)

print(f'Training R^2 score: {train_score:.2f}')
print(f'Testing R^2 score: {test_score:.2f}')

# Visualize the coefficients
coefficients = pd.Series(lasso_model.coef_, index=X.columns)
plt.figure(figsize=(12, 6))
coefficients.plot(kind='bar')
plt.title('Lasso Regression Coefficients')
plt.show()
