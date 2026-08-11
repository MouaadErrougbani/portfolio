from uuid import UUID

from pydantic import BaseModel, RootModel

from app.schemas.base import ResponseSchema


class CategoryCreate(BaseModel):
    label: str


class CategoryUpdate(BaseModel):
    label: str | None = None


class CategoryResponse(ResponseSchema):
    id: UUID
    label: str



class SkillsByCategoryResponse(
    RootModel[dict[str, list[str]]]
):
    pass