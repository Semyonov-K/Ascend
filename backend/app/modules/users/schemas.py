from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    age: int | None = None


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
