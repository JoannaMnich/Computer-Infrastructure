#! C:/Users/jmnic/anaconda3/python.exe

import os
from datetime import datetime
import yfinance as yf
import matplotlib.pyplot as plt

def download_faang_data():
    tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOGL"]

    df = yf.download(tickers, period="5d", interval="1h")

    # Ensure data folder exists
    os.makedirs("data", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"data/{timestamp}.csv"

    df.to_csv(filename)

    print(f"Saved data to: {filename}")
    return df, timestamp


def plot_faang(df, timestamp):
    # Ensure plots folder exists
    os.makedirs("plots", exist_ok=True)

    close_cols = [col for col in df.columns if "Close" in col]
    tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOGL"]

    # Create plot
    plt.figure(figsize=(12, 6))

    for col, ticker in zip(close_cols, tickers):
        plt.plot(df.index, df[col], label=ticker)

    plt.title(f"Closing Prices - {timestamp[:8]}")
    plt.xlabel("Date")
    plt.ylabel("Close Price ($)")
    plt.legend()
    plt.tight_layout()

    plot_filename = f"plots/{timestamp}.png"
    plt.savefig(plot_filename)

    print(f"Saved plot to: {plot_filename}")


if __name__ == "__main__":
    df, timestamp = download_faang_data()
    plot_faang(df, timestamp)
    plt.show()