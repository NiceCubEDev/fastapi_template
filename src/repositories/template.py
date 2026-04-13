from src.schemas.template import TemplateModel


class TemplateRepository:
    async def get_template(self) -> TemplateModel:
        return TemplateModel(text="FastAPI template is ready")


def get_template_repository() -> TemplateRepository:
    return TemplateRepository()
