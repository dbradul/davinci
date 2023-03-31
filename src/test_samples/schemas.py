from typing import Optional

from pydantic import BaseModel


class BaseTestSample(BaseModel):
    # description: str
    # is_function: Optional[bool] = False
    # code_context: Optional[str]
    input: str
    expected: str


class TestSample(BaseTestSample):
    id: int

    class Config:
        orm_mode = True


class TestSampleUpdate(BaseTestSample):

    class Config:
        orm_mode = True

class TestSampleCreate(BaseTestSample):

    class Config:
        orm_mode = True
