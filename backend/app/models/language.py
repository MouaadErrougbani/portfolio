from uuid import UUID

from sqlalchemy import (
    PrimaryKeyConstraint,
    Text,
    UniqueConstraint,
    Uuid,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Language(Base):
    __tablename__ = "languages"

    __table_args__ = (
        PrimaryKeyConstraint(
            "id",
            name="languages_pkey",
        ),
        UniqueConstraint(
            "code",
            name="languages_code_key",
        ),
        UniqueConstraint(
            "label",
            name="languages_label_key",
        ),
    )

    id: Mapped[UUID] = mapped_column(
        Uuid,
        server_default=text("gen_random_uuid()"),
    )

    code: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    label: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )