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


class SolutionVerdict(BaseModel):
    verdict: VerdictKind
    error: Optional[SolutionError]
