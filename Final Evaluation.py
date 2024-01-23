import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
data=pd.read_csv('Final Daily Prices.csv')
data1=pd.read_csv('D:\Python Programs!!\Data Mining\Assignment\Final Daily Prices.csv')
print(mean_absolute_error(data1['USD'][:11835],data['USD']))
x=np.arange(11835)
plt.plot(x,data1['USD'][:11835])
plt.legend(['Original Final Daily Prices'])
plt.ylabel('Price of Gold in USD!!')
plt.show()
