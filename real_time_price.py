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
    price = float(soup.find(class_=class1).text.strip()[1:].replace(",",""))
    company_name =  soup.find(class_=class2).text
    print(company_name)
    print(price)
    return company_name,price


if __name__=='__main__':
    for i in range(10):
        real_time_price('INFY',"NSE")
        time.sleep(1)