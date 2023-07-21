import os

from dotenv import load_dotenv
from fastapi import FastAPI

from core.database import db
from promotion_routes import promotion_router

load_dotenv()

app = FastAPI(title=os.getenv("APP_TITLE"))


@app.get("/")
async def hello() -> str:
    new_secret = await db["trading"].insert_one({"promotion": "Bitcoin"})
    return f"{new_secret.inserted_id}"


app.include_router(promotion_router)
