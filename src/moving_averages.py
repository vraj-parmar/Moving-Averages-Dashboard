# This module contains functions to calculate different types of moving averages.

import numpy as np

def SMA(series, period):
    """
    Calculate the Simple Moving Average (SMA).

    Parameters:
    - series: The data series to calculate the SMA on.
    - period: The number of periods over which to calculate the SMA.

    Returns:
    - A series representing the SMA.
    """
    return series.rolling(window=period).mean()

def WMA(series, period):
    """
    Calculate the Weighted Moving Average (WMA).

    Parameters:
    - series: The data series to calculate the WMA on.
    - period: The number of periods over which to calculate the WMA.

    Returns:
    - A series representing the WMA.
    """
    weights = np.arange(1, period + 1)
    return series.rolling(period).apply(lambda prices: np.dot(prices, weights)/weights.sum(), raw=True)

def EMA(series, period):
    """
    Calculate the Exponential Moving Average (EMA).

    Parameters:
    - series: The data series to calculate the EMA on.
    - period: The number of periods over which to calculate the EMA.

    Returns:
    - A series representing the EMA.
    """
    return series.ewm(span=period, adjust=False).mean()
