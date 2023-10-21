from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from db_api.database import get_session
from db_api.tables.users import Users


async def add_user(
        user_id: int
):
    async with get_session() as session:
        user = Users(
            user_id=user_id
        )
        session.add(user)
        try:
            await session.commit()
        except IntegrityError:
            await session.rollback()

async def select_user_id(user_id: int):
    async with get_session() as session:
        sql = select(Users.user_id).where(
            Users.user_id == user_id
        )
        result = await session.execute(sql)
        return result.scalar()

async def select_id(user_id: int):
    async with get_session() as session:
        sql = select(Users.id).where(
            Users.user_id == user_id
        )
        result = await session.execute(sql)
        return result.scalar()

async def select_all_users():
    async with get_session() as session:
        sql = select(Users.user_id)
        result = await session.execute(sql)
        return result.scalars().all()
