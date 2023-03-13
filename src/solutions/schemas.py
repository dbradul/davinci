from enum import Enum
from typing import Optional, List

from pydantic import BaseModel


class VerdictKind(str, Enum):
    PASSED = 'PASSED'
    FAILED = 'FAILED'


class SolutionError(BaseModel):
    message: str
    input: str
    expected: str
    actual: str
    # stacktrace: str


class Solution(BaseModel):
    content: str

    # class Config:
    #     schema_extra = {
    #         "examples":{
    #             "normal": {
    #                 "content": "a, b, c = [float(x) for x in input().split()]\nresult = a + b * ( c / 2 )\nprint(result)",
    #             },
    #             "converted": {
    #                 "content": "a, b, c = [float(x) for x in input().split()]\nresult = a + b * ( c / 2 )\nprint(result)",
    #             },
    #             "invalid": {
    #                 "content": "a, b, c = [float(x) for x in input().split()]\nresult = a + b * ( c / 2 )\nprint(result)",
    #             },
    #         },
    #         # "example": {
    #         #     "content": "a, b, c = [float(x) for x in input().split()]\nresult = a + b * ( c / 2 )\nprint(result)",
    #         # }
    #     }


class SolutionVerdict(BaseModel):
    verdict: VerdictKind
    error: Optional[SolutionError]
