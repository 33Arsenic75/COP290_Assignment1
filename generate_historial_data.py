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

def generate_db(df, symbol):
    engine = create_engine(f'sqlite:///historial_data/{symbol}.db')
    
    # Convert the DataFrame to a SQL table
    df.to_sql('stock_data_table', con=engine, if_exists='replace', index=False)

if __name__ == '__main__':
    with open('ind_nifty50list.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['Series'] != 'EQ':
                continue
            #print(row['Symbol'])
            df = get_stock_data(symbol=row['Symbol'], years=1)
            generate_db(df, row['Symbol'])
