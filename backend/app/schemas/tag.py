from uuid import UUID

from pydantic import BaseModel

from app.schemas.base import ResponseSchema


class TagCreate(BaseModel):
    label: str


class TagUpdate(BaseModel):
    label: str | None = None


class TagResponse(ResponseSchema):
    id: UUID
    label: str