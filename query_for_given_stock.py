# importing necessary libraries
import os
import pandas as pd
from sqlalchemy import create_engine
import sys
from query_for_stock import execute_query_on_db

if __name__ == '__main__':
    symbol = sys.argv[1]
    query = sys.argv[2]
    execute_query_on_db(f'{symbol}.db', query)