"""Config settings file"""
import os
from functools import lru_cache
from pydantic import BaseSettings
from dotenv import load_dotenv, find_dotenv

__all__ = ["settings"]


class _Settings(BaseSettings):

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class BotSettings(BaseSettings):

    BOT_NAME: str = "AstroGPTBot"
    BOT_VERSION: str = "0.1.0"

    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "DEBUG")
    TOKEN: str = os.getenv("TELEGRAM_TOKEN")


@lru_cache(maxsize=1)
def get_settings():
    return BotSettings(_env_file=find_dotenv('.env'))


settings: BotSettings = get_settings()