import requests
from bs4 import BeautifulSoup
import time

def getHtmlcode(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        return soup
    else:
        print(f"Błąd pobrania zawartości strony {response.status_code}")

def getElementId(soup):
    elements_with_class = soup.find_all('div', class_='css-1sw7q4x')

    id_href_map = {}

    for element in elements_with_class:
        element_id = element.get('id')
        element_href = element.find('a', href=True).get('href') if element.find('a', href=True) else None
        img_src = element.find()
        special_product = element.find('div', {'class': 'css-1jh69qu'})


        if element_id and element_href and not special_product:
            id_href_map[element_id] = element_href

    return id_href_map

def MonitorMode(url):
    all_cards = []

    while True:
        print('waiting')
        time.sleep(30)  # Czekaj 30 sekund

        soup = getHtmlcode(url)
        new_href_map = getElementId(soup)

        for new_id, new_href in new_href_map.items():
            if new_id not in all_cards:
                print("New card found with ID:", new_id)
                print("Link:", new_href)
                all_cards.append(new_id)

# Example usage:
url = 'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/q-wynajem-mieszkania/?search%5Border%5D=created_at%3Adesc#895856146'
MonitorMode(url)

