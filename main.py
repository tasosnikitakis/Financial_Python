#packages install
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
yf.pdr_override()
import matplotlib.pyplot as plt


# We can get data by our choice by giving days bracket
today = date.today()
start_date = "2017-01-01"
end_date = "2019–11–30"

#data = pdr.get_data_yahoo("AAPL", start="2020-01-01", end=today)


#tickers = ["MSFT", "PG", "U", "AAPL"]
#new_data = pd.DataFrame()
#for t in tickers:
#    new_data[t] = pdr.get_data_yahoo(t, start="2020-01-01", end=today)["Adj Close"]




#rate of return
pg = pdr.get_data_yahoo("U", start="2022-01-01", end=today)
print(pg.head())

#simple rate of return calculation
# the formula is P1/P0 - 1 this calculates the daily simple rate of return of all the data in the 'adj close' column
# P1 = pg["Adj Close"]
# P1 = pg["Adj Close"].shift(1). The shift function with a lag of 1 returns the adjusted closing price of the previous
# trading day.
pg["simple return"] = pg["Adj Close"]/pg["Adj Close"].shift(1) - 1
print(pg["simple return"])
# this is the column of the simple return daily prices
pg["simple return"].plot(figsize=(8, 5))
#plt.show()
# We use the plot function of the pyplot module from matplotlib to plot a graph and show it with the plt.show() function


average_returns_d = pg["simple return"].mean()
print(average_returns_d)
average_returns_a = pg["simple return"].mean() * 250
print(str(round(average_returns_a, 3) * 100) + "%")

# logarithmic rate of return calculation
pg["log return"] = np.log(pg["Adj Close"]/pg["Adj Close"].shift(1))
print(pg["log return"])
log_return_d = pg["log return"].mean()
log_return_a = pg["log return"].mean() * 250
print(log_return_a)
print(log_return_d)

#portfolio rate of return calculation
tickers = ["U", "MSFT", "ADBE", "DDOG", "MMM", "CFG", "AMZN", "SBSW", "CRSP", "PBA", "ABNB", "WFC", "NIO"]
mydata = pd.DataFrame()
for t in tickers:
    mydata[t] = pdr.get_data_yahoo(t, start="2020-01-01", end=today)["Adj Close"]
print(mydata.info())
print(mydata.tail())
print(mydata.head())
#normalization to 100
print(mydata.iloc[0])
(mydata/mydata.iloc[0] * 100).plot(figsize = (15, 6))
plt.show()

returns = (mydata/mydata.shift(1)) - 1
print(returns.head())
weights = np.array([23.68, 13.29, 12.87, 10.34, 6.92, 6.63, 5.8, 5.75, 3.94, 3.72, 3.36, 2.75, 0.95])
#anual returns calculation
annual_returns = returns.mean() * 250
print(annual_returns)
dot_calculation = np.dot(annual_returns, weights)
portfolio_rate_of_return = str(round(dot_calculation, 5) * 100) + "%"
print(portfolio_rate_of_return)


#market indexes
