

'''documentacion https://pandas.pydata.org/docs/reference/frame.html'''
import pandas
import pandas as pd


data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}

purchases = pd.DataFrame(data)

print(purchases)

purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])

print(purchases)

print(purchases.loc['June'])
print(purchases["apples"])
ordenes = pd.read_csv("../Exams/dodic_order_book.csv",index_col=0)
print(ordenes)

'''
.head() outputs the first five rows of your DataFrame by default, but we could also pass a number as well: movies_df.head(10) would output the top ten rows, for example.

To see the last five rows use .tail(). tail() also accepts a number, and in this case we printing the bottom two rows.:'''

print(ordenes.head())
print(ordenes.tail())
ordenes.info()

print(ordenes.shape)

print(ordenes.columns)
newordenes = ordenes.rename(columns={'server_ts':"timestamp"})
print(newordenes.columns)
print(ordenes.columns)
ordenes.rename(columns={'server_ts':"timestamp"},inplace=True)
print(ordenes.columns)


'''
How to work with missing values
When exploring data, you’ll most likely encounter missing or null values, which are essentially placeholders for non-existent values. Most commonly you'll see Python's None or NumPy's np.nan, each of which are handled differently in some situations.

There are two options in dealing with nulls:

Get rid of rows or columns with nulls
Replace nulls with non-null values, a technique known as imputation
Let's calculate to total number of nulls in each column of our dataset. The first step is to check which cells in our DataFrame are null:
'''

print(ordenes.isnull())

print(ordenes['size']*ordenes['price'])
ordenes["letras"] = ordenes['symbol'].str.slice(0,3)
print(ordenes)
print(ordenes['price'].std())

print(ordenes[['price','size']].describe())
print(ordenes[(ordenes['account'] == 1225) | (ordenes['account'] ==1001)])

print(ordenes[(ordenes['account'].isin([1225,1001]))])

print(ordenes.groupby('account').count())
print(ordenes.groupby('account')["price"].sum())
print(ordenes.price.value_counts())

print(ordenes.account.value_counts())

print(ordenes.groupby("account").price.sum())
print(ordenes.groupby("account").price.max())
import matplotlib.pyplot as plt
ordenes.price[(ordenes['price']  >= 18)].plot()

plt.show()

import yfinance

from datetime import date
from datetime import timedelta
day = date.today()-timedelta(days=100)
ggal = yfinance.download(["GGAL","YPF"],start=day)

ggal["Close"].plot()
#ggal.to_excel("ggal.xlsx")
plt.show()