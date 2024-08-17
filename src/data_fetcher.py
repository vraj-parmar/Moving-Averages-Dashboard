# This module is responsible for fetching stock data using the yfinance library.

import yfinance as yf

def fetch_stock_data(ticker, interval, start_date):
    """
    Fetch stock data from Yahoo Finance.

    Parameters:
    - ticker: The stock symbol for the company (e.g., "TSM").
    - interval: The interval of the data (e.g., "1d", "15m").
    - start_date: The start date for fetching the data.

    Returns:
    - A DataFrame containing the stock data.
    """
    return yf.download(ticker, interval=interval, start=start_date)
