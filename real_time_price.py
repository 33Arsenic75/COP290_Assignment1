import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def get_soup(ticker, exchange):
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def real_time_price(ticker, exchage):
    soup = get_soup(ticker=ticker, exchange=exchage)
    class1 = "YMlKec fxKbKc"
    class2 = "zzDege"
    class3 = ["P2Luy", "Ebnabc", "ZYVHBb"]
    class4 = "JwB6zf"
    price = float(soup.find(class_=class1).text.replace(",", "").replace("₹", ""))
    change = float(soup.find("span", class_=class3).text)
    company_name = soup.find(class_=class2).text
    percentage_change = float(soup.find(class_=class4).text.replace("%", ""))
    print(company_name, price, change, percentage_change)
    return company_name, price, change, percentage_change


if __name__ == "__main__":
    df = pd.read_csv("ind_nifty50list.csv")
    # for symbol, exchange in zip(df["Symbol"], df["Exchange"]):
    #     real_time_price(ticker=symbol, exchage=exchange)
    real_time_price("NIFTY_50", "INDEXNSE")
