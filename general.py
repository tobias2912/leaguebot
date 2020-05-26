import discord as disc
from util import *
commands = ["highfive"]

async def init(msg):
    print(get_cmd(msg))
    user:disc.Member = msg.guild.get_member_named(get_args(msg))
    if user is None:
        return "highfive who?"
    if get_cmd(msg) == "highfive":
        out = f"{msg.author.name} high fives {tag(user)}!"
        await msg.delete()
        return out
    return ""

