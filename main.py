from fastapi import FastAPI
import uvicorn
from app.core import wiki, wiki_search, wiki_phrases

api = FastAPI()


@api.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki"}


@api.get("/search/{value}")
async def search(value: str):
    """Page to search on wikipedia"""

    results = wiki_search(value)
    return {"results": results}


@api.get("/wiki/{name}")
async def wiki_page(name: str):
    """Retrive wiki page"""

    result = wiki(name)
    return {"result": result}


@api.get("/phrases/{name}")
async def phrases(name: str):
    """Retrive wiki page and return phrases"""

    result = wiki_phrases(name)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(api, port=8080, host="0.0.0.0")
