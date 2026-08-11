from uuid import UUID

from pydantic import BaseModel

from app.schemas.base import ResponseSchema


class ProgrammingLanguageCreate(BaseModel):
    label: str


class ProgrammingLanguageUpdate(BaseModel):
    label: str | None = None


class ProgrammingLanguageResponse(ResponseSchema):
    id: UUID
    label: str