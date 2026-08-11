from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import (
    Date,
    ForeignKeyConstraint,
    PrimaryKeyConstraint,
    Text,
    UniqueConstraint,
    Uuid,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from app.models.association_tables import (
    project_framework,
    project_keyword,
    project_language,
    project_subdomain,
    project_tag,
)

if TYPE_CHECKING:
    from app.models.domain import Domain
    from app.models.framework import Framework
    from app.models.keyword import Keyword
    from app.models.programming_language import ProgrammingLanguage
    from app.models.subdomain import Subdomain
    from app.models.tag import Tag


class Project(Base):
    __tablename__ = "projects"

    __table_args__ = (
        ForeignKeyConstraint(
            ["id_domain"],
            ["domains.id"],
            name="projects_id_domain_fkey",
        ),
        PrimaryKeyConstraint(
            "id",
            name="projects_pkey",
        ),
        UniqueConstraint(
            "github_link",
            name="projects_github_link_key",
        ),
        UniqueConstraint(
            "name",
            name="projects_name_key",
        ),
        UniqueConstraint(
            "production_link",
            name="projects_production_link_key",
        ),
    )

    id: Mapped[UUID] = mapped_column(
        Uuid,
        server_default=text("gen_random_uuid()"),
    )

    name: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
    )

    github_link: Mapped[str | None] = mapped_column(
        Text,
    )

    production_link: Mapped[str | None] = mapped_column(
        Text,
    )

    realization_date: Mapped[date | None] = mapped_column(
        Date,
    )

    image: Mapped[str | None] = mapped_column(
        Text,
    )

    id_domain: Mapped[UUID | None] = mapped_column(
        Uuid,
    )

    # Many-to-One
    domain: Mapped["Domain | None"] = relationship(
        back_populates="projects",
    )

    # Many-to-Many
    frameworks: Mapped[list["Framework"]] = relationship(
        secondary=project_framework,
        back_populates="projects",
    )

    keywords: Mapped[list["Keyword"]] = relationship(
        secondary=project_keyword,
        back_populates="projects",
    )

    programming_languages: Mapped[list["ProgrammingLanguage"]] = relationship(
        secondary=project_language,
        back_populates="projects",
    )

    subdomains: Mapped[list["Subdomain"]] = relationship(
        secondary=project_subdomain,
        back_populates="projects",
    )

    tags: Mapped[list["Tag"]] = relationship(
        secondary=project_tag,
        back_populates="projects",
    )