import requests
from bs4 import BeautifulSoup



def pobierz_zawartosc_wszystkich_div(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        divy = soup.find_all('li', {'class': 'css-1r0si1e'})

        if divy:
            # Iteruj przez wszystkie znalezione divy
            for index, div_content in enumerate(divy):
                print(f'Zawartość diva {index + 1}: {div_content.text}')
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









