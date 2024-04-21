import wikipedia


def wiki(name="War Goddess", length=1):
    """Fetching details from wiki page"""

    this_wiki = wikipedia.summary(name, length)
    return this_wiki


def wiki_search(name):
    "Search Wikipedia for name"

    results = wikipedia.search(name)
    return results
