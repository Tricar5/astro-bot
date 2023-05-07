from fastapi import FastAPI

from horoscoper.config import settings
from horoscoper.endpoints import api_router


__all__ = ["app"]


def create_app() -> FastAPI:
    application = FastAPI(
        title=settings.API_NAME,
        description="Сервис API для генерации гороскопа",
        docs_url="/docs",
        openapi_url="/openapi",
        version=settings.API_NAME,
    )
    print(settings.MODEL_PATH)

    application.include_router(api_router)
    return application


app: FastAPI = create_app()
