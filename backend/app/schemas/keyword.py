from uuid import UUID

from pydantic import BaseModel

from app.schemas.base import ResponseSchema


class KeywordCreate(BaseModel):
    label: str


class KeywordUpdate(BaseModel):
    label: str | None = None


class KeywordResponse(ResponseSchema):
    id: UUID
    label: str