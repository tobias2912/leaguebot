# bot.py
import os
import discord
from dotenv import load_dotenv
import builds
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
    svar = builds.init(message.content)
    await message.channel.send(svar)

client.run(token)
