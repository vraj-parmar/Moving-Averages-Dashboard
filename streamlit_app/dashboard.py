# This module defines the Streamlit dashboard for visualizing TSMC stock data.
# It imports data fetching and moving average calculation functions from the src directory.

import streamlit as st
import plotly.graph_objects as go
from src.data_fetcher import fetch_stock_data
from src.moving_averages import SMA, WMA, EMA
import pandas as pd


def run_dashboard():
    """
    Run the Streamlit dashboard for TSMC stock analysis.
    The dashboard allows users to visualize stock prices and moving averages.
    """
    # Set the layout of the Streamlit app to wide
    st.set_page_config(layout="wide")

    # Set the title of the dashboard
    st.title("TSMC Stock Analysis Dashboard")

    # Sidebar for user input parameters
    st.sidebar.header("User Input Parameters")

    # Dropdown for selecting the interval
    interval = st.sidebar.selectbox(
        "Select Interval",
        ["1m", "5m", "15m", "30m", "60m", "1d"],
        index=2  # Default to 15m
    )

    # Date input for selecting the start date
    start_date = st.sidebar.date_input("Start Date", pd.to_datetime('2024-01-01'))

    # Define the ticker symbol for TSMC
    ticker = "TSM"

    # Fetch the stock data using the selected interval and start date
    stock_data = fetch_stock_data(ticker, interval, start_date)

    # Display the stock data in a table
    st.write(f"### {ticker} Stock Data ({interval} intervals)")
    st.dataframe(stock_data.tail())

    # Plot the closing price of the stock
    st.write("### Closing Price")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='Close'))
    st.plotly_chart(fig)

    # Sidebar slider to select the SMA period
    sma_period = st.sidebar.slider("SMA Period", 1, 50, 20)
    # Calculate the SMA and add it to the stock data
    stock_data['SMA'] = SMA(stock_data['Close'], sma_period)

    # Plot the closing price and SMA
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='Close'))
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['SMA'], mode='lines', name=f'SMA ({sma_period})'))
    st.write(f"### {sma_period}-minute Simple Moving Average (SMA)")
    st.plotly_chart(fig)

    # Sidebar slider to select the WMA period
    wma_period = st.sidebar.slider("WMA Period", 1, 50, 20)
    # Calculate the WMA and add it to the stock data
    stock_data['WMA'] = WMA(stock_data['Close'], wma_period)

    # Plot the closing price and WMA
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='Close'))
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['WMA'], mode='lines', name=f'WMA ({wma_period})'))
    st.write(f"### {wma_period}-minute Weighted Moving Average (WMA)")
    st.plotly_chart(fig)

    # Sidebar slider to select the EMA period
    ema_period = st.sidebar.slider("EMA Period", 1, 50, 20)
    # Calculate the EMA and add it to the stock data
    stock_data['EMA'] = EMA(stock_data['Close'], ema_period)

    # Plot the closing price and EMA
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='Close'))
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['EMA'], mode='lines', name=f'EMA ({ema_period})'))
    st.write(f"### {ema_period}-minute Exponential Moving Average (EMA)")
    st.plotly_chart(fig)

    # Plot the closing price, SMA, WMA, and EMA together
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='Close'))
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['SMA'], mode='lines', name=f'SMA ({sma_period})'))
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['WMA'], mode='lines', name=f'WMA ({wma_period})'))
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['EMA'], mode='lines', name=f'EMA ({ema_period})'))
    st.write("### SMA, WMA, and EMA Combined")
    st.plotly_chart(fig)

    # Sidebar information about the app
    st.sidebar.write("""
    ## About
    This dashboard allows you to visualize TSMC's stock price with various intervals along with three types of moving averages:
    - **Simple Moving Average (SMA)**
    - **Weighted Moving Average (WMA)**
    - **Exponential Moving Average (EMA)**
    """)

