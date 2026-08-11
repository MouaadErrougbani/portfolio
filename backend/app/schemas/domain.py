from uuid import UUID

from pydantic import BaseModel

from app.schemas.base import ResponseSchema


class DomainCreate(BaseModel):
    label: str


class DomainUpdate(BaseModel):
    label: str | None = None


class DomainResponse(ResponseSchema):
    id: UUID
    label: str