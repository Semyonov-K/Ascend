import enum

from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.core.db import Base
from backend.app.core.mixins import IntPkMixin, TimestampMixin


class UserRole(str, enum.Enum):
    user = "user"
    admin = "admin"


class User(IntPkMixin, TimestampMixin, Base):
    __tablename__ = "users"

    name: Mapped[str | None] = mapped_column(String(50), default=None)
    surname: Mapped[str | None] = mapped_column(String(50), default=None)
    age: Mapped[int | None] = mapped_column(default=None)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.user)
