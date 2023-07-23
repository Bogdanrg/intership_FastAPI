import motor.motor_asyncio

from config import app_settings

MONGODB_URL = app_settings.MONGODB_URL

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client[app_settings.MONGO_INITDB_DATABASE]
