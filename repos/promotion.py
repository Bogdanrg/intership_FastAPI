from core.database import db


class PromotionRepository:
    collection = db["trading"]

    @classmethod
    async def create(cls, promotion: dict) -> str:
        new_promotion = await cls.collection.insert_one(promotion)
        return new_promotion.inserted_id
