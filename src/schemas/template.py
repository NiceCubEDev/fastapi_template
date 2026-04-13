from pydantic import BaseModel


class TemplateModel(BaseModel):
    text: str
