import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller


class BrentOilAnalysis:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.preprocess_data()

    def preprocess_data(self):
        self.df['Date'] = pd.to_datetime(self.df['Date'], format='mixed')
        self.df.set_index('Date', inplace=True)
        self.df.sort_index(inplace=True)
        self.df['Price'] = self.df['Price'].ffill()
        self.df['Log_Return'] = np.log(
            self.df['Price'] / self.df['Price'].shift(1))

    def plot_trend(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.df.index, self.df['Price'], color='blue')
        plt.title('Task 1: Brent Oil Price Trend Analysis')
        plt.show()

    def check_stationarity(self):
        print("\n--- Stationarity Testing (ADF Test) ---")
        res = adfuller(self.df['Price'].dropna())
        print(f'Price p-value: {res[1]:.4f}')
        return res[1]

    def plot_volatility(self):
        plt.figure(figsize=(12, 5))
        plt.plot(self.df.index, self.df['Log_Return'], color='red')
        plt.title('Task 1: Volatility Patterns (Log Returns)')
        plt.show()
