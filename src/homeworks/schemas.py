from typing import Optional

from pydantic import BaseModel


class BaseHomework(BaseModel):
    description: str
    is_function: Optional[bool] = False
    code_context: Optional[str]
    sample_input: Optional[str]
    sample_output: Optional[str]


class Homework(BaseHomework):
    number: int

    class Config:
        orm_mode = True


class HomeworkUpdate(BaseHomework):

    class Config:
        orm_mode = True

class HomeworkCreate(BaseHomework):

    class Config:
        orm_mode = True
