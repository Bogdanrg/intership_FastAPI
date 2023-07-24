from fastapi import APIRouter

from services.parser import parse_promotions
from repos.promotion import PromotionRepository
from services.producer import send_data

promotion_router = APIRouter(prefix="/api/v1/promotions", tags=["promotions"])


@promotion_router.get("/pull")
async def pull_promotions() -> dict:
    promotions = await parse_promotions()
    await PromotionRepository.create_all(promotions)
    await send_data(promotions)
    return promotions


@promotion_router.get("/update")
async def update_promotions() -> dict:
    promotions = await parse_promotions()
    await PromotionRepository.update_all(promotions)
    await send_data(promotions)
    return promotions
