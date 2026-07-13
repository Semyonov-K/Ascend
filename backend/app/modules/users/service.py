from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.core.security import hash_password
from backend.app.modules.users.models import User
from backend.app.modules.users.schemas import UserCreate


async def create_user(session: AsyncSession, data: UserCreate) -> User:
    user = User(
        username=data.username,
        age=data.age,
        hashed_password=hash_password(data.password),
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
