# importing necessary libraries
from datetime import date
import pandas as pd
import yfinance as yf

def top_bottom_3_helper():
    df=pd.read_csv('stock_name.csv')
    dic=[]
    for symbol in df['Symbol']:
        if (symbol=="NIFTY_50" or symbol=="SENSEX"):
            continue
        name = symbol+".NS"
        temp=pd.DataFrame(yf.download(name, period='1d'))
        if temp.empty:
            continue
        
        open_ = temp["Open"].iloc[0]  # Get the first (and only) value in the "Open" column
        close_ = temp["Close"].iloc[0]
        colour = 'red' if open_ > close_ else 'green'
        percent = (close_-open_)*100/(open_)
        #print(open_,close_)
        percent = round(percent,3)
        dic.append([symbol,percent,colour])
    # for i in dic:
    #     print(i)
    sorted_items = sorted(dic, key=lambda x: x[1], reverse=True)
    return sorted_items
    
def top_bottom_3(sorted_dict):
    top_3 = sorted_dict[:3]
    bottom_3 = sorted_dict[-3:]
    return top_3,bottom_3
    

