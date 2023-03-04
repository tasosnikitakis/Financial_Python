#imports
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
from yahoo_fin import stock_info as si
yf.pdr_override()
import matplotlib.pyplot as plt
plt.style.use("dark_background")

class Portfolio:
    def __init__(self):
        self.name = ""
        self.tickers = []
        self.portfolio_data = pd.DataFrame(columns=['Ticker', 'Units', 'Avg. Price'])

    def add_stock(self, ticker, units, avg_price):
        new_row = {'Ticker': ticker, 'Units': units, 'Avg. Price': avg_price}
        self.portfolio_data = pd.concat([self.portfolio_data, pd.DataFrame([new_row])], ignore_index=True)

    def add_stock_interactive(self):
        """Method to add a stock to the portfolio interactively"""

        # Ask the user to input the stock data
        while True:
            ticker = input("Enter the stock ticker (or type 'off' to finish): ")
            if ticker.lower() == 'off':
                break

            units = int(input("Enter the number of units: "))
            avg_price = float(input("Enter the average price: "))

            # Create a new row for the portfolio_data dataframe with the stock information
            new_row = {'Ticker': ticker, 'Units': units, 'Avg. Price': avg_price}

            # Add the new row to the portfolio_data dataframe
            self.portfolio_data = pd.concat([self.portfolio_data, pd.DataFrame([new_row])], ignore_index=True)

    def total_invested(self):
        """Method to calculate the total amount invested in the portfolio"""

        # Multiply the number of units by the average price for each stock, and sum the results
        total_invested = round(sum(self.portfolio_data['Units'] * self.portfolio_data['Avg. Price']), 2)

        return total_invested

    def pie_chart(self):
        """Method to create a pie chart of the portfolio holdings"""

        # Calculate the total portfolio value
        total_value = self.total_invested()

        # Calculate the percentage of each stock in the portfolio by value
        percentages = (self.portfolio_data['Units'] * self.portfolio_data['Avg. Price']) / total_value

        # Create a dictionary with the ticker symbols as keys and the percentages as values
        data = dict(zip(self.portfolio_data['Ticker'], percentages))

        # Create a pie chart with the data
        fig, ax = plt.subplots()
        ax.pie(data.values(), labels=data.keys(), autopct='%1.1f%%', shadow=False)
        ax.axis('equal')
        ax.set_title('Portfolio Holdings - Pie Chart')


        # Show the chart
        plt.show()


    def current_value(self):
        """Method to calculate the current value of the portfolio based on the current stock prices"""

        # Create a list of ticker symbols for the stocks in the portfolio
        tickers = self.portfolio_data['Ticker'].tolist()

        # Use yfinance to get the current stock prices for the tickers

        prices = si.get_live_price(tickers)

        # Calculate the current value of each stock based on the number of units and the current price
        stock_values = self.portfolio_data['Units'] * prices

        # Calculate the total current value of the portfolio
        total_value = stock_values.sum()

        return total_value
