import pytest
from httpx import AsyncClient
from ..main import app

@pytest.mark.asyncio
async def test_create_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/clients", json={
            "nom": "Société ABC",
            "email": "contact@abc.com",
            "telephone": "0612345678"
        })
        assert response.status_code == 200
        data = response.json()
        assert data["email"] == "contact@abc.com"
