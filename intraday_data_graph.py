import requests
import pandas as pd
from datetime import datetime,timedelta
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
from dateutil import parser

def intra_day_data(ISIN_CODE,symbol):
    start_date = datetime.now().date()
    end_date = start_date- timedelta(days=0)
    url = f'https://api.upstox.com/v2/historical-candle/NSE_EQ%7C{ISIN_CODE}/1minute/{start_date}/{end_date}'
    headers = {
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    print(ISIN_CODE)
    # Check the response status
    if response.status_code == 200:
        # Do something with the response data (e.g., print it)
        df=pd.DataFrame(response.json())
        # df.to_csv(f'intraday_data/{symbol}.csv')
        data={'Time':[],'Price':[]}
        for i in reversed(df['data']['candles']):
            data['Time'].append(datetime.fromisoformat(i[0]).strftime("%H:%M"))
            data['Price'].append(i[1])
        data=pd.DataFrame(data)
        timestamps = data['Time']
        closing_prices = data['Price']
        fig, ax = plt.subplots(figsize=(10, 6))
        # print(timestamps)
        color=''
        n = len(closing_prices)
        if(closing_prices[0]>closing_prices[n-1]):
            color='red'
        else:
            color='green'
        ax.plot(timestamps, closing_prices, label='Closing Prices', marker='', linestyle='-', color=color)
        ax.set_xticks(timestamps[::120])
        # Adjust the major locator to show labels for every 2 hours
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())

        # Rotating x-axis labels for better readability
        plt.xticks(rotation=45, ha='right')

        # Adding labels and title
        plt.xlabel('Time')
        plt.ylabel('Closing Prices')
        plt.title('Closing Prices Over Time')

        # Display the legend
        plt.legend()

        # Show the plot
        plt.savefig(f'intraday_data/{symbol}.png',transparent=True)
        plt.close()
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code} - {response.text}")
        

if __name__ == '__main__':
    # Read the CSV file into a DataFrame
    data = pd.read_csv('ind_nifty50list.csv')
    # intra_day_data(ISIN_CODE='INE423A01024', symbol='ADANIENT')
    # Iterate through the 'ISIN Code' and 'Symbol' columns simultaneously
    for code, symbol in zip(data['ISIN Code'], data['Symbol']):
        intra_day_data(ISIN_CODE=code, symbol=symbol)
