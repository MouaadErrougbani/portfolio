from datetime import date
from uuid import UUID

from pydantic import BaseModel

from app.schemas.base import ResponseSchema


class ProjectCreate(BaseModel):
    name: str
    description: str | None = None
    github_link: str | None = None
    production_link: str | None = None
    realization_date: date | None = None
    image: str | None = None
    id_domain: UUID | None = None


class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    github_link: str | None = None
    production_link: str | None = None
    realization_date: date | None = None
    image: str | None = None
    id_domain: UUID | None = None


class ProjectResponse(ResponseSchema):
    id: UUID
    name: str
    description: str | None = None
    github_link: str | None = None
    production_link: str | None = None
    realization_date: date | None = None
    image: str | None = None
    id_domain: UUID | None = None

class ProjectDetailsResponse(BaseModel):
    id: UUID
    name: str
    description: str | None

    tags: list[str]

    githubLink: str | None
    productionLink: str | None

    realizationDate: date | None

    domain: str | None

    subDomain: list[str]

    keywords: list[str]

    languages: list[str]

    frameworks: list[str]

    image: str | None