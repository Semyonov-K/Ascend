import enum
from datetime import date, datetime

from sqlalchemy import String, ForeignKey, Enum, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.core.db import Base
from backend.app.core.mixins import IntPkMixin, TimestampMixin


class Characteristic(str, enum.Enum):
    body = "body"
    mind = "mind"
    mastery = "mastery"
    discipline = "discipline"
    spirit = "spirit"
    sociality = "sociality"


class Difficulty(str, enum.Enum):
    easy = "easy"
    normal = "normal"
    hard = "hard"


class Cadence(str, enum.Enum):
    hourly = "hourly"
    daily = "daily"
    weekly = "weekly"
    monthly = "monthly"


class TargetType(str, enum.Enum):
    binary = "binary"
    numeric = "numeric"


class SourceType(str, enum.Enum):
    manual = "manual"
    webhook = "webhook"


class Habit(IntPkMixin, TimestampMixin, Base):
    __tablename__ = "habits"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str | None] = mapped_column(default=None)
    characteristic: Mapped[Characteristic] = mapped_column(Enum(Characteristic), nullable=False)
    difficulty: Mapped[Difficulty] = mapped_column(Enum(Difficulty), nullable=False)
    cadence: Mapped[Cadence] = mapped_column(Enum(Cadence), nullable=False)
    target: Mapped[float] = mapped_column(default=1.0)
    target_type: Mapped[TargetType] = mapped_column(Enum(TargetType), default=TargetType.binary)
    unit: Mapped[str | None] = mapped_column(default=None)
    current_streak: Mapped[int] = mapped_column(default=0)
    best_streak: Mapped[int] = mapped_column(default=0)
    last_checkin_at: Mapped[datetime | None] = mapped_column(default=None)
    is_active: Mapped[bool] = mapped_column(default=True)


class HabitCheckin(IntPkMixin, TimestampMixin, Base):
    __tablename__ = "habit_checkins"

    __table_args__ = (
        UniqueConstraint("habit_id", "checkin_date", name="uq_habit_checkin_per_day"),
    )

    habit_id: Mapped[int] = mapped_column(
        ForeignKey("habits.id", ondelete="CASCADE"), nullable=False
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    value: Mapped[float] = mapped_column(nullable=False)
    checkin_date: Mapped[date] = mapped_column(nullable=False)
    source: Mapped[SourceType] = mapped_column(Enum(SourceType), default=SourceType.manual)
    idempotency_key: Mapped[str | None] = mapped_column(default=None)
