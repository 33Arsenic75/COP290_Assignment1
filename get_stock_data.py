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
def get_stock_data(symbol, years):
    # Calculate the start and end date based on the number of years
    end_date = date.today()
    start_date = end_date.replace(year=end_date.year - years)
    # Fetch stock data using jugaad_data.nse
    try:
        stock_info = stock_df(
            symbol=symbol,
            from_date=date(start_date.year, start_date.month, start_date.day),
            to_date=date(end_date.year, end_date.month, end_date.day),
            series="EQ"
        )
    except Exception as e:
        print(f"An error occurred while fetching stock info: {e}")
        stock_info = None  # or any default value or action you want
    # Extracting required columns
    # Convert the data dictionary to a Pandas DataFrame
    df = pd.DataFrame(stock_info)
    #print(df)
    # Convert the 'Date' column to datetime format
    #df['Date'] = pd.to_datetime(df['Date'])

    # Date, Open Price, Close Price, High, Low, Last Trade Price (LTP), Volumne, Value and Number of Trades
    columns_to_remove = ['PREV. CLOSE', 'SERIES', '52W H', 'VWAP', 'SYMBOL', '52W L']
    for column in columns_to_remove:
        if column in df.columns:
            df = df.drop(columns=column)
    # print(df.columns)
    print(symbol)
    return df

if __name__=='__main__':
    df=pd.read_csv('ind_nifty50list.csv')
    for symbol in df['Symbol']:
        get_stock_data(symbol=symbol,years=1)