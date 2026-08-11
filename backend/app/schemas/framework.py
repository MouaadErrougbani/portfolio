from uuid import UUID

from pydantic import BaseModel

from app.schemas.base import ResponseSchema


class FrameworkCreate(BaseModel):
    label: str


class FrameworkUpdate(BaseModel):
    label: str | None = None


class FrameworkResponse(ResponseSchema):
    id: UUID
    label: str