import requests
from bs4 import BeautifulSoup
import pandas as pd

cookies = {
    'zguid': '24|%24ce2f5443-2e51-4ec7-b5f1-d694781955bc',
    'zjs_anonymous_id': '%22ce2f5443-2e51-4ec7-b5f1-d694781955bc%22',
    'zjs_user_id': 'null',
    'zg_anonymous_id': '%22a0001df1-b7ae-4398-b292-ee9eaac4e85b%22',
    'g_state': '{"i_p":1713908095783,"i_l":3}',
    'zgsession': '1|4cd24f35-f2fa-4446-ba51-dd236e816804',
    'JSESSIONID': '02C91D8772197B5B093CE51A38667880',
    'AWSALB': 'T0EkTYXjoBURfaVAkXy0RYRiQY/fV8xJFMMiU+EF5HxwllF8sX3bz6Pn5QkcK230c8j96gnfp6LwC0eCjR4jWt4CSjFPpKXI2a5tqK72XWg4ZaMAAx0qbOrquWBU',
    'AWSALBCORS': 'T0EkTYXjoBURfaVAkXy0RYRiQY/fV8xJFMMiU+EF5HxwllF8sX3bz6Pn5QkcK230c8j96gnfp6LwC0eCjR4jWt4CSjFPpKXI2a5tqK72XWg4ZaMAAx0qbOrquWBU',
    'search': '6|1719203999715%7Crect%3D42.43891079093197%2C-72.36787257568359%2C42.29660833051234%2C-72.6432174243164%26rid%3D50721%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D0%26listPriceActive%3D1%26type%3Dhouse%2Ccondo%2Ctownhouse%2Capartment%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26student-housing%3D0%26income-restricted-housing%3D0%26military-housing%3D0%26disabled-housing%3D0%26senior-housing%3D0%26excludeNullAvailabilityDates%3D0%26isRoomForRent%3D0%26isEntirePlaceForRent%3D1%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0950721%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Atrue%7D%09%09%09%09%09',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'content-type': 'application/json',
    # 'cookie': 'zguid=24|%24ce2f5443-2e51-4ec7-b5f1-d694781955bc; zjs_anonymous_id=%22ce2f5443-2e51-4ec7-b5f1-d694781955bc%22; zjs_user_id=null; zg_anonymous_id=%22a0001df1-b7ae-4398-b292-ee9eaac4e85b%22; g_state={"i_p":1713908095783,"i_l":3}; zgsession=1|4cd24f35-f2fa-4446-ba51-dd236e816804; JSESSIONID=02C91D8772197B5B093CE51A38667880; AWSALB=T0EkTYXjoBURfaVAkXy0RYRiQY/fV8xJFMMiU+EF5HxwllF8sX3bz6Pn5QkcK230c8j96gnfp6LwC0eCjR4jWt4CSjFPpKXI2a5tqK72XWg4ZaMAAx0qbOrquWBU; AWSALBCORS=T0EkTYXjoBURfaVAkXy0RYRiQY/fV8xJFMMiU+EF5HxwllF8sX3bz6Pn5QkcK230c8j96gnfp6LwC0eCjR4jWt4CSjFPpKXI2a5tqK72XWg4ZaMAAx0qbOrquWBU; search=6|1719203999715%7Crect%3D42.43891079093197%2C-72.36787257568359%2C42.29660833051234%2C-72.6432174243164%26rid%3D50721%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D0%26listPriceActive%3D1%26type%3Dhouse%2Ccondo%2Ctownhouse%2Capartment%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26student-housing%3D0%26income-restricted-housing%3D0%26military-housing%3D0%26disabled-housing%3D0%26senior-housing%3D0%26excludeNullAvailabilityDates%3D0%26isRoomForRent%3D0%26isEntirePlaceForRent%3D1%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0950721%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Atrue%7D%09%09%09%09%09',
    'origin': 'https://www.zillow.com',
    'priority': 'u=1, i',
    'referer': 'https://www.zillow.com/amherst-ma/rentals/',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
}

