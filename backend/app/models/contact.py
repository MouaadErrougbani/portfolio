from uuid import UUID

from sqlalchemy import (
    PrimaryKeyConstraint,
    Text,
    Uuid,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Contact(Base):
    __tablename__ = "contacts"

    __table_args__ = (
        PrimaryKeyConstraint(
            "id",
            name="contacts_pkey",
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

    icon: Mapped[str | None] = mapped_column(
        Text,
    )

    link: Mapped[str | None] = mapped_column(
        Text,
    )