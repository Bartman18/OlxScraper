import requests
from bs4 import BeautifulSoup



def getDetails(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        divy = []
        divy = soup.find_all('li', {'class': 'css-1r0si1e'})

        if divy:
            # Iteruj przez wszystkie znalezione divy
            for i in divy:
                print(i.text)
            return i.text
        else:
            print(f'Nie znaleziono divów o klasie "css-1r0si1e"')
    else:
        print(f'Błąd podczas pobierania strony. Kod odpowiedzi: {response.status_code}')


def getAllImage(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        imageClass = soup.find_all('div', {'class': 'swiper-zoom-container'})

        if imageClass:
            for index, div_content in enumerate(imageClass):
                imgTag = div_content.find('img')
                if imgTag:
                    imgSrc = imgTag.get('src')
                    print(f'Zawartość src dla diva {index + 1}: {imgSrc}')
                else:
                    print(f'Nie znaleziono tagu img w divie {index + 1}')
        else:
            print(f'Nie znaleziono divów o klasie "swiper-zoom-container"')
    else:
        print(f'Błąd podczas pobierania strony. Kod odpowiedzi: {response.status_code}')


def getPrice(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        price = soup.find('h3', {'class': 'css-93ez2t'})

        if price:

            return price.text
        else:
            print('Nie znaleziono elementu o klasie: ' + 'css-93ez2t')
    else:
        print(f'Błąd podczas pobierania strony. Kod odpowiedzi: {response.status_code}')

def getMainImage(url):
    response = requests.get(url)

    if(response.status_code ==200):
        soup = BeautifulSoup(response.text, "html.parser")


        mainImage = soup.find('div', {'class': 'swiper-zoom-container'})

        if mainImage:

            imgTag = soup.find('img')
            if imgTag:
                imgSrc = imgTag.get('src')
                return imgSrc

            else:
                print(f'Nie znaleziono tagu img w divie ')
        else:
            print(f'Nie znaleziono divów o klasie "swiper-zoom-container"')
    else:
        print(f'Błąd podczas pobierania strony. Kod odpowiedzi: {response.status_code}')

# def getLocation(url):
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, "html.parser")
#
#         finDiv = soup.find('div', {'class': 'css-13l8eec'})
#
#         if finDiv:
#             findLocation = finDiv.find_all('div')  # Use finDiv to narrow down the search
#             if findLocation:
#                 location = finDiv.find('p', {'class': 'css-1cju8pu er34gjf0'})
#
#                 print(location.text)  # Use 'location' instead of 'findLocation'
#                 return location.text
#             else:
#                 print("nie znaleziono lokalizacji p")
#         else:
#             print('nie znaleziono lokalizacji div')
#     else:
#         print(f'Błąd podczas przetwarzania strony {response.status_code}')




url = 'https://www.olx.pl/d/oferta/wynajme-mieszkanie-2-pokojowe-ul-folwarczna-poznan-CID3-IDXSAxb.html'








