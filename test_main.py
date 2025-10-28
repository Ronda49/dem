from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FakeDB API"}

def test_get_user_success():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Alice", "age": 25}

def test_get_user_not_found():
    response = client.get("/users/99")
    assert response.status_code == 404

def test_add_user():
    response = client.post("/users/3", json={"name": "Charlie", "age": 22})
    assert response.status_code == 200
    assert response.json()["message"] == "User added successfully"
