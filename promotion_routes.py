from typing import List

from fastapi import APIRouter

from repos.promotion import PromotionRepository
from schemas.models import PromotionModel
from services.parser import parse_promotions
from services.producer import send_data

promotion_router = APIRouter(prefix="/api/v1/promotions", tags=["promotions"])


@promotion_router.get("/pull", response_model=List[PromotionModel])
async def pull_promotions() -> List[PromotionModel]:
    promotions = await parse_promotions()
    promotions["property"] = "pull"
    await send_data(promotions)
    await PromotionRepository.insert_many(promotions)
    promotions_list = await PromotionRepository.get_all()
    return promotions_list
