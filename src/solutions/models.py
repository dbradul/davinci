# from sqlalchemy import Column
# from sqlalchemy import Integer
# from sqlalchemy import String
# from sqlalchemy import ForeignKey
# from sqlalchemy import Boolean
#
# from davinci.database import Base
#
#
# class Solution(Base):
#     __tablename__ = 'solution'
#
#     id = Column(Integer, primary_key=True)
#     homework_id = Column(Integer, ForeignKey('homework.id'), index=True)
#     input = Column(String, nullable=False)
#     expected = Column(String, nullable=False)
#     is_function = Column(Boolean, nullable=True, default=False)
