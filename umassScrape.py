import operator
import csv
import math
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run():
    driver = webdriver.Chrome()
    driver.get('https://offcampushousing.umass.edu/housing')


    soup = BeautifulSoup(driver.page_source, 'html.parser')
    num_place = int((soup.find('p',
                            attrs = {'class': 'list-search-results-available-count'})).text.split()[0])

    listings = []
    i = 1
    while i <= math.ceil(num_place / 40):
        url = 'https://offcampushousing.umass.edu/housing/page-' + f'{i}'
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'body')))
        temp_soup = BeautifulSoup(driver.page_source, 'html.parser')
        listings.extend(temp_soup.find_all('li', attrs = {'class': 'list-result-item'}))
        i += 1

    print(len(listings))
    houses = []

    #Ways to sort
    price_comparator = operator.attrgetter('price')
    distant_comparator = operator.attrgetter('distant_from_campus')
    num_bed_comparator = operator.attrgetter('num_bed')

    diffrent_util = {}
    #Link prefix
    LINK_PREFIX = "https://offcampushousing.umass.edu"

    for house in listings:
        #Contact INFO
        phone_number = house.find_all('span', attrs = {'class': 'hidden sm:inline'})[-1].text

        distant_from_campus = house.find('span', attrs = {'class': 'bold'}).text.split()[0]
        distant_from_campus = distant_from_campus.replace("+", "")
        distant_from_campus = float(distant_from_campus)

        #Link to the Listing itself
        link = LINK_PREFIX + house.find('a', attrs = {'class': 'card-anchor text-wrap'}).get('href')
        #Scrapping more details about the House
        driver.get(link)
        sub_soup = BeautifulSoup(driver.page_source, 'html.parser')


        name = sub_soup.h1
        if name:
            name = name.text
        else:
            name = np.nan

        address = sub_soup.find('p', attrs = {'data-qaid': 'address'})
        if address:
            address = address.text
        else:
            address = np.nan

        floor_plan_options = sub_soup.find_all('tr', attrs = {'data-qaid': 'floorPlanRow'})
        del floor_plan_options[1::2] #Remove the hidden css that is meant for Mobile User

        util_include = ""
        raw_util_included = sub_soup.find('table', attrs = {'class': 'expenses-table',
                                                        'data-qaid': 'utilities'})
        if raw_util_included:
            raw_util_included = raw_util_included.find_all('td', attrs = {'data-qaid': 'name'})
            #A list of utilities included in the Listing
            for util in raw_util_included:
                diffrent_util[util.text] = 1
                util_include += util.text + ", "
        for option in floor_plan_options:
            num_bed = option.find('td', attrs = {'data-qaid' : 'beds'}).text
            num_bed = num_bed.split()[0]
            is_Studio = 0
            if num_bed != "Studio":
                num_bed = int(num_bed)
            else:
                num_bed = 1
                is_Studio = 1

            num_bath = float(option.find('td', attrs = {'data-qaid': 'baths'}).text.split()[0])


            whole_price_str = option.find('td', attrs = {'data-qaid' : 'price'}).text
            whole_price_str = whole_price_str.replace("$", "")
            whole_price_str = whole_price_str.replace(",", "")
            whole_price_str = whole_price_str.split()

            price = whole_price_str[-1]

            for i, s in enumerate(whole_price_str):
                if s == "/":
                    price = whole_price_str[i - 1]
                    break

            try:
                price = int(price)
                price = math.ceil(price / num_bed)
            except:
                price = np.nan

            sq_feet = option.find('td', attrs = {'data-qaid' : 'sqFeet'})
            if sq_feet:
                sq_feet = sq_feet.text
                if sq_feet:
                    sq_feet = sq_feet.replace(",", '')
                    sq_feet = int(sq_feet.split()[-1])
            else:
                sq_feet = np.nan

            max_occu = option.find('td', attrs = {'data-qaid' : 'maxOccupants'})
            if max_occu:
                max_occu = max_occu.text.split()
                if max_occu:
                    max_occu = int(max_occu[0])
                else:
                    max_occu = np.nan
            else:
                max_occu = np.nan

            houses.append({
                'Link': link,
                'Phone Number': phone_number,
                'Name': name,
                'Address': address,
                'Distant From Campus': distant_from_campus,
                'Bedroom(s)': num_bed,
                'Is Studio?': is_Studio,
                'Bathroom(s)': num_bath,
                'Included Utilities': util_include,
                'Price/Bed': price,
                'Size (square Feet)': sq_feet,
                'MAXIMUM Number of People': max_occu,
            })

    print(num_place, len(houses))

    #Write to a CSV File to store the data for future usage.
    keys = houses[0].keys()

    with open('housing_data.csv', 'w', newline='', encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(houses)

    print(diffrent_util.keys())
    return(list(diffrent_util.keys()))
