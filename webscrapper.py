#The default tutorial web scrapper to learn how to Code

from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get('https://books.toscrape.com/')
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
books = soup.find_all('li', attrs={'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
# for name in test:
#     print(name.text)

#Save to CSV file
# file_name = ('Book.csv')
# f = open(file_name, 'w')

for book in books:
    book_title = book.h3.a['title']
    
    book_price = book.find_all('p', {'class': 'price_color'})
    
    price = book_price[0].text.strip()
    
    print(book_title, end= ' ')
    print(price)
