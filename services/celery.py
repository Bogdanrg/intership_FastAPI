import asyncio

from celery import Celery
from celery.schedules import crontab

from config import app_settings
from repos.promotion import PromotionRepository
from services.parser import parse_promotions
from services.producer import send_data

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
    asyncio.run(update_promotions())


async def update_promotions() -> None:
    promotions = await parse_promotions()
    await send_data(promotions)
    await PromotionRepository.update_all(promotions)
