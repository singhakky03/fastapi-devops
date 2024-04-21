import wikipedia
from textblob import TextBlob


def wiki(name="War Goddess", length=1):
    """Fetching details from wiki page"""

    this_wiki = wikipedia.summary(name, length)
    return this_wiki


def wiki_search(name):
    "Search Wikipedia for name"

    results = wikipedia.search(name)
    return results


def wiki_phrases(name):
    """Return phrases from wikipedia"""

    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
