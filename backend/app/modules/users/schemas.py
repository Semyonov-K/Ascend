from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from backend.app.modules.users.models import UserRole


class UserBase(BaseModel):
    name: str | None = Field(default=None, max_length=50)
    surname: str | None = Field(default=None, max_length=50)
    age: int | None = Field(default=None, ge=0, le=150)
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=128)


class UserUpdate(UserBase):
    password: str | None = Field(default=None, min_length=8, max_length=128)
    name: str | None = Field(default=None, max_length=50)
    surname: str | None = Field(default=None, max_length=50)
    age: int | None = Field(default=None, ge=0, le=150)
    username: str | None = Field(default=None, min_length=3, max_length=50)
    email: EmailStr | None = None


class UserRead(UserBase):
    id: int
    role: UserRole
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserRoleUpdate(BaseModel):
    role: UserRole
