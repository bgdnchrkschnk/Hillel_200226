from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from core.lessons.lesson_21.declarative_base import Base


class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Встановлення відношення "один до багатьох" з таблицею Employee
    employees = relationship("Employee", back_populates="department")
