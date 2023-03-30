from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from davinci.database import Base


class TestSample(Base):
    __tablename__ = 'test_sample'

    id = Column(Integer, primary_key=True)
    homework_id = Column(Integer, ForeignKey('homework.id'), index=True)
    input = Column(String, nullable=False)
    expected = Column(String, nullable=False)
