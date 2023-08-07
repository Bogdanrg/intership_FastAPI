import pytest
from httpx import AsyncClient

from config import app_settings
from main import app


@pytest.mark.asyncio
async def test_pull() -> None:
    async with AsyncClient(app=app, base_url=app_settings.BASE_URL) as ac:
        response = await ac.get("/api/v1/promotions/pull")
    assert response.status_code == 200
    assert set(response.json()[0].keys()) == {"_id", "name", "price"}
