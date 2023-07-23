from requests import get

from config import app_settings
from repos.promotion import PromotionRepository

API_KEY = app_settings.API_KEY


async def parse_promotions() -> dict:
    codes = (code for code in app_settings.CODES.split(","))
    response_data: dict = {"result": []}
    for code in codes:
        response = get(
            url=app_settings.ALPHAVANTAGE_URL.format(code=code, apikey=API_KEY)
        )
        if response.json().get("Realtime Currency Exchange Rate"):
            await PromotionRepository.create(
                response.json()["Realtime Currency Exchange Rate"]
            )
        response_data["result"].append(response.json())
    return response_data
