from pydantic import BaseModel

from app.schemas.base import ResponseSchema


class TraductionCreate(BaseModel):
    label: str
    ar: str | None = None
    fr: str | None = None
    en: str | None = None


class TraductionUpdate(BaseModel):
    ar: str | None = None
    fr: str | None = None
    en: str | None = None


class TraductionResponse(ResponseSchema):
    label: str
    ar: str | None = None
    fr: str | None = None
    en: str | None = None