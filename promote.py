import discord
commands=["promote", "vote"]
vote_counter = 0
promoted_user = None
def init(message: discord.Message):
    words = message.content.split()
    first = words[0]
    if first == "promote":
        return promote(words, message)
    if first == "vote":
        return vote(words, message)
    return ""


def promote(words, message):
    if len(words)>1:
        guild = message.guild
        username = words[1]
        user = guild.get_member_named(username)
        if user is not None:
            return user.name + " up for promotion in "+guild.name
        else:
            return username +" not a username "
    else:
        return "missing arguments"

def vote(words, message):
    if len(words)>1:
        guild = message.guild
        username = words[1]
        user = guild.get_member_named(username)
        if user is not None:
            return message.author.name + " votes for "+ user.name
        else:
            return username +" not a username "
    else:
        return "missing arguments"
