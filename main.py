#packages install
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
pg = pdr.get_data_yahoo("PG", start="2020-01-01", end=today)
print(pg.head())

pg["simple return"] = pg["Adj Close"]/pg["Adj Close"].shift(1) - 1
print(pg["simple return"])
pg["simple return"].plot(figsize=(8, 5))
plt.show()
