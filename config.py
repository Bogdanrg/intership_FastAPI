import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    API_KEY: str = os.getenv("API_KEY", "")
    MONGODB_URL: str = os.getenv("MONGODB_URL", "")
    MONGO_INITDB_DATABASE: str = os.getenv("MONGO_INITDB_DATABASE", "")
    APP_TITLE: str = os.getenv("APP_TITLE", "")
    ALPHAVANTAGE_URL: str = os.getenv("ALPHAVANTAGE_URL", "")
    CODES: str = os.getenv("CODES", "")
    KAFKA_TOPIC_NAME: str = os.getenv("KAFKA_TOPIC_NAME", "")
    BOOTSTRAP_SERVER: str = os.getenv("BOOTSTRAP_SERVER", "")


app_settings = Settings()
