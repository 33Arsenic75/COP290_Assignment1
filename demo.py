from jugaad_data.nse import NSELive
import pandas as pd
import requests
from io import BytesIO
from PIL import Image


def download_and_save_svg(url, save_path):
    try:
        # Send a GET request to the URL with headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15'
        }
        response = requests.get(url, headers=headers)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Save the SVG content to the specified path
            with open(save_path, 'wb') as svg_file:
                svg_file.write(response.content)
            print(f"SVG downloaded and saved successfully: {save_path}")
        else:
            print(f"Failed to download SVG. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading SVG: {e}")
        
        
if __name__ == '__main__':
    n = NSELive()
    all_indices = (n.all_indices())['data'][0]
    chart365dPath = all_indices['chart365dPath']
    chart30dPath  = all_indices['chart30dPath']
    chartTodayPath= all_indices['chartTodayPath']
    download_and_save_svg(chartTodayPath,'index_graph/Nifty_Today')
    download_and_save_svg(chart30dPath,'index_graph/Nifty_30d')
    download_and_save_svg(chart365dPath,'index_graph/Nifty_365d')
    

