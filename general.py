import discord as disc
import util
commands=["highfive"]

def init(message):
    words = message.content.split()
    user:disc.Member = message.guild.get_member_named(words[1])
    if user is None:
        return "highfive who?"
    if words[0] == "highfive":
        if len(words)>1:
            out = message.author.name + " high fives "+util.tag(user)+ "!"
            return out
    return ""

