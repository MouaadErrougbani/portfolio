from uuid import UUID

from pydantic import BaseModel

from app.schemas.base import ResponseSchema


class LanguageCreate(BaseModel):
    code: str
    label: str


class LanguageUpdate(BaseModel):
    code: str | None = None
    label: str | None = None


class LanguageResponse(ResponseSchema):
    id: UUID
    code: str
    label: str