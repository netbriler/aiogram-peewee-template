from sqlalchemy.ext.asyncio import AsyncSession

from .logging import logger


def save_execute(f):
    async def wrapper(session: AsyncSession, *args, **kwargs):
        try:
            return await f(session, *args, **kwargs)
        except Exception as e:
            await session.rollback()
            logger.error(e)

    return wrapper


async def save_commit(session: AsyncSession):
    try:
        await session.commit()
    except Exception as e:
        await session.rollback()
        logger.error(e)
