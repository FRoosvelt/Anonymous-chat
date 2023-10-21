from sqlalchemy import Column, Integer, BigInteger

from db_api.database import Base


class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
