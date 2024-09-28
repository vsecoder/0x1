from fastapi import APIRouter
from app.handlers.file.api import router as user_router

router = APIRouter()

router.include_router(user_router, prefix="/file", tags=["file"])


@router.get("/")
async def api_root():
    return {"ping": "pong"}
