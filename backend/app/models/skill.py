from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import (
    ForeignKeyConstraint,
    PrimaryKeyConstraint,
    Text,
    UniqueConstraint,
    Uuid,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models.category import Category


class Skill(Base):
    __tablename__ = "skills"

    __table_args__ = (
        ForeignKeyConstraint(
            ["category_id"],
            ["categories.id"],
            name="skills_category_id_fkey",
        ),
        PrimaryKeyConstraint(
            "id",
            name="skills_pkey",
        ),
        UniqueConstraint(
            "skill",
            name="skills_skill_key",
        ),
    )

    id: Mapped[UUID] = mapped_column(
        Uuid,
        server_default=text("gen_random_uuid()"),
    )

    skill: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    category_id: Mapped[UUID | None] = mapped_column(
        Uuid,
    )

    category: Mapped["Category | None"] = relationship(
        back_populates="skills",
    )