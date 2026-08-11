from pydantic import BaseModel

from app.schemas.base import ResponseSchema


class InfoCreate(BaseModel):
    message: str | None = None
    petit_desc: str | None = None
    full_desc: str | None = None
    image: str | None = None


class InfoUpdate(BaseModel):
    message: str | None = None
    petit_desc: str | None = None
    full_desc: str | None = None
    image: str | None = None


class InfoResponse(ResponseSchema):
    id: int
    message: str | None = None
    petit_desc: str | None = None
    full_desc: str | None = None
    image: str | None = None