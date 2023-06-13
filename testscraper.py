

#This comment is going to be ignored, I just wanted to try out python
print("Bonita Smoke Shop Price Scraper of the MSRP")
#Okay now I'm going to try the web scraper
import requests
from bs4 import BeautifulSoup

# Set the URL of the page you want to scrape
url = 'https://bonitasmokeshop.com/arturo-fuente-don-carlos-double-robusto/'

# Connect to the website and retrieve the HTML content
response = requests.get(url)
html = response.content

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')

# Find the price element in the HTML using a CSS selector
price_element = soup.select_one('.price')

# Extract the price text from the element
price_text = price_element.get_text()

# Convert the price text to a float
price = float(price_text.replace('$', ''))

# Print the price
print('The price of the product is:', price)

soup.find_all("a")