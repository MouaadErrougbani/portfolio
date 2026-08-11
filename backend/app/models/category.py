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
    from app.models.skill import Skill


class Category(Base):
    __tablename__ = "categories"

    __table_args__ = (
        PrimaryKeyConstraint(
            "id",
            name="categories_pkey",
        ),
        UniqueConstraint(
            "label",
            name="categories_label_key",
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

    skills: Mapped[list["Skill"]] = relationship(
        back_populates="category",
        cascade="all, delete-orphan",
    )