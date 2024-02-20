# bot.py
import os
import discord
import json
from dotenv import load_dotenv
from poelib import poelib
from alva import Alva

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

        hotbots_guid = os.getenv('HOT_BOTS_GUID')
        hotbots = client.get_channel(hotbots_guid) or await client.fetch_channel(hotbots_guid)

        requestData = None
        with open('queries/q1.txt') as f:
            requestData = json.load(f)
        
        self._tradeBot = poelib(bot_channel=hotbots)
        self._tradeBot.query("q1", requestData)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content[0] == '!':

            command = message.content[1:].split(' ')[0]
            parameter = ' '.join(message.content[1:].split(' ')[1:])
            
            if(command == 'extract'):
                response = poelib.extractOil(parameter)
                await message.channel.send(response)

            if(command == 'alva'):
                alva = Alva()
                await message.channel.send(alva.run())

            if(command =='UwU'):
                await message.channel.send("Weebs are a scourge upon the earth and one day a reckoning will come.")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
