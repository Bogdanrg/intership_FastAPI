import asyncio

import kafka.errors
import pytest
from httpx import AsyncClient

from config import app_settings
from main import app
from services.producer import producer


@pytest.mark.asyncio
async def test_pull() -> None:
    try:
        async with AsyncClient(app=app, base_url=app_settings.BASE_URL) as ac:
            await producer.init_producer()
            await producer.start()
            response = await ac.get("/api/v1/promotions/pull")
        assert response.status_code == 200
        assert set(response.json()[0].keys()) == {"_id", "name", "price"}
        await producer.stop()
    except kafka.errors.KafkaConnectionError:
        await asyncio.sleep(5)
