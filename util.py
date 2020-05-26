import discord as disc


def tag(user:disc.User):
    """
    return string tagging user
    """
    return "<@" + str(user.id)+">"

def get_args(msg:disc.Message):

    """
    returns characters after first space (arguments) from a message
    can return empty string
    """
    return " ".join(msg.content.split(" ")[1:])

def get_cmd(msg:disc.Message):
    """
    get first word in a message
    """
    return msg.content.split(" ")[0]





