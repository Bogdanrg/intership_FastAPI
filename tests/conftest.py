import asyncio

import pytest


@pytest.fixture()
def promotion_data():
    promotion = {
        "name": "BTC",
        "price": 2900.01
    }
    yield promotion
    del promotion


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture()
def promotions():
    promotions = {"result": [
        {
            "name": "BTC",
            "price": 2900.01
        },
        {
            "name": "ETH",
            "price": 800
        }
    ]
    }
    yield promotions
    del promotions


@pytest.fixture()
def new_promotions():
    promotions = {"result": [
        {
            "name": "BTC",
            "price": 2200
        },
        {
            "name": "ETH",
            "price": 200
        }
    ]}
    yield promotions
    del promotions
