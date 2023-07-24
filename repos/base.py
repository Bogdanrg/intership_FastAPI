from typing import Generic, TypeVar

T = TypeVar('T')


class BaseRepository:
    collection = Generic[T]

    @classmethod
    async def create(cls, promotion: dict) -> str:
        new_promotion = await cls.collection.insert_one(promotion)
        return new_promotion.inserted_id
