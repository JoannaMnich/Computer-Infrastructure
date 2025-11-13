#! /usr/bin/env python3

# Dates and times.
import datetime as dt

# Yahoo finance data.
import yfinance as yf

# Get historical data for multiple tickers at once:
tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOGL"]

# Get data:
df=yf.download(tickers,period="5d", interval="1d")

# Current date and time:
now=dt.datetime.now()

filename = "../data/" + dt.datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"
df.to_csv(filename)