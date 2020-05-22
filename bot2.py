# bot.py
import os
import discord
from dotenv import load_dotenv
#import builds
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

print(token)
client = discord.Client()
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run(token)