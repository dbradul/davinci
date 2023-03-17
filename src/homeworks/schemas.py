from pydantic import BaseModel


class BaseHomework(BaseModel):
    number: int
    description: str


class Homework(BaseHomework):
    # id: int

    class Config:
        orm_mode = True
