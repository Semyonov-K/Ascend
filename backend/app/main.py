from fastapi import FastAPI

from backend.app.api.router import api_router
from backend.app.core.config import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    new_app = FastAPI(title=settings.app_name, debug=settings.debug)
    new_app.include_router(api_router)
    return new_app


app = create_app()
