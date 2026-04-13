from typing import Annotated

from fastapi import Depends, HTTPException

from src.repositories.template import TemplateRepository, get_template_repository
from src.schemas.template import TemplateModel


class TemplateService:
    def __init__(self, repository: TemplateRepository):
        self.repository = repository

    async def get_template(self) -> TemplateModel:
        try:
            return await self.repository.get_template()
        except Exception as exc:
            raise HTTPException(status_code=500, detail="Template service failed") from exc


def get_template_service(
    repository: Annotated[TemplateRepository, Depends(get_template_repository)],
) -> TemplateService:
    return TemplateService(repository)
