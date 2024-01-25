import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_soup(ticker,exchange):
    url = f'https://www.google.com/finance/quote/{ticker}:{exchange}'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def real_time_price(ticker,exchage):
    soup=get_soup(ticker=ticker,exchange=exchage)
    class1 = "YMlKec fxKbKc" 
    class2 = "zzDege"
    class3 = ["P2Luy", "Ebnabc", "ZYVHBb"]
    # "P2Luy Ebnabc ZYVHBb"
    price = float(soup.find(class_ = class1).text.strip()[0:].replace(",",""))
    change  = float(soup.find('span',class_ = class3).text)
    company_name =  soup.find(class_=class2).text
    print(company_name)
    print(price)
    print(change)
   
# if __name__=='__main__':
#     for i in range(5):
#         real_time_price('NIFTY_50',"INDEXNSE")
#         time.sleep(1)