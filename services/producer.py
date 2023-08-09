import json
import logging

from aiokafka import AIOKafkaProducer

from config import app_settings


class AIOProducer:
    def __init__(self) -> None:
        self.producer: AIOKafkaProducer | None = None

    async def init_producer(self) -> None:
        self.producer = AIOKafkaProducer(
            bootstrap_servers=[app_settings.BOOTSTRAP_SERVER]
        )

    async def send_data(self, data: dict) -> None:
        await self.producer.send_and_wait(
            app_settings.KAFKA_TOPIC_NAME, json.dumps(data).encode("utf-8")
        )
        logging.info(data)

    async def start(self) -> None:
        await self.producer.start()

    async def stop(self) -> None:
        await self.producer.stop()


producer = AIOProducer()
