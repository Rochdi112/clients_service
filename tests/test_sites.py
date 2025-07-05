import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Tests unitaires pour Site

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_dummy_site():
    assert True

def test_create_and_get_site():
    token = "testtoken"
    headers = {"Authorization": f"Bearer {token}"}
    # Créer un client d'abord
    client_data = {"name": "Test Client", "email": "test@client.com", "phone": "0600000000"}
    client_resp = client.post("/clients/", json=client_data, headers=headers)
    client_id = client_resp.json()["id"]
    site_data = {"name": "Site 1", "address": "123 rue Maroc", "client_id": client_id}
    response = client.post("/sites/", json=site_data, headers=headers)
    assert response.status_code == 200
    site_id = response.json()["id"]
    get_response = client.get(f"/sites/{site_id}", headers=headers)
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Site 1"
