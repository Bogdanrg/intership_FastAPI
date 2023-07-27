from typing import TypeVar

from core.database import db

T = TypeVar("T")


class BaseRepository:
    collection: db

    @classmethod
    async def create(cls, promotion: dict) -> str:
        new_promotion = await cls.collection.insert_one(promotion)
        return new_promotion.inserted_id

    @classmethod
    async def get_all(cls) -> list:
        promotions = cls.collection.find()
        promotion_list = await promotions.to_list(1000)
        return promotion_list
