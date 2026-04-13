from fastapi import APIRouter

from src.api.v1.template import router as template_router

router = APIRouter(prefix="/api/v1")
router.include_router(template_router)
