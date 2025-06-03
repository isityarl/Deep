# ARIMA vs. LSTM for USD Exchange Rate Forecasting

## Overview

This project aims to forecast the USD exchange rate using two different time series modeling techniques:
1.  **ARIMA (Autoregressive Integrated Moving Average):**
2.  **LSTM (Long Short-Term Memory):**

The notebook loads historical USD exchange rate data, preprocesses it, applies both ARIMA and LSTM models, and visualizes their forecasts. The goal is to compare the forecasting capabilities of these two approaches on the given dataset.

## Data Source

* **`data.csv`**:
    * **Relevant Columns Used:**
        * `Date`: The date of the exchange rate record (expected in `dd.mm.yyyy` format).
        * `USD`: The USD exchange rate value (numerical).


## Workflow

* **Data Preprocessing:** Includes date conversion, indexing, differencing (for ARIMA), scaling, and sequence creation (for LSTM).
* **Stationarity Testing:** The ADF test is used to ensure the time series is suitable for ARIMA.
* **ARIMA Model:**
    * Identifies model order (p,d,q) using ACF/PACF plots (though a simple (0,0,0) is used on differenced data in the current snippet).
    * Fits the model and generates point forecasts.
* **LSTM Model:**
    * Uses a lookback window to create input sequences (X) and target values (y).
    * Employs an LSTM architecture with multiple layers and a final linear layer for regression.
    * Trains using Mean Squared Error (MSE) loss.
* **Forecasting & Visualization:** Both models produce forecasts which are then plotted against the actual test data for visual comparison.
