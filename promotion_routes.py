from fastapi import APIRouter

from services.parser import parse_promotions
from services.producer import send_data

promotion_router = APIRouter(prefix="/api/v1/promotions", tags=["promotions"])


@promotion_router.get("/pull")
async def pull_promotions() -> dict:
    response = await parse_promotions()
    await send_data(response)
    return response
