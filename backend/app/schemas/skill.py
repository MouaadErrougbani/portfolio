from uuid import UUID

from pydantic import BaseModel

from app.schemas.base import ResponseSchema


class SkillCreate(BaseModel):
    skill: str
    category_id: UUID | None = None


class SkillUpdate(BaseModel):
    skill: str | None = None
    category_id: UUID | None = None


class SkillResponse(ResponseSchema):
    id: UUID
    skill: str
    category_id: UUID | None = None