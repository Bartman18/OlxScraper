
from discord import Intents, Client, Message
from discord import Embed
import olx
TOKEN = 'Insert your discord bot token'

intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

async def send_message(message: Message, url: str) -> None:
    if not url:
        print('message was empty')
        return

    try:
        price = olx.getPrice(url)
        pic_url = olx.getMainImage(url)
        details = olx.getDetails(url)

        embed = Embed(title="Mieszkanie", description=f"[Click here for more details]({url})")

        # Dodawanie informacji o dostępności każdego produktu do wbudowanej wiadomości
        embed.add_field(name="price", value=price)

        for detail in details:
            # Check if the split operation is successful
            if ': ' in detail:
                key, val = detail.split(': ', 1)  # Split each detail into key and value
                embed.add_field(name=key, value=val)
            else:
                # If split fails, set a default value for val
                embed.add_field(name="Unknown Detail", value=detail)

        # Dodanie obrazka do wbudowanej wiadomości
        embed.set_image(url=pic_url)

        await message.channel.send(embed=embed)
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
        link = message.content.split()[1] if len(message.content.split()) > 1 else None
        print(link)
        await send_message(message, link)

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')

def runBot() -> None:
    try:
        client.run(token=TOKEN)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

runBot()
