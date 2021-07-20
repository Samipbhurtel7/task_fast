import json
from fastapi.testclient import TestClient
from application.database import Base, engine
from application.app import  app

Base.metadata.create_all(bind=engine)

client = TestClient(app)

dummy = {
    "id": "001",
    "address": "http://example.com",
    "author": {
        "id": "A001",
        "username": "string"
    },
    "created": "2021-07-20T04:26:41.751Z",
    "counters": {
        "A": 3,
        "B": 2,
    }
}


def test_post_error_article():
    response = client.post("/article")
    assert response.status_code == 422

def test_post_article():
    response = client.post("/article", json=dummy)
    assert response.status_code == 200

def test_get_articles():
    response = client.get("/articles")
    articles = response.json()
    assert len(articles) == 1
    assert response.status_code == 200

def test_get_article():
    response = client.get("/article/001")
    article = response.json()
    assert article.get("path") == dummy.get("address")
    assert response.status_code == 200

def test_update_article():
    dummy["address"] = "http://newexample.com"
    response = client.put("/article/001", json=dummy)
    assert response.status_code == 200

def test_delete_article():
    response = client.delete("/article/002")
    assert response.status_code == 200
