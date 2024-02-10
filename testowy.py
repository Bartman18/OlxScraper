import requests
from bs4 import BeautifulSoup
import time
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime, timedelta

def webhookSend(new_id,new_href, data, price, new_img,data_location):
    Url = 'https://discord.com/api/webhooks/1204433421640929381/8I9EohsWf2o_7aD1CZiSuumHYu2coAM-Xtm6tua9QjHbZvmV0EADM0BWiBS-88qBi5SC'
    webhook = DiscordWebhook(url=Url)
    img = new_img
    id_new = new_id
    href = new_href
    truncated_description = ""
    remaining_description = ""
    remaing = False


    if getDescription(href):
        descripton = getDescription(href)
        if descripton:
            character_count = len(descripton)
            if character_count > 1024:
                truncated_description = descripton[:1024]


                remaining_description = descripton[1024:]
                remaing = True
            else:
                truncated_description = descripton


    embed = DiscordEmbed(title="Nowa oferta",description=data,color=0x03b2f8)



    embed.add_embed_field(name="Location", value=data_location)
    embed.add_embed_field(name="Price", value=price)
    embed.add_embed_field(name="ID", value=id_new)
    embed.add_embed_field(name="Description", value=truncated_description)
    if remaing:
        embed.add_embed_field(name=None,value=remaining_description)


    embed.add_embed_field(name="link", value=f"[Click Here]({href})", inline=False)
    embed.set_image(url=img)







    webhook.add_embed(embed)

    response = webhook.execute()

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
        img_src = element.find('img', src=True).get('src') if element.find('img', src=True) else None
        special_product = element.find('div', {'class': 'css-1jh69qu'})
        price_detail = element.find('div',{'class': 'css-u2ayx9'})

        if price_detail:
            price = price_detail.find('p').text



        data_element = element.find('div', {'class': 'css-odp1qd'})
        if data_element:
            data = data_element.find('p')

            if data:
                data_text = data.get_text(strip=True)
                data_split = data_text.split('-')

                if len(data_split) > 1:
                    data_result = data_split[1].strip()
                    data_location = data_split[0].strip()
                    if data_result:
                        data_result = getTime(data_result)
                else:
                    data_result = "Error: Data not in the expected format"
            else:
                data_result = "Error: No 'p' element found inside 'css-odp1qd' class"
        else:
            data_result = "Error: No 'css-odp1qd' class found"

        if element_id and data_element and element_href and img_src and not special_product:
            id_href_map[element_id] = (element_href, img_src, data_result, price, data_location)

    return id_href_map

def getTime(data_results):
    if data_results:
        data_split = data_results.split('o ')
        if len(data_split) > 1:
            leftWords = data_split[0].strip()
            timeString = data_split[1].strip()
            try:
                current_time = datetime.strptime(timeString, "%H:%M")
                add_hour = current_time + timedelta(hours=1)

                # Convert add_hour back to string
                add_hour_str = add_hour.strftime("%H:%M")

                # Concatenate leftWords and add_hour_str
                data_results = f"{leftWords}o {add_hour_str}"

            except ValueError as e:
                print(f"Error parsing timeString: {timeString}")
                print(e)
    return data_results







def getPhotoFromOlx(new_img, new_href):

    if new_img.startswith('/app'):
        photoResponse = requests.get(new_href)
        soup = BeautifulSoup(photoResponse.text, "html.parser")
        findClass = soup.find('div', {'class': 'swiper-zoom-container'})

        if findClass:
            photo = findClass.find('img', src=True).get('src') if soup.find('img', src=True) else None

            new_img = photo
            return new_img
    else:
        return new_img
def getPhotoFromOtodom(new_img, new_href):
    if new_img.startswith('/app'):
        response = requests.get(new_href)
        if ( response.status_code == 200 ) :
            soup = BeautifulSoup(response.text, "html.parser")
            if soup:
                string = str(soup)
                if string:
                    index = string.find("large")
                    if index:


                        sliced = string[index + 8:]

                        index_end = sliced.find('"')

                        result = sliced[:index_end]
                        print(result)
                else:
                    print('nie znaleziono main')


def getDescription(new_href):

    response = requests.get(new_href)
    soup = BeautifulSoup(response.text,"html.parser")
    if new_href.startswith('https://www.olx.pl/'):
        if soup:
            getDiv = soup.find('div',{'class':'css-1m8mzwg'})
            if getDiv:
                getData = getDiv.find('div',{'class':'css-1t507yq er34gjf0'})

                return getData.text
    elif new_href.startswith('https://www.otodom.pl'):
        if soup:
            getDiv = soup.find('div',{'class': 'css-1ugtzj2 e175i4j93'})
            if getDiv:
                getData = getDiv.find('div', {'class': 'css-1wekrze e1lbnp621'})

                return getData.text


def MonitorMode(url):
    all_cards = []

    while True:
        print('waiting')
        time.sleep(30)

        soup = getHtmlcode(url)

        new_href_map = getElementId(soup)

        for new_id, (new_href, new_img,data, price, data_location) in new_href_map.items():
            if new_id not in all_cards:
                if new_href.startswith("/d/"):
                    new_href = "https://www.olx.pl" + new_href


                if new_img.startswith('/app'):
                    if new_href.startswith('https://www.olx'):

                        new_img = getPhotoFromOlx(new_img, new_href)
                    elif new_href.startswith('https://www.otodom.pl'):
                        new_img = getPhotoFromOlx(new_img,new_href)







                all_cards.append(new_id)
                webhookSend(new_id, new_href, data, price, new_img, data_location)



url = 'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/q-wynajem-mieszkania/?search%5Border%5D=created_at%3Adesc#895856146'
MonitorMode(url)



