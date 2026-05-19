from sqlalchemy import Column, Integer, String, Boolean

from lessons.lesson_21.declarative_base import Base



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    age = Column(Integer)
