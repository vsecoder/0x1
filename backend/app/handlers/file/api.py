from fastapi import APIRouter

from app.db.functions import File

router = APIRouter()


@router.get("/{sha256}")
async def get_file(sha256: str):
    return await File.get_file(sha256=sha256)

# upload file

# prune files
