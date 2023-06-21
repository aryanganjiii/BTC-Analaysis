"""
Which week had the most volatility?
"""
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

df = df.drop([0, 1])
df.set_index('Date', inplace=True)

df_sp = np.split(df, 52)
highest_of_the_week = []
lowest_of_the_week = []
for i in df_sp:
    highest_of_the_week.append(i['Open'].max())
    lowest_of_the_week.append(i['Open'].min())

highest_of_the_week_ar = np.array(highest_of_the_week)
lowest_of_the_week_ar = np.array(lowest_of_the_week)
tolerence_week = highest_of_the_week_ar - lowest_of_the_week_ar
print(tolerence_week.argmax())
