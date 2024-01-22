# importing necessary libraries
import os
import pandas as pd
from sqlalchemy import create_engine
import sys

def execute_query_on_db(db_file, query):
    engine = create_engine(f'sqlite:///data/{db_file}')

    try:
        result = pd.read_sql_query(query, con=engine)
        if not result.empty:
            print(f"Results for query in database '{db_file}':")
            print(result)
            print("\n")
    except Exception as e:
        print(f"An error occurred while executing the query in database '{db_file}': {e}")