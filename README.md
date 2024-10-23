# Currency Converter Application

This is a simple Currency Converter application built using **Python** and **Tkinter** for the graphical user interface. The application allows users to convert amounts between different currencies by fetching real-time exchange rates from the **ExchangeRate-API**.

## Features

- Convert amounts from one currency to another using real-time exchange rates.
- Displays the converted amount after fetching the exchange rate from the API.
- User-friendly interface built with **Tkinter**.
- Error handling for invalid inputs (e.g., non-numeric amounts, unavailable currencies).
- Displays helpful error messages in case of API failures or invalid currency codes.

## How It Works

1. The user inputs:
   - An amount to convert.
   - A base currency (the currency they want to convert from).
   - A target currency (the currency they want to convert to).

2. The application sends a request to the ExchangeRate-API to fetch the latest exchange rate for the base currency.

3. The conversion rate is used to calculate the equivalent amount in the target currency.

4. The result is displayed on the GUI.

## Requirements

- **Python 3.x** 
- **Tkinter** (comes pre-installed with Python)
- **requests** library (install with `pip install requests`)


