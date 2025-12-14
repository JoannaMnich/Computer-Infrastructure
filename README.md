# FAANG Stock Data Downloader and Plotter

This repository contains a Python script that downloads recent stock price data for the FAANG companies (Facebook/Meta, Apple, Amazon, Netflix, and Google) and generates plots of their closing prices.

The script uses **Yahoo Finance** data via the `yfinance` library and saves both CSV data files and PNG plots locally.

## Features

- Download the last 5 days of stock data at 1-hour intervals for FAANG companies.
- Save the downloaded data as a timestamped CSV file in the `data` folder.
- Generate a line plot of closing prices for all FAANG companies and save it as a PNG file in the `plots` folder.
- Simple, PEP8-compliant Python code for easy customization.

## Requirements

- Python 3.8+
- Libraries:
  - `yfinance`
  - `matplotlib`
  - `pandas` (installed automatically with `yfinance`)

Install the required libraries using:

```bash
pip install yfinance matplotlib pandas

- Usage

Clone this repository:

git clone https://github.com/yourusername/faang-stock-data.git
cd faang-stock-data


Run the script:

python faang.py


The script will:

Download the latest FAANG stock data.

Save it as a CSV file in the data folder.

Generate a line plot of closing prices and save it in the plots folder.

Display the plot using matplotlib.

- Folder Structure
faang-stock-data/
│
├── data/       # Saved CSV files of stock data
├── plots/      # Saved PNG plots
├── faang.py    # Main script
└── README.md   # Project documentation

- Customization

To add or remove tickers, edit the tickers list in faang.py:

tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOGL"]


Change the time period or interval by modifying the yf.download parameters:

df = yf.download(tickers, period="5d", interval="1h")


