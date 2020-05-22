commands=["highfive"]

def init(message):
    words = message.content.split()
    if words[0] == "highfive":
        if len(words)>1:
            out = message.author.name + " high fives " + words[1]+"!"
            return out
    return ""
