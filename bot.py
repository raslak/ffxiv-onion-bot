import os

import discord
from dotenv import load_dotenv

from market import find_cheapest_onion


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.content == '/onion':
        response = find_cheapest_onion()
        await message.channel.send(response)


client.run(TOKEN)