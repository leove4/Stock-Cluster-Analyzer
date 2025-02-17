import tkinter as tk
from tkinter import ttk, messagebox
import yfinance as yf
import pandas as pd
import riskfolio as rp
import matplotlib.pyplot as plt

def analyze():
    # Get input values from the UI
    stocks_input = entry_stocks.get()
    start_date = entry_start.get()
    end_date = entry_end.get()
    
    if not stocks_input:
        messagebox.showerror("Input Error", "Please enter at least one stock symbol.")
        return
    stocks = [s.strip() for s in stocks_input.split(",") if s.strip()]
    
    # Validate dates
    try:
        pd.to_datetime(start_date)
        pd.to_datetime(end_date)
    except Exception:
        messagebox.showerror("Date Error", "Please enter valid dates in YYYY-MM-DD format.")
        return

    # Download stock data
    try:
        data = yf.download(stocks, start=start_date, end=end_date)
    except Exception as e:
        messagebox.showerror("Download Error", f"Error downloading data: {e}")
        return

    # Use "Adj Close" if available, else "Close"
    if "Adj Close" in data.columns:
        price_data = data["Adj Close"]
    elif "Close" in data.columns:
        price_data = data["Close"]
    else:
        messagebox.showerror("Data Error", "No appropriate price data found!")
        return

    # Compute returns
    returns = price_data.pct_change().dropna()
    
    # Generate the cluster dendrogram plot using Riskfolio
    fig, ax = plt.subplots(figsize=(10, 6))
    rp.plot_clusters(
        returns=returns,
        codependence='pearson',
        linkage='ward',
        k=None,
        max_k=10,
        leaf_order=True,
        dendrogram=True,
        ax=ax
    )
    plt.show()  # Display the plot in a new window

# Create the main window
root = tk.Tk()
root.title("Stock Cluster Analysis")

# Create and place the widgets
label_stocks = ttk.Label(root, text="Stock Symbols (comma separated):")
label_stocks.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_stocks = ttk.Entry(root, width=50)
entry_stocks.insert(0, "PANW, NVDA, AAPL, MSFT, GOOG, TSLA, DIS, AXP, GLD, ^GSPC")
entry_stocks.grid(row=0, column=1, padx=5, pady=5)

label_start = ttk.Label(root, text="Start Date (YYYY-MM-DD):")
label_start.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_start = ttk.Entry(root, width=20)
entry_start.insert(0, "2018-01-01")
entry_start.grid(row=1, column=1, padx=5, pady=5, sticky="w")

label_end = ttk.Label(root, text="End Date (YYYY-MM-DD):")
label_end.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_end = ttk.Entry(root, width=20)
entry_end.insert(0, "2025-01-10")
entry_end.grid(row=2, column=1, padx=5, pady=5, sticky="w")

button_analyze = ttk.Button(root, text="Analyze", command=analyze)
button_analyze.grid(row=3, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()

