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


class Tag(Base):
    __tablename__ = "tags"

    __table_args__ = (
        PrimaryKeyConstraint(
            "id",
            name="tags_pkey",
        ),
        UniqueConstraint(
            "label",
            name="tags_label_key",
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
        secondary="project_tag",
        back_populates="tags",
    )