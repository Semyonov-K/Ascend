import enum
from datetime import datetime

from sqlalchemy import Enum, String, func
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.core.db import Base


class UserRole(str, enum.Enum):
    user = "user"
    admin = "admin"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None] = mapped_column(String(50), default=None)
    surname: Mapped[str | None] = mapped_column(String(50), default=None)
    age: Mapped[int | None] = mapped_column(default=None)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.user)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
