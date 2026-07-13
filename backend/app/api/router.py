from fastapi import APIRouter

from backend.app.modules.system.router import router as system_router
from backend.app.modules.users.router import router as users_router

api_router = APIRouter()
api_router.include_router(system_router)
api_router.include_router(users_router)
