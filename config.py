from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_TITLE: str
    MONGO_INITDB_DATABASE: str
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str
    MONGODB_URL: str
    API_KEY: str
    CODES: str
    ALPHAVANTAGE_URL: str
    ZOOKEEPER_CLIENT_PORT: int
    ZOOKEEPER_TICK_TIME: int
    KAFKA_BROKER_ID: int
    KAFKA_ZOOKEEPER_CONNECT: str
    KAFKA_ADVERTISED_LISTENERS: str
    KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: str
    KAFKA_INTER_BROKER_LISTENER_NAME: str
    KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: int
    KAFKA_TOPIC_NAME: str
    BOOTSTRAP_SERVER: str
    CELERY_BROKER_URL: str
    UVICORN_HOST: str
    UVICORN_PORT: int

    model_config = SettingsConfigDict(env_file=".env")


app_settings = Settings()
