from httpx import AsyncClient

from config import app_settings

API_KEY = app_settings.API_KEY


async def parse_promotions() -> dict:
    codes = (code for code in app_settings.CODES.split(","))
    promotions: dict = {"result": []}
    for code in codes:
        async with AsyncClient() as client:
            response = await client.get(f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
                                        f'&from_currency'
                                        f'={code}&to_currency=USD&apikey={API_KEY}')
            if response.json().get('Realtime Currency Exchange Rate', None):
                promotion = {
                    'code': response.json()['1. From_Currency Code'],
                    'price': response.json()['8. Bid Price']
                }
                promotions['result'].append(promotion)
    return promotions
