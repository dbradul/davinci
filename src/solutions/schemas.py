from enum import Enum
from typing import Optional, List

from pydantic import BaseModel


# class VerdictStatus(int, Enum):
#     SUCCESS = 0
#     ERROR = -1
#
#
# class VerdictKind(str, Enum):
#     PASSED = 'PASSED'
#     FAILED = 'FAILED'
#

class SolutionError(BaseModel):
    message: str
    input: str
    expected: str
    actual: str
    # stacktrace: str


class Solution(BaseModel):
    content: str

#
# class SolutionVerdict(BaseModel):
#     status: VerdictStatus
#     kind: VerdictKind
#
#
# class SolutionVerdictSuccess(SolutionVerdict):
#     status = VerdictStatus.SUCCESS
#     kind = VerdictKind.PASSED
#
#
# class SolutionVerdictError(SolutionVerdict):
#     status = VerdictStatus.ERROR
#     kind = VerdictKind.FAILED


class SolutionResponse(BaseModel):
    # verdict: SolutionVerdict
    success: bool
    error: Optional[SolutionError]


class SolutionResponseSuccess(SolutionResponse):
    # verdict = SolutionVerdict(
    #     status=VerdictStatus.SUCCESS,
    #     verdict=VerdictKind.PASSED
    # )
    # verdict = SolutionVerdictSuccess()
    success = True


class SolutionResponseFail(SolutionResponse):
    # verdict = SolutionVerdict(
    #     status=VerdictStatus.ERROR,
    #     verdict=VerdictKind.FAILED
    # )
    # verdict = SolutionVerdictError()
    success = False
    # error: SolutionError
