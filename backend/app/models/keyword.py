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

if TYPE_CHECKING:
    from app.models.project import Project


class Keyword(Base):
    __tablename__ = "keywords"

    __table_args__ = (
        PrimaryKeyConstraint(
            "id",
            name="keywords_pkey",
        ),
        UniqueConstraint(
            "label",
            name="keywords_label_key",
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
        secondary="project_keyword",
        back_populates="keywords",
    )