from datetime import date
from uuid import UUID

from sqlalchemy import (
    Date,
    PrimaryKeyConstraint,
    Text,
    Uuid,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Diploma(Base):
    __tablename__ = "diplomas"

    __table_args__ = (
        PrimaryKeyConstraint(
            "id",
            name="diplomas_pkey",
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

    establishment: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    start_date: Mapped[date | None] = mapped_column(
        Date,
    )

    end_date: Mapped[date | None] = mapped_column(
        Date,
    )