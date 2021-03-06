import discord as disc
from util import *
import asyncio
import random
commands=["promote", "vote"]
voted_users = []
promoted_user = None
votes_req = 3
knights_id = 261940259263086592
knights_id = 714154460695232614 #test server


async def init(msg: disc.message):
    """
    users with correct role id can add others to role by promote and vote
    """
    if not is_knight(msg.author, msg.guild):
        await reply(msg, "you are not knighted and have no jurisdiction!")
        return

    first = get_cmd(msg)
    if first == "promote":
        return await promote(msg)
    if first == "vote":
        return await vote(msg)
    raise Exception("command"+first+" not found")


async def promote(msg:disc.message):
    global promoted_user
    global voted_users

    if get_args!="":
        username = get_args(msg)
        guild = msg.guild
        user = guild.get_member_named(username)
        if user is None:
            return username +" not a username "
        if is_knight(user, guild):
            return username +" is already knighted!"
        if user == promoted_user:
            return "username is already up for promotion, type vote to support him"
        else:
            promoted_user = user
            voted_users = []
            await reply(msg, tag(user) + " has been selected for the Knighting Ceremony!")
            await reply(msg, str(votes_req)+" votes from different knights are required to proceed!")
    else:
        return "missing arguments"


async def vote(msg:disc.message):
    global promoted_user
    if get_args != "":
        guild = msg.guild
        username = get_args(msg)
        user = guild.get_member_named(username)
        if user is None:
            return username +" not a username "
        if promoted_user is None:
            return "no user up for promotion"
        if user != promoted_user:
            return username +" is not the selected user"
        if msg.author in voted_users:
            return msg.author.display_name +" has already voted"
        voted_users.append(msg.author)
        if len(voted_users)>= votes_req:
            await add_role(guild, user)
            promoted_user = None
            voted_users.clear()
            return f"{msg.author.name} has last vote for {tag(user)}, and he shall been knighted!"
        
        return get_praise(msg.author, promoted_user) + f" ({len(voted_users)}/{votes_req} votes)"     
    else:
        return "missing arguments"


def get_praise(voter:disc.User, promoted:disc.User):
    """returns str with some nice words"""
    strings = [f"{voter.name} votes for {tag(promoted)}'s courage", f"{voter.name} thinks {tag(promoted)} would be devoted to the church",
    f"{voter.name} votes for {tag(promoted)}, as he would be loyal to his lord", f"{voter.name} says {tag(promoted)} would never avoid dangerous paths out of fear."]
    return random.choice(strings)


async def reply(msg:disc.message, text:str):
    await msg.channel.send(text)


async def add_role(guild: disc.Guild, user:disc.Member, role_id = knights_id):
    role = guild.get_role(role_id)
    print("adding", role.name, "to", user.name)
    await user.add_roles(role)

    
def is_knight(user:disc.Member, guild):
    knight_role = guild.get_role(knights_id)
    if knight_role in user.roles:
        return True