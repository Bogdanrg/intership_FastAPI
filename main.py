from fastapi import FastAPI

from config import app_settings
from promotion_routes import promotion_router

app = FastAPI(title=app_settings.APP_TITLE)


app.include_router(promotion_router)
