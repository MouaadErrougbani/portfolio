from typing import Optional


from sqlalchemy import (
    PrimaryKeyConstraint,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Traduction(Base):
    __tablename__ = "traductions"

    __table_args__ = (
        PrimaryKeyConstraint(
            "label",
            name="traductions_pkey",
        ),
    )

    label: Mapped[str] = mapped_column(
        Text,
    )

    ar: Mapped[Optional[str]] = mapped_column(
        Text,
    )

    fr: Mapped[Optional[str]] = mapped_column(
        Text,
    )

    en: Mapped[Optional[str]] = mapped_column(
        Text,
    )