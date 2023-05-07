import os

from dotenv import find_dotenv, load_dotenv
from pydantic import BaseSettings


class _Settings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class ModelSettings(_Settings):
    load_dotenv()

    API_NAME = "HOROSCOPE_API"
    API_VERSION = "0.1.0"

    # MODEL
    MODEL_PATH: str = os.getenv("MODEL_PATH", "models/horoscope")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "ai-forever/rugpt3small_based_on_gpt2")
    DEVICE: str = os.getenv("DEVICE", "cpu")
    SEQUENCE_LENGTH: int = os.getenv("SEQUENCE_LENGTH", 500)
    MODEL_TEMPERATURE: float = os.getenv("MODEL_TEMPERATURE", 0.95)


def get_settings():
    return ModelSettings(_env_file=".env")


settings: ModelSettings = get_settings()
