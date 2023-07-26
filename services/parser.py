from httpx import AsyncClient

from config import app_settings

API_KEY = app_settings.API_KEY


async def parse_promotions() -> dict:
    codes = (code for code in app_settings.CODES.split(","))
    promotions: dict = {"result": []}
    for code in codes:
        async with AsyncClient() as client:
            response = await client.get(
                url=app_settings.ALPHAVANTAGE_URL.format(code=code, apikey=API_KEY)
            )
            if response.json().get("Realtime Currency Exchange Rate", None):
                promotion = {
                    "code": response.json()["Realtime Currency Exchange Rate"][
                        "1. From_Currency Code"
                    ],
                    "price": response.json()["Realtime Currency Exchange Rate"][
                        "8. Bid Price"
                    ],
                }
                promotions["result"].append(promotion)
    return promotions
