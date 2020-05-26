# bot.py
import os

import discord
from dotenv import load_dotenv

import builds
import general
import promote
modules = [builds, general, promote]


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(' has connected to Discord!')

@client.event
async def on_message(message: discord.Message):
    """
    based on first word, send message to correct function
    """
    if message.author == client.user:
        return
    words = message.content.split()
    first = words[0]

    if first in builds.commands:
        svar = builds.init(message)
        if svar != "":
            await message.channel.send(svar)
    if first in general.commands:
        svar = await general.init(message)
        await message.channel.send(svar)
    if first in promote.commands:
        svar = await promote.init(message)
        if svar is not None and svar != "":
            await message.channel.send(svar)

    if first == "!help":
        all_commands = "".join([str(x.commands) for x in modules])
        await message.channel.send(all_commands)



client.run(token)
