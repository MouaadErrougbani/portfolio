from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import (
    PrimaryKeyConstraint,
    Text,
    UniqueConstraint,
    Uuid,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from app.models.association_tables import project_language

if TYPE_CHECKING:
    from app.models.project import Project


class ProgrammingLanguage(Base):
    __tablename__ = "programming_languages"

    __table_args__ = (
        PrimaryKeyConstraint(
            "id",
            name="programming_languages_pkey",
        ),
        UniqueConstraint(
            "label",
            name="programming_languages_label_key",
        ),
    )

    id: Mapped[UUID] = mapped_column(
        Uuid,
        server_default=text("gen_random_uuid()"),
    )

    label: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    projects: Mapped[list["Project"]] = relationship(
        secondary=project_language,
        back_populates="programming_languages",
    )