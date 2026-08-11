from uuid import UUID

from pydantic import BaseModel

from app.schemas.base import ResponseSchema


class SubdomainCreate(BaseModel):
    label: str


class SubdomainUpdate(BaseModel):
    label: str | None = None


class SubdomainResponse(ResponseSchema):
    id: UUID
    label: str