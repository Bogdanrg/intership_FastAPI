import asyncio
import json
import logging

from aiokafka import AIOKafkaProducer

from config import app_settings

loop = asyncio.get_event_loop()
producer = AIOKafkaProducer(
    loop=loop, bootstrap_servers=[app_settings.BOOTSTRAP_SERVER]
)


async def send_data(data: dict) -> None:
    await producer.send_and_wait(
        app_settings.KAFKA_TOPIC_NAME, json.dumps(data).encode("utf-8")
    )
    logging.info(data)
