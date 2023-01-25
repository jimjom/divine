import discord
import os
import random
from DealFinder import DealFinder
from dotenv import load_dotenv
import time

load_dotenv()

token = os.getenv('POE_SESSION_ID')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

async def findDealsLoop(dealFinder, timeout):
    while True:
        deals = dealFinder.findDeals()
        print(deals)
        time.sleep(timeout)

async def messageChannel(channelName, message):
    for channel in client.guilds[0].channels:
        if channel.name == channelName:
            await channel.send(message)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    dealFinder = DealFinder(client)
    await findDealsLoop(dealFinder,5) #TODO: Replace with 3600 for 1hr


#TODO: Respond to !help command
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        await message.channel.send('Yeah i bet you\'d like that wouldn\'t you (bitch)')

client.run(token)