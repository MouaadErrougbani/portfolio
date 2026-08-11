from datetime import date
from uuid import UUID

from pydantic import BaseModel

from app.schemas.base import ResponseSchema


class DiplomaCreate(BaseModel):
    name: str
    establishment: str
    start_date: date | None = None
    end_date: date | None = None


class DiplomaUpdate(BaseModel):
    name: str | None = None
    establishment: str | None = None
    start_date: date | None = None
    end_date: date | None = None


class DiplomaResponse(ResponseSchema):
    id: UUID
    name: str
    establishment: str
    start_date: date | None = None
    end_date: date | None = None