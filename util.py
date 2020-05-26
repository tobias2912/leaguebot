import discord as disc


def tag(user:disc.User):
    """
    return string tagging user
    """
    return "<@" + str(user.id)+">"

