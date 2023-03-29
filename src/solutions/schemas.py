from typing import Optional

from pydantic import BaseModel


class SolutionError(BaseModel):
    message: str
    input: str
    expected: str
    actual: str


class Solution(BaseModel):
    content: str


class SolutionResponse(BaseModel):
    success: bool
    error: Optional[SolutionError]


class SolutionResponseSuccess(SolutionResponse):
    success = True


class SolutionResponseFail(SolutionResponse):
    success = False
