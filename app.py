import requests
import tkinter as tk
from tkinter import ttk, messagebox

# API key and URL
API_KEY = "009b980a5619331aa9536f25"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

# Function to fetch the exchange rate
def get_exchange_rate(base_currency, target_currency):
    try:
        response = requests.get(BASE_URL + base_currency)
        data = response.json()

        if response.status_code != 200:
            messagebox.showerror("Error", f"API Error: {data['error-type']}")
            return None

        rate = data["conversion_rates"].get(target_currency)
        if rate is None:
            messagebox.showerror("Error", f"Currency {target_currency} is not available.")
            return None

        return rate
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching exchange rate: {e}")
        return None

# Function to perform conversion
def convert_currency():
    amount = amount_entry.get()
    base_currency = base_currency_entry.get().upper()
    target_currency = target_currency_entry.get().upper()

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid amount.")
        return

    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        converted_amount = amount * rate
        result_label.config(text=f"{amount:.2f} {base_currency} = {converted_amount:.2f} {target_currency}")

# Tkinter setup
root = tk.Tk()
root.title("Currency Converter")

# Create widgets
amount_label = ttk.Label(root, text="Amount:")
amount_label.grid(row=0, column=0, padx=10, pady=10)

amount_entry = ttk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

base_currency_label = ttk.Label(root, text="Base Currency (e.g., USD):")
base_currency_label.grid(row=1, column=0, padx=10, pady=10)

base_currency_entry = ttk.Entry(root)
base_currency_entry.grid(row=1, column=1, padx=10, pady=10)

target_currency_label = ttk.Label(root, text="Target Currency (e.g., EUR):")
target_currency_label.grid(row=2, column=0, padx=10, pady=10)

target_currency_entry = ttk.Entry(root)
target_currency_entry.grid(row=2, column=1, padx=10, pady=10)

convert_button = ttk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()
