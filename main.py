from fastapi import FastAPI

from config import app_settings
from promotion_routes import promotion_router
from services.producer import producer

app = FastAPI(title=app_settings.APP_TITLE)


@app.on_event("startup")
async def startup_event() -> None:
    await producer.init_producer()
    await producer.start()


@app.on_event("shutdown")
async def shutdown_event() -> None:
    await producer.stop()


app.include_router(promotion_router)
