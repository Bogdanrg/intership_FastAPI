import asyncio

from celery import Celery
from celery.schedules import crontab

from config import app_settings
from repos.promotion import PromotionRepository
from services.parser import parse_promotions
from services.producer import producer

app = Celery(__name__)
app.conf.broker_url = app_settings.CELERY_BROKER_URL
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "update-promotions-every-minute": {
        "task": "run_update_promotions",
        "schedule": crontab(minute="*/1"),
    }
}

app.conf.timezone = "UTC"


@app.task(name="run_update_promotions")
def run_update_promotions() -> None:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(update_promotions())


async def update_promotions() -> None:
    await producer.init_producer()
    await producer.start()
    promotions = await parse_promotions()
    promotions["action"] = "rate_update"
    await producer.send_data(promotions)
    await PromotionRepository.update_one(promotions)
