from uuid import UUID

from sqlalchemy import (
    Boolean,
    PrimaryKeyConstraint,
    SmallInteger,
    Text,
    Uuid,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Navigation(Base):
    __tablename__ = "navigations"

    __table_args__ = (
        PrimaryKeyConstraint(
            "id",
            name="navigations_pkey",
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

    position: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False,
    )

    enabled: Mapped[bool] = mapped_column(
        Boolean,
        server_default=text("true"),
        nullable=True
    )