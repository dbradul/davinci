from textwrap import dedent
from typing import Union

from fastapi import APIRouter, Depends, Body

from solutions import schemas
from solutions.schemas import Solution, SolutionResponse
from solutions.services import SolutionService, AISolutionService

#
# SOLUTION_EXAMPLE = Body(
#     examples={
#         "no_input": {
#             "summary": "Simple example",
#             "description": "A solution that doesn't require input.",
#             "value": {
#                 "content": "print('Hello world!')",
#             }
#         },
#         "floats": {
#             "summary": "Floats example",
#             "description": "A solution that requires floats as input.",
#             "value": {
#                 "content": dedent("""
#                     a, b, c = [float(x) for x in input().split()]
#                     result = a + b * ( c / 2 )
#                     print(result)
#                 """),
#             }
#         },
#         "string": {
#             "summary": "String example",
#             "description": "A solution that requires string as input.",
#             "value": {
#                 "content": dedent("""
#                     s = input()
#                     result = ''.join(x.capitalize() for x in s.split('_'))
#                     print(result)
#                 """),
#             }
#         },
#         "function": {
#             "summary": "Function example",
#             "description": "A solution that requires an implementation to be inside 'solution' function only.",
#             "value": {
#               "content": dedent("""
#                   def solution(lst):
#                       return max(lst) - min(lst)
#                   """)
#             }
#         },
#     },
# )


router = APIRouter(
    prefix="/test_samples",
    tags=["test_samples"],
)

#
# @router.post(
#     '/{homework_number}/auto',
#     response_model=SolutionResponse,
# )
# def submit_solution_to_automated_checker(
#     homework_number: int,
#     solution: Solution = SOLUTION_EXAMPLE,
#     solution_service: SolutionService = Depends(),
# ):
#     return solution_service.check(
#         homework_number,
#         solution.content
#     )
#
#
# @router.post(
#     '/{homework_number}/ai',
#     response_model=str,
# )
# def submit_solution_to_ai(
#     homework_number: int,
#     solution: Solution = SOLUTION_EXAMPLE,
#     solution_service: AISolutionService = Depends(),
# ):
#     return solution_service.check(
#         homework_number,
#         solution.content
#     )
#
#
# @router.get(
#     '/{homework_number}/ai_prompt',
#     response_model=str,
# )
# def get_ai_prompt(
#     homework_number: int,
#     solution_service: AISolutionService = Depends(),
# ):
#     return solution_service.get_prompt(
#         homework_number
#     )


# @router.get(
#     '/',
#     response_model=List[schemas.Homework],
# )
# def get_homeworks(
#     homeworks_service: HomeworksService = Depends(),
# ):
#     return homeworks_service.get_many()


@router.get(
    '/{number}',
    response_model=schemas.Homework,
)
def get_homework(
    number: int,
    homeworks_service: HomeworksService = Depends(),
):
    return homeworks_service.get(
        number=number,
    )
