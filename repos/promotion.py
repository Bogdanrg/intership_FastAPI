from core.database import db

from .base import BaseRepository


class PromotionRepository(BaseRepository):
    collection = db["trading"]

    @classmethod
    async def update_one(cls, promotions: dict) -> None:
        for promotion in promotions["result"]:
            await cls.collection.update_one(
                {"name": promotion["name"]}, {"$set": promotion}
            )

    @classmethod
    async def insert_many(cls, promotions: dict) -> int:
        result = await cls.collection.insert_many(
            [promotion for promotion in promotions["result"]]
        )
        return len(result.inserted_ids)
