# Stock-Cluster-Analyzer

- A Python-based tool to analyze stock clustering based on @quantscience_ (X) approach, made ready to use with a tkinter UI.
- Helps you to build a portfolio with uncorrelated assets
  
## Features

- **Ticker stock selection:**  
  Manually enter ticker symbols in the tkinter UI.

- **Time period selection:**  
  Select start and end dates for the analysis.

- **Data download:**  
  Retrieve historical price data using yfinance.

- **Return Computation:**  
  Calculate daily returns based on adjusted (or close) prices.

- **Clustering visualization:**  
  Generate a dendrogram of stock clusters using Riskfolio.

> **Note:**  
> When choosing stocks, make sure the time period corresponds to the available price data. For example for the time period 2015-01-01 to 2025-01-01 make sure you pick a stock that IPO'd before 2015 or it will not be displayed on the graph.


## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/leove4/stock-cluster-analyzer.git
   cd stock-cluster-analyzer

2. **Install requirements**

   ```bash
   pip install -r requirements.txt

3. **Run the program**

   ```bash
   python fi_ui.py
