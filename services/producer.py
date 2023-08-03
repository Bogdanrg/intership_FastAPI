import json
from config import app_settings

from aiokafka import AIOKafkaProducer


async def send_data(data: dict) -> None:
    producer = AIOKafkaProducer(bootstrap_servers=[app_settings.BOOTSTRAP_SERVER])
    await producer.start()
    try:
        await producer.send_and_wait(
            app_settings.KAFKA_TOPIC_NAME, json.dumps(data).encode("utf-8")
        )
    finally:
        await producer.stop()
