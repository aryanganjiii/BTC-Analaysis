"""
The best and worst days of the week for investing by The least loss
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pd.set_option("display.width", 320)
pd.set_option("display.max_columns", 12)

df = pd.read_csv('BTC-USD.csv')
df['Date'] = df['Date'].values.astype(np.datetime64)
df['day'] = df['Date'].apply(lambda x: x.day)
df['month'] = df['Date'].apply(lambda x: x.month)
df['weekday'] = df['Date'].apply(lambda x: x.isoweekday())
df['benefit'] = df['Close'] - df['Open']
df['tolerance'] = df['High'] - df['Low']
df.set_index('Date', inplace=True)
dfLoss = df[df['benefit'] < 0]
gp_weekday = dfLoss.groupby('weekday').sum()
max_loss = gp_weekday['benefit'].min()
min_loss = gp_weekday['benefit'].max()
print('max loss', gp_weekday[gp_weekday['benefit'] == max_loss].index[0])
print('min loss', gp_weekday[gp_weekday['benefit'] == min_loss].index[0])
gp_weekday['benefit'].plot()
plt.show()

