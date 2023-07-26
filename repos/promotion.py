from core.database import db

from .base import BaseRepository


class PromotionRepository(BaseRepository):
    collection = db["trading"]

    @classmethod
    async def update_all(cls, promotions: dict) -> None:
        for promotion in promotions["result"]:
            await cls.collection.update_one(
                {"code": promotion["code"]}, {"$set": promotion}
            )

    @classmethod
    async def create_all(cls, promotions: dict) -> int:
        result = await cls.collection.insert_many(
            [promotion for promotion in promotions["result"]]
        )
        return len(result.inserted_ids)
