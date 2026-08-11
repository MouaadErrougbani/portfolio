from uuid import UUID

from pydantic import BaseModel

from app.schemas.base import ResponseSchema


class ContactCreate(BaseModel):
    label: str
    icon: str | None = None
    link: str | None = None


class ContactUpdate(BaseModel):
    label: str | None = None
    icon: str | None = None
    link: str | None = None


class ContactResponse(ResponseSchema):
    id: UUID
    label: str
    icon: str | None = None
    link: str | None = None