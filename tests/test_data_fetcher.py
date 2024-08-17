# This module contains unit tests for the data_fetcher module.

import unittest
from src.data_fetcher import fetch_stock_data
import pandas as pd


class TestDataFetcher(unittest.TestCase):

    def test_fetch_stock_data(self):
        """
        Test the fetch_stock_data function to ensure it returns a DataFrame with expected columns.
        """
        ticker = "TSM"  # TSMC stock ticker
        interval = "1d"  # Daily interval
        start_date = pd.to_datetime('2024-01-01')  # Start date for fetching data
        data = fetch_stock_data(ticker, interval, start_date)  # Fetch the stock data

        # Assert that the returned data is not None
        self.assertIsNotNone(data)

        # Assert that the 'Close' column is present in the returned data
        self.assertIn('Close', data.columns)


if __name__ == '__main__':
    unittest.main()
