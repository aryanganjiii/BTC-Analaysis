import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
X = pd.read_csv("BTC-USD.csv")
y = X["Open"]

x_train = X[:336]
x_test = X[336:]

y_train = y[:336]
y_test = y[336:]

x_train.drop(columns=["Open","Date"],inplace=True)
x_test.drop(columns=["Open","Date"],inplace=True)

axes=np.arange(len(X))

model = LinearRegression()
model.fit(x_train, y_train)

plt.plot(axes[:336], y_train)
plt.plot(axes[336:], y_test)
plt.plot(axes[336:], model.predict(x_test),"g--")


plt.show()



