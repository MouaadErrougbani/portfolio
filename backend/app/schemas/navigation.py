from uuid import UUID

from pydantic import BaseModel

from app.schemas.base import ResponseSchema


class NavigationCreate(BaseModel):
    label: str
    position: int
    enabled: bool = True


class NavigationUpdate(BaseModel):
    label: str | None = None
    position: int | None = None
    enabled: bool | None = None


class NavigationResponse(ResponseSchema):
    id: UUID
    label: str
    position: int
    enabled: bool