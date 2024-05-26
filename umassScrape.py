from bs4 import BeautifulSoup
import requests
from selenium import webdriver



driver = webdriver.Edge()
driver.get('https://offcampushousing.umass.edu/housing')

# page_to_scrape = requests.get('https://offcampushousing.umass.edu/')
soup = BeautifulSoup(driver.page_source, 'html.parser')
num_place = int((soup.find('p',
                          attrs = {'class': 'list-search-results-available-count'})).text.split()[0])


listings = []
i = 1
while len(listings) < 2:
    url = 'https://offcampushousing.umass.edu/housing/page-' + f'{i}'
    driver.get(url)
    temp_soup = BeautifulSoup(driver.page_source, 'html.parser')
    listings.extend(temp_soup.find_all('li', attrs = {'class': 'list-result-item'}))
    i += 1

for house in listings[:2]:
    name = house.find('a', attrs = {'class': 'card-anchor text-wrap'}).text
    address = house.find('address', attrs = {'class': 'copy-row address-container'}).text
    num_bed = int(house.find('span', attrs = {'class': 'price-range'}).text.split()[0])
    price = house.find('span', attrs = {'class': 'border-left'}).text
    distant_from_campus = 
    print(name, address, num_bed, price)
    

# for name in test:
#     print(name.text)

#Save to CSV file
# file_name = ('Book.csv')
# f = open(file_name, 'w')

# for book in books:
#     book_title = book.h3.a['title']
    
#     book_price = book.find_all('p', {'class': 'price_color'})
    
#     price = book_price[0].text.strip()
    
#     print(book_title, end= ' ')
#     print(price)