#imports
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
from datetime import date
from Portfolio import Portfolio
import yfinance as yf
from yahoo_fin import stock_info as si
yf.pdr_override()
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
plt.style.use("dark_background")

my_portfolio = Portfolio()
my_portfolio.add_stock('META', 10, 132.64)
my_portfolio.add_stock('AMZN', 90, 123.0)
my_portfolio.add_stock('NFLX', 3, 150.0)
my_portfolio.add_stock('GOOG', 50, 200.0)

# Calculate the current value of the portfolio
stock = "AAPL"
amount = 20
price = si.get_live_price(stock)
print(round(price, 2))

