import pytest
from httpx import AsyncClient
from ..main import app

@pytest.mark.asyncio
async def test_create_site():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        await ac.post("/clients", json={
            "nom": "Client X",
            "email": "x@example.com",
            "telephone": "0600000000"
        })
        response = await ac.post("/sites", json={
            "nom": "Site A",
            "adresse": "Rue Alpha",
            "client_id": 1
        })
        assert response.status_code == 200
        assert response.json()["nom"] == "Site A"
