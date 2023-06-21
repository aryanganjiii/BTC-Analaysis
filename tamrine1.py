"""
The month with the most profit and loss
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
gp_month = df.groupby('month').sum()

maxProfitMonth = gp_month[gp_month['benefit'] > 0]['benefit'].max()
maxLossMonth = gp_month[gp_month['benefit'] < 0]['benefit'].min()
print('max profit month=', gp_month[gp_month['benefit'] == maxProfitMonth].index[0])
print('max loss month=', gp_month[gp_month['benefit'] == maxLossMonth].index[0])
gp_month['benefit'].plot()
plt.show()
