"""
alex has 1000$
if alex buys btc for every wednesday and sells it every saturday in the same week,how much does alex have
after a year ?
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

dfW3 = df[df['weekday'] == 3]['Open']
dfW6 = df[df['weekday'] == 6]['Close']
dfW3 = dfW3.reset_index(drop=True)
dfW6 = dfW6.reset_index(drop=True)
benefit = dfW6 - dfW3
print(benefit)
print('__________-')
money = 1000
money_list=[money]
for i in range(len(benefit)):
    money += benefit[i]
    money_list.append(money)
    print(money)
plt.plot(money_list)
plt.show()