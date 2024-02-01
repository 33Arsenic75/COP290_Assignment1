import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def get_soup(ticker, exchange):
    # gives the soup for a specific stock google webpage
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def real_time_price(ticker, exchage):
    # scraps the data using bs4 and selenium
    soup = get_soup(ticker=ticker, exchange=exchage)
    class1 = "YMlKec fxKbKc"
    class2 = "zzDege"
    class3 = ["P2Luy", "Ebnabc", "ZYVHBb"]
    class7 = "P2Luy Ez2Ioe ZYVHBb"
    class4 = "JwB6zf"
    class5 = "gyFHrc"
    class6 = "P6K39c"
    price = float(soup.find(class_=class1).text.replace(",", "").replace("₹", ""))
    company_name = soup.find(class_=class2).text
    previous = float(
        soup.find_all(class_=class6)[0].text.replace("₹", "").replace(",", "")
    )
    change = round((price - previous), 2)
    percentage_change = round((float(change / previous) * 100), 3)
    try:
        pe_ratio = float(soup.find_all(class_=class6)[4].text)
    except:
        pe_ratio = None
    return company_name, price, change, percentage_change, pe_ratio


def get_prev_closing(ticker, exchage):
    soup = get_soup(ticker=ticker, exchange=exchage)
    class6 = "P6K39c"
    previous = float(
        soup.find_all(class_=class6)[0].text.replace("₹", "").replace(",", "")
    )
    previous = round(previous, 2)
    return previous


def fetch_real_time():
    # returns price, change, percentage change and pe ratio for all nifty 50 stocks
    df = pd.read_csv("ind_nifty50list.csv")
    dict = {}
    for symbol, exchange, exchange in zip(df["Symbol"], df["Exchange"], df["Exchange"]):
        if exchange == "NSE":
            company_name, price, change, percentage_change, pe_ratio = real_time_price(
                ticker=symbol, exchage=exchange
            )
            dict[company_name] = (price, change, percentage_change, pe_ratio)
    return dict
