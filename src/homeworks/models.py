from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from davinci.database import Base


class Homework(Base):
    __tablename__ = 'homework'

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False, unique=True)
    description = Column(String, nullable=False)
