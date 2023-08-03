import bson
import pytest

from repos.promotion import PromotionRepository


@pytest.mark.asyncio
async def test_create_promotion(promotion_data):
    inserted_id = await PromotionRepository.create(promotion_data)
    document = await PromotionRepository.collection.find_one({"_id": inserted_id})
    assert type(inserted_id) == bson.objectid.ObjectId
    assert document["name"] == "BTC"


@pytest.mark.asyncio
async def test_get_all():
    documents = await PromotionRepository.get_all()
    assert type(documents) == list
    assert len(documents) > 0


@pytest.mark.asyncio
async def test_insert_many(promotions):
    PromotionRepository.collection.delete_many({})
    inserted_ids = await PromotionRepository.insert_many(promotions)
    assert inserted_ids == 2


@pytest.mark.asyncio
async def test_update(new_promotions):
    await PromotionRepository.update_one(new_promotions)
    documents = await PromotionRepository.get_all()
    for document in documents:
        del document["_id"]
    assert documents == new_promotions["result"]