json_data = {
    'searchQueryState': {
        'pagination': {},
        'isMapVisible': False,
        'mapBounds': {
            'west': -72.6432174243164,
            'east': -72.36787257568359,
            'south': 42.29660833051234,
            'north': 42.43891079093197,
        },
        'regionSelection': [
            {
                'regionId': 50721,
                'regionType': 6,
            },
        ],
        'filterState': {
            'isForRent': {
                'value': True,
            },
            'isForSaleByAgent': {
                'value': False,
            },
            'isForSaleByOwner': {
                'value': False,
            },
            'isNewConstruction': {
                'value': False,
            },
            'isComingSoon': {
                'value': False,
            },
            'isAuction': {
                'value': False,
            },
            'isForSaleForeclosure': {
                'value': False,
            },
            'isMultiFamily': {
                'value': False,
            },
            'isLotLand': {
                'value': False,
            },
            'isManufactured': {
                'value': False,
            },
        },
        'isListVisible': True,
        'mapZoom': 12,
    },
    'wants': {
        'cat1': [
            'listResults',
        ],
    },
    'requestId': 3,
    'isDebugRequest': False,
}

response = requests.put('https://www.zillow.com/async-create-search-page-state', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"searchQueryState":{"pagination":{},"isMapVisible":false,"mapBounds":{"west":-72.6432174243164,"east":-72.36787257568359,"south":42.29660833051234,"north":42.43891079093197},"regionSelection":[{"regionId":50721,"regionType":6}],"filterState":{"isForRent":{"value":true},"isForSaleByAgent":{"value":false},"isForSaleByOwner":{"value":false},"isNewConstruction":{"value":false},"isComingSoon":{"value":false},"isAuction":{"value":false},"isForSaleForeclosure":{"value":false},"isMultiFamily":{"value":false},"isLotLand":{"value":false},"isManufactured":{"value":false}},"isListVisible":true,"mapZoom":12},"wants":{"cat1":["listResults"]},"requestId":3,"isDebugRequest":false}'
#response = requests.put('https://www.zillow.com/async-create-search-page-state', cookies=cookies, headers=headers, data=data)


headers = {
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'https://www.zillow.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'Content-Type': 'text/plain;charset=UTF-8',
}

params = {
    'sentry_key': 'a0dfc4d25bb843acb944ff1d115fd1b2',
    'sentry_version': '7',
    'sentry_client': 'sentry.javascript.nextjs/7.54.0',
}

data = '{"sent_at":"2024-05-25T04:40:30.617Z","sdk":{"name":"sentry.javascript.nextjs","version":"7.54.0"}}\n{"type":"session"}\n{"sid":"3a55b663cecf4236ae6dc0a6b2df49fe","init":false,"started":"2024-05-25T04:40:00.664Z","timestamp":"2024-05-25T04:40:30.617Z","status":"exited","errors":0,"attrs":{"release":"K7K4mMsp3Lt2Rji86J6vN","environment":"prod","user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"}}'

response = requests.post(
    'https://o168728.ingest.sentry.io/api/4505313524383744/envelope/',
    params=params,
    headers=headers,
    data=data,
)


headers = {
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'https://www.zillow.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'Content-Type': 'text/plain;charset=UTF-8',
}

params = {
    'sentry_key': 'a0dfc4d25bb843acb944ff1d115fd1b2',
    'sentry_version': '7',
    'sentry_client': 'sentry.javascript.nextjs/7.54.0',
}

data = '{"sent_at":"2024-05-25T04:40:30.618Z","sdk":{"name":"sentry.javascript.nextjs","version":"7.54.0"}}\n{"type":"session"}\n{"sid":"a09d19831072473f9a982c4ad5528c99","init":true,"started":"2024-05-25T04:40:30.617Z","timestamp":"2024-05-25T04:40:30.617Z","status":"ok","errors":0,"attrs":{"release":"K7K4mMsp3Lt2Rji86J6vN","environment":"prod","user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"}}'

response = requests.post(
    'https://o168728.ingest.sentry.io/api/4505313524383744/envelope/',
    params=params,
    headers=headers,
    data=data,
)

with requests.session() as s:
    #Finding the total number of page on zillow listing
    page_num = s.get('https://www.zillow.com/amherst-ma/rentals/', headers = headers, timeout = 20)
    temp_soup = BeautifulSoup(page_num.text, 'html.parser')
    text = temp_soup.find('span', attrs = {'class': 'Text-c11n-8-100-8__sc-aiai24-0 lmjttZ'})
    END_PAGE = int(text.text[-1])

    soup_list = []
    for page in range(1, END_PAGE + 1):
        url = 'https://www.zillow.com/amherst-ma/rentals/' + f'{page}_p/'
        request = s.get(url, headers = headers, timeout = 20)
        soup = BeautifulSoup(request.content, 'html.parser')
        soup_list.append(soup)

df_list = []
for page_of_listing in soup_list:
    df = pd.DataFrame()
    address = page_of_listing.find_all('address', attrs = {'data-test': 'property-card-addr'})
    print(len(address))