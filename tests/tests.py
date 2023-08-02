import pytest
from httpx import AsyncClient

from main import app


@pytest.mark.anyio
async def test_root() -> None:
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8080") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == "2"
