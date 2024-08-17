# This module contains unit tests for the moving_averages module.

import unittest
import pandas as pd
from src.moving_averages import SMA, WMA, EMA


class TestMovingAverages(unittest.TestCase):

    def setUp(self):
        """
        Setup method to create a sample data series for testing.
        """
        self.data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_SMA(self):
        """
        Test the SMA function to ensure it calculates the correct Simple Moving Average.
        """
        result = SMA(self.data, 3)
        self.assertAlmostEqual(result.iloc[-1], 9.0, places=4)

    def test_WMA(self):
        """
        Test the WMA function to ensure it calculates the correct Weighted Moving Average.
        """
        result = WMA(self.data, 3)
        expected_wma = (8 * 1 + 9 * 2 + 10 * 3) / (1 + 2 + 3)
        self.assertAlmostEqual(result.iloc[-1], expected_wma, places=4)

    def test_EMA(self):
        """
        Test the EMA function to ensure it calculates the correct Exponential Moving Average.
        """
        result = EMA(self.data, 3)
        expected_ema = 9.001953125  # Based on previous results
        self.assertAlmostEqual(result.iloc[-1], expected_ema, places=4)


if __name__ == '__main__':
    unittest.main()
