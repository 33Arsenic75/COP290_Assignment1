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
import concurrent.futures

def generate_db(df, symbol,company_name):
    engine = create_engine(f'sqlite:///historical_data/{company_name}.db')
    
    # Convert the DataFrame to a SQL table
    df.to_sql('stock_data_table', con=engine, if_exists='replace', index=False)

def process_stock_data(row):
    if row['Exchange'] != 'NSE':
        return None

    symbol = row['Symbol']
    company_name = row['Company Name']
    
    df = get_stock_data(symbol=symbol, years=10)
    generate_db(df, symbol, company_name)

if __name__ == '__main__':
    with open('ind_nifty50list.csv', 'r') as file:
        csv_reader = csv.DictReader(file)

        # Using ThreadPoolExecutor for parallel processing
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Submit tasks for each row in the CSV file
            futures = [executor.submit(process_stock_data, row) for row in csv_reader]

            # Wait for all tasks to complete
            concurrent.futures.wait(futures)
            
            # Optional: You can collect results or handle exceptions if needed
            # results = [future.result() for future in futures]
            # handle_results(results)
