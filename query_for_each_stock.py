# importing necessary libraries
import os
import pandas as pd
from sqlalchemy import create_engine
import sys
from query_for_stock import execute_query_on_db

if __name__ == '__main__':
    query = sys.argv[1]

    # Assuming 'data' is the folder containing your database files
    data_folder = 'data'
    db_files = [file for file in os.listdir(data_folder) if file.endswith('.db')]

    for db_file in db_files:
        print(db_file)
        execute_query_on_db(db_file, query)
