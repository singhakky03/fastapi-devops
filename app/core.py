import wikipedia


def wiki(name="War Goddess", length=1):
    """Fetching details from wiki page"""

    this_wiki = wikipedia.summary(name, length)
    return this_wiki
