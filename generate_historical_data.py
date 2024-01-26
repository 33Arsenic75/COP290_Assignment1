# importing necessary libraries
from datetime import date
from jugaad_data.nse import bhavcopy_save, bhavcopy_fo_save
import pandas as pd
import time
import os
import matplotlib.pyplot as plt
from jugaad_data.nse import stock_df
import sys
from get_stock_data import get_stock_data
from sqlalchemy import create_engine
import csv

def generate_db(df, symbol,company_name):
    engine = create_engine(f'sqlite:///historical_data/{company_name}.db')
    
    # Convert the DataFrame to a SQL table
    df.to_sql('stock_data_table', con=engine, if_exists='replace', index=False)

if __name__ == '__main__':
    with open('ind_nifty50list.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['Exchange'] != 'NSE':
                continue
            #print(row['Symbol'])
            df = get_stock_data(symbol=row['Symbol'], years=40)
            generate_db(df, row['Symbol'],row['Company Name'])
