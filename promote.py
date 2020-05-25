import discord as disc
import asyncio
commands=["promote", "vote"]
voted_users = []
promoted_user = None
votes_req = 1
knights_id = 261940259263086592
knights_id = 714154460695232614 #test server


async def init(message: disc.Message):
    if not is_knight(message.author, message.guild):
        await reply(message, "you are not knighted and have no jurisdiction!")
        return
    words = message.content.split()
    first = words[0]
    if first == "promote":
        return await promote(words, message)
    if first == "vote":
        return vote(words, message)
    raise Exception("command"+first+" not found")


async def promote(words, message:disc.Message):
    global promoted_user
    global voted_users

    if len(words)>1:
        guild = message.guild
        reply(message, guild.roles)
        username = words[1]
        user = guild.get_member_named(username)
        if user is None:
            return username +" not a username "
        if is_knight(user, guild):
            return username +" is already knighted!"
        else:
            promoted_user = user
            voted_users = []
            return user.name + " up for promotion in "+guild.name
    else:
        return "missing arguments"


async def vote(words, message:disc.Message):
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
            return (message.author.name + " has last vote for "+ user.name+", and has been knighted!")
        return message.author.name + " votes for "+ user.name     
    else:
        return "missing arguments"

async def reply(message:disc.Message, text:str):
    await message.channel.send(text)

async def add_role(guild: disc.Guild, user:disc.Member, role_id = knights_id):
    role = guild.get_role(role_id)
    print("adding", role.name, "to", user.name)
    await user.add_roles(role)

    
def is_knight(user:disc.Member, guild):
    knight_role = guild.get_role(knights_id)
    if knight_role in user.roles:
        return True