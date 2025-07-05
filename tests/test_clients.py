import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Tests unitaires pour Client

from fastapi.testclient import TestClient
from main import app
from dependencies import get_current_user

# Override de l'authentification pour les tests
class DummyUser:
    id = 1
    email = "admin@example.com"
    role = "admin"

def override_current_user():
    return DummyUser()

app.dependency_overrides[get_current_user] = override_current_user
client = TestClient(app)

def test_create_and_get_client():
    data = {"name": "Test Client", "email": "test@client.com", "phone": "0600000000"}
    response = client.post("/clients/", json=data)
    assert response.status_code == 200
    client_id = response.json()["id"]

    get_response = client.get(f"/clients/{client_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Test Client"

def test_update_client():
    data = {"name": "Client Update", "email": "update@client.com", "phone": "0600000001"}
    response = client.post("/clients/", json=data)
    assert response.status_code == 200
    client_id = response.json()["id"]

    update_data = {"name": "Client Updated"}
    update_response = client.put(f"/clients/{client_id}", json=update_data)
    assert update_response.status_code == 200
    assert update_response.json()["name"] == "Client Updated"

def test_delete_client():
    data = {"name": "Client Delete", "email": "delete@client.com", "phone": "0600000002"}
    response = client.post("/clients/", json=data)
    assert response.status_code == 200
    client_id = response.json()["id"]

    delete_response = client.delete(f"/clients/{client_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["ok"] is True
