from typing import Final
from discord import Intents, Client, Message
import discord
from discord import Embed
import olx
TOKEN = 'MTIwMjczOTI5MzIzMjE3NzIwMg.Gdok5x.P1N1hmB06GfEVOr-eUapFL9sXx02i_JE6TyPk8'

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

async def send_message(message: Message, url: str) -> None:
    if not url:
        print('message was empty')
        return

    if is_private := url[0] == '?':
        user_message = url[1:]

    try:

        price = olx.getPrice(url)

        pic_url = olx.getProductImage(url)

        embed = Embed(title="Mieszkanie" == url, description="Dostępność produktów:")

        # Dodawanie informacji o dostępności każdego produktu do wbudowanej wiadomości

        embed.add_field(name="price", value=price)


        # Dodanie obrazka do wbudowanej wiadomości
        embed.set_image(url=pic_url)


        await message.channel.send(embed=embed) if is_private else await message.channel.send(embed=embed)
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running')


@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    if message.content.startswith('!olx'):
        link = message.content.split()[1]
        print(link)

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, link)

def runBot() -> None:
    client.run(token=TOKEN)
