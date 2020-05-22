# bot.py
import os

import discord
from dotenv import load_dotenv

import builds
import general
import promote

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    words = message.content.split()
    first = words[0]
    if first in builds.commands:
        svar = builds.init(message.content)
        if svar != "":
            await message.channel.send(svar)
    if first in general.commands:
        svar = general.init(message)
        await message.channel.send(svar)
    if first in promote.commands:
        svar = promote.init(message)
        await message.channel.send(svar)

client.run(token)
