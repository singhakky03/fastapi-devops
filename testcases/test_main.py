from fastapi.testclient import TestClient
from main import api

client = TestClient(api)

def test_root_page():
    response =  client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API. Call /search or /wiki"}

def test_read_phrase():
    response = client.get("/phrases/tendulkar")
    assert response.status_code == 200
    assert response.json() == {"result":["sachin tendulkar","[ sətɕin teːɳɖulkəɾ ]","april","international cricketer","indian national team"]}

