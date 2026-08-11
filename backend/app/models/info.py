from sqlalchemy import (
    PrimaryKeyConstraint,
    SmallInteger,
    Text,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Info(Base):
    __tablename__ = "infos"

    __table_args__ = (
        PrimaryKeyConstraint(
            "id",
            name="infos_pkey",
        ),
    )

    id: Mapped[int] = mapped_column(
        SmallInteger,
        server_default=text("1"),
    )

    message: Mapped[str | None] = mapped_column(
        Text,
    )

    petit_desc: Mapped[str | None] = mapped_column(
        Text,
    )

    full_desc: Mapped[str | None] = mapped_column(
        Text,
    )

    image: Mapped[str | None] = mapped_column(
        Text,
    )