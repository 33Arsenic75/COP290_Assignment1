# importing necessary libraries
from datetime import date
import pandas as pd
import yfinance as yf

def top_bottom_3_helper():
    # give a list if stocks sorted based on percentage change
    df=pd.read_csv('stock_name.csv')
    dic=[]
    for symbol in df['Symbol']:
        if (symbol=="NIFTY_50" or symbol=="SENSEX"):
            continue
        name = symbol+".NS"
        temp=pd.DataFrame(yf.download(name, period='1d'))
        if temp.empty:
            continue
        
        open_ = temp["Open"].iloc[0]
        close_ = temp["Close"].iloc[0]
        colour = 'red' if open_ > close_ else 'green'
        percent = (close_-open_)*100/(open_)
        percent = round(percent,3)
        dic.append([symbol,percent,colour])
    sorted_items = sorted(dic, key=lambda x: x[1], reverse=True)
    return sorted_items
    
def top_bottom_3(sorted_dict):
    # give top and bottom 3 stocks based on percentage change
    top_3 = sorted_dict[:3]
    bottom_3 = sorted_dict[-3:]
    return top_3,bottom_3
    

