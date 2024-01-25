# importing necessary libraries
from datetime import date
from jugaad_data.nse import bhavcopy_save, bhavcopy_fo_save
import pandas as pd
import time
import os
import matplotlib.pyplot as plt
from jugaad_data.nse import stock_df
import sys
import pyarrow

from get_stock_data import get_stock_data

def get_Graph(symbol,years,selected_columns):
    df=get_stock_data(symbol=symbol,years=years)
    # Plotting
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot the first column with the primary y-axis
    ax1.plot(df['DATE'], df[selected_columns[0]], marker='o', linestyle='-', label=selected_columns[0], color='b')
    ax1.set_xlabel('Date')
    ax1.set_ylabel(selected_columns[0], color='b')
    ax1.tick_params('y', colors='b')

    # Create a secondary y-axis for the remaining columns
    ax2 = ax1.twinx()

    # Plot the remaining columns with different scales and colors
    for i, col in enumerate(selected_columns[1:], start=1):
        ax2.plot(df['DATE'], df[col], marker='o', linestyle='-', label=col)
        ax2.set_ylabel(col)

    # Display the legend for both y-axes
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # Save the plot
    plt.title('Stock Prices Over Time')
    plt.grid(True)
    plt.savefig(f'static/{symbol}.png',transparent=True)
    return plt