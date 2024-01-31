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

def top_bottom_3_helper():
    df=pd.read_csv('stock_name.csv')
    dic={}
    for symbol in df['Symbol']:
        try:
            temp=get_stock_data(symbol=symbol,years=1)
            open_  = temp["OPEN"][0]
            close_ = temp["CLOSE"][0]
            colour = 'red' if open_ > close_ else 'green'
            percent = (close_-open_)*100/(open_)
            percent = round(percent,3)
            dic[symbol]=[symbol,percent,colour]
        except:
            continue
    sorted_items = sorted(dic.items(), key=lambda x: x[1][1], reverse=True)
    return sorted_items
    
def top_bottom_3():
    sorted_items=top_bottom_3_helper()
    sorted_dict = dict(sorted_items)
    top_3 = list(sorted_dict.values())[:3]
    bottom_3 = list(sorted_dict.values())[-3:]
    return top_3,bottom_3
    
print(top_bottom_3())
