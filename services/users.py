from sqlalchemy import select, func, update
from sqlalchemy.ext.asyncio import AsyncSession

from data.config import ADMINS
from models import User
from utils.misc.logging import logger


async def count_users(session: AsyncSession):
    sql = select([func.count()]).select_from(User)
    query = await session.execute(sql)

    return query.scalar()


async def get_users(session: AsyncSession) -> list[User]:
    sql = select(User)
    query = await session.execute(sql)

    return [u for u, in query]


async def get_user(session: AsyncSession, id: int) -> User:
    sql = select(User).where(User.id == id)
    query = await session.execute(sql)

    user = query.scalar_one_or_none()

    return user


async def update_user(session: AsyncSession, user: User, name: str, username: str = None) -> User:
    user.name = name
    user.username = username

    await session.commit()

    return user


async def edit_user_language(session: AsyncSession, id: int, language: str):
    sql = update(User).where(User.id == id).values(language=language)

    await session.execute(sql)
    await session.commit()


async def create_user(session: AsyncSession, id: int, name: str, username: str = None, language: str = None) -> User:
    new_user = User(id=id, name=name, username=username, language=language)

    if id in ADMINS:
        new_user.is_admin = True

    session.add(new_user)
    await session.commit()

    logger.info(f'New user {new_user}')

    return new_user


async def get_or_create_user(session: AsyncSession, id: int, name: str, username: str = None,
                             language: str = None) -> User:
    user = await get_user(session, id)

    if user:
        user = await update_user(session, user, name, username)

        return user

    return await create_user(session, id, name, username, language)
