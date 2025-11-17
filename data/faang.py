#! /usr/bin/env python3

# Dates and time
import datetime as dt

#Yahoo Finance data
import yfinance as yf

# Get data
df=yf.download(["META", "AAPL", "AMZN", "NFLX", "GOOGL"], period="5d", interval="1h")

# Current data and time
now=dt.datetime.now()

# File name
filename="data/" + now.strftime("%Y%m%d-%H%M%S") + ".csv"

# Save data as CSV file
df.to_csv(filename)