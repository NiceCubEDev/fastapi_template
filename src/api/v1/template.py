from typing import Annotated

from fastapi import APIRouter, Depends

from src.schemas.template import TemplateModel
from src.services.template import TemplateService, get_template_service

router = APIRouter(prefix="/template", tags=["template"])


@router.get("", response_model=TemplateModel)
async def get_template(
    service: Annotated[TemplateService, Depends(get_template_service)],
) -> TemplateModel:
    return await service.get_template()
