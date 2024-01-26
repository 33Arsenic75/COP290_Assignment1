import requests
from bs4 import BeautifulSoup
from real_time_price import get_soup

symbol = 'NIFTY_50'
exchange = 'INDEXNSE'
class_name = 'ushogf'

soup = get_soup(symbol, exchange)
print(soup.prettify())
svg_element = soup.find('svg', class_=class_name)

# Extract path data from the SVG element
path_elements = svg_element
for path in path_elements:
    path_data = path.get('d')
    print("Path Data:", path_data)
