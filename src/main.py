from __future__ import annotations

from fastapi import FastAPI

from src.api import api_router
from src.core.config import settings

app = FastAPI(title=settings.app_name, version=settings.app_version)
app.include_router(api_router)


@app.get("/health", tags=["health"])
async def health() -> dict[str, str]:
    return {"status": "ok"}
