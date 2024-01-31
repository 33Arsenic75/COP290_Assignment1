from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main(ticker, exchange):
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    # Set ChromeOptions for configuring the behavior of the Chrome browser
    options = webdriver.ChromeOptions()

    # Set the browser to run in headless mode
    options.add_argument("--headless")

    # Disable the GPU
    options.add_argument("--disable-gpu")

    # Define preferences to configure the behavior of the browser profile
    prefs = {"profile.default_content_setting_values.notifications": 2}

    # Add experimental options to the ChromeOptions
    options.add_experimental_option("prefs", prefs)

    # Set window size
    options.add_argument("window-size=1920x1080")

    # Initialize the WebDriver for Chrome, specifying the ChromeDriverManager to manage the Chrome driver
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

    # Define the URL of the webpage to be scraped
    # url = "https://www.google.com/finance/quote/NIFTY_50:INDEXNSE"

    # Open the specified URL in the headless Chrome browser
    driver.get(url)

    # Set up a WebDriverWait instance with a timeout of 10 seconds
    wait = WebDriverWait(driver, 10)

    # Wait until an element matching the specified CSS selector (".ushogf svg") is present in the DOM
    svg_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".ushogf svg"))
    )

    # Get the outer HTML content of the located SVG element
    svg_outer_html = svg_element.get_attribute("outerHTML")

    # Quit the WebDriver and close the browser window
    driver.quit()

    # Return the outer HTML content of the SVG element
    return svg_outer_html
