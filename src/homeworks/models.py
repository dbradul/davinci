from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy.orm import relationship

from davinci.database import Base


class Homework(Base):
    __tablename__ = 'homework'

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False, unique=True, index=True)
    description = Column(String, nullable=False)
    code_context = Column(String, nullable=True)
    sample_input = Column(String, nullable=True)
    sample_output = Column(String, nullable=True)
    is_function = Column(Boolean, nullable=True, default=False)

    test_samples = relationship("TestSample", back_populates="homework")