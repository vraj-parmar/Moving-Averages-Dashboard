# **TSMC Stock Analysis Dashboard**

## **Overview**

The TSMC Stock Analysis Dashboard is a web application built using [Streamlit](https://streamlit.io/) and [Plotly](https://plotly.com/). It allows users to visualize Taiwan Semiconductor Manufacturing Company (TSMC) stock data, including its closing prices and various moving averages, such as Simple Moving Average (SMA), Weighted Moving Average (WMA), and Exponential Moving Average (EMA).

## **Features**

- **Interactive Dashboard**: Visualize TSMC stock data with adjustable intervals and starting dates.
- **Moving Averages**: Calculate and plot SMA, WMA, and EMA to analyze stock trends.
- **User Input Parameters**: Customize the analysis using dropdowns and sliders for intervals, start dates, and moving average periods.
- **Plotly Visualisations**: High-quality, interactive charts for better data interpretation.

## **Directory Structure**

```
├── src
│   ├── data_fetcher.py         # Module for fetching stock data using yfinance
│   ├── moving_averages.py      # Module for calculating SMA, WMA, and EMA
├── streamlit_app
│   ├── dashboard.py            # Main Streamlit dashboard application
├── tests
│   ├── test_data_fetcher.py    # Unit tests for the data_fetcher module
│   ├── test_moving_averages.py # Unit tests for the moving_averages module
├── app.py                      # Entry point to run the Streamlit app
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
```

## **Installation**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/Quants-Moving_Averages-Dashboard.git
   cd Quants-Moving_Averages-Dashboard
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install the Required Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## **Running the Application**

To start the Streamlit application, simply run:

```bash
streamlit run app.py
```

This will launch the dashboard in your web browser, where you can interact with the various features.

## **Testing**

Unit tests are provided to ensure the reliability of the data fetching and moving average calculations. To run the tests, use:

```bash
python -m unittest discover -s tests
```

## **Usage**

1. **Select Interval**: Choose the data interval (e.g., 1 day, 15 minutes) from the sidebar.
2. **Select Start Date**: Pick the start date for the data analysis.
3. **Adjust Moving Averages**: Use sliders to set the periods for SMA, WMA, and EMA.
4. **View Results**: The dashboard will display the closing prices along with the chosen moving averages.

## **About**

This dashboard is designed to help traders and analysts understand the behavior of TSMC's stock over time by providing a clear and customisable view of its historical data and trends.
And for me to understand the basics of Quants.