from typing import Optional

from pydantic import BaseModel


class BaseHomework(BaseModel):
    number: int
    description: str
    code_context: Optional[str]
    sample_input: Optional[str]
    sample_output: Optional[str]


class Homework(BaseHomework):
    id: int

    class Config:
        orm_mode = True
