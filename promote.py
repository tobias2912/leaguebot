import discord
import asyncio
commands=["promote", "vote"]
voted_users = []
promoted_user = None
votes_req = 1
knights_id = 261940259263086592


def init(message: discord.Message):
    words = message.content.split()
    first = words[0]
    if first == "promote":
        return promote(words, message)
    if first == "vote":
        return vote(words, message)
    return ""


def promote(words, message):
    global promoted_user
    global voted_users
    if len(words)>1:
        guild = message.guild
        username = words[1]
        user = guild.get_member_named(username)
        if user is not None:
            promoted_user = user
            voted_users = []
            return user.name + " up for promotion in "+guild.name
        else:
            return username +" not a username "
    else:
        return "missing arguments"

def vote(words, message):
    global promoted_user
    if len(words)>1:
        guild = message.guild
        username = words[1]
        user = guild.get_member_named(username)
        if user is None:
            return username +" not a username "
        if promoted_user is None:
            return "no user up for promotion"
        if user != promoted_user:
            return username +" is not the selected user"
        if message.author in voted_users:
            return message.author.display_name +" has already voted"
        voted_users.append(message.author)
        if len(voted_users)>= votes_req:
            add_role(guild, user)
            reply(message, message.author.name + " has last vote for "+ user.name)
            return ""
        return message.author.name + " votes for "+ user.name     
    else:
        return "missing arguments"

def reply(message, text):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(message.channel.send(text))
    loop.close()

def add_role(guild: discord.Guild, user:discord.Member, role_id = knights_id):
    role = guild.get_role(id)
    print("adding", role.name, "to", user.name)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(user.add_roles(role))
    loop.close()
    