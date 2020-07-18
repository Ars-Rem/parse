import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/newauto/marka-jaguar/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/83.0.4103.116 Safari/537.36', 'accept': '*/*'}
HOST = 'https://auto.ria.com'


def get_url(url, params=None):
    res = requests.get(url, headers=HEADERS, params=params)
    return res


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='proposition')

    cars = []
    for item in items:
        uah_prise = item.find('span', class_='grey size13')
        if uah_prise:
            uah_prise = uah_prise.get_text(strip=True)
        else:
            print('Цены нет')

        cars.append({
            'title': item.find('div', class_='proposition_title').get_text(strip=True),
            'link': HOST + item.find('a', class_='').get('href'),
            # 'price': item.find('div', class_='proposition_price').get_text(strip=True),
            'usd_prise': item.find('span', class_='green').get_text(strip=True),
            'uah_prise': uah_prise,
            'city': item.find('svg', class_='svg-i16_pin').find_next('strong').get_text()


        })
    print(cars)
    return cars


def parse():
    html = get_url(URL)
    if html.status_code == 200:
        print('Response Ok')
        cars = get_content(html.text)
    else:
        print("Error response")


parse()
