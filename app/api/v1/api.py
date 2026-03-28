from fastapi import APIRouter
from app.api.v1.endpoints import times

api_router = APIRouter()

api_router.include_router(times.router)
