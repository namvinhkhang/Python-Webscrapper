import time
from selenium import webdriver
from bs4 import BeautifulSoup
import json

# Start the WebDriver
driver = webdriver.Chrome()

# Navigate to the Zillow website
driver.get('https://www.zillow.com/homes/for_sale/New-York_rb/')

# Wait for the page to load
time.sleep(5)

# Scroll down the page to load more listings
last_height = driver.execute_script("return window.scrollY;")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return window.scrollY;")
    if new_height == last_height:
        break
    last_height = new_height

# Extract the data from the page
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Find the JSON data in the page source
json_data = None
for script in soup.find_all('script'):
    if script.text.startswith('window.zillow'):
        json_data = script.text
        break

if json_data:
    # Parse the JSON data
    json_data = json_data.replace('window.zillow=', '')
    data = json.loads(json_data)

    # Extract the search results
    content = data['searchResults']['listResults']

    # Process the data
    for item in content:
        price = item['price']
        address = item['address']['street']
        number_of_bed = item['bedrooms']
        size = item['area']
        status = item['statusText']

        property_data = {
            'link': 'https://www.zillow.com' + item['detailUrl'],
            'price': price,
            'address': address,
            'number of bed': number_of_bed,
            'size (sqft)': size,
            'status': status,
        }

        print(property_data)

# Close the WebDriver
driver.quit()