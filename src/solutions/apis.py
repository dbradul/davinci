from typing import List

from fastapi import APIRouter, Depends, Body

from solutions import models, schemas
from solutions.schemas import Solution
from solutions.services import SolutionService, AISolutionService


SOLUTION_EXAMPLE = Body(
    examples={
        "no_input": {
            "summary": "Simple example",
            "description": "A solution that doesn't require input.",
            "value": {
                "content": "print('Hello world!')",
            }
        },
        "floats": {
            "summary": "Floats example",
            "description": "A solution that requires floats as input.",
            "value": {
                "content": "a, b, c = [float(x) for x in input().split()] \nresult = a + b * ( c / 2 ) \nprint(result)",
            }
        },
        "string": {
            "summary": "String example",
            "description": "A solution that requires string as input.",
            "value": {
                "content": "s = input() \nresult = ''.join(x.capitalize() for x in s.split('_')) \nprint(result)",
            }
        },
    },
)


router = APIRouter(
    prefix="/solutions",
    tags=["solutions"],
)


@router.post(
    '/{homework_number}/auto',
    response_model=schemas.SolutionVerdict,
)
def submit_solution_to_automated_checker(
    homework_number: int,
    # solution: Solution,
    solution: Solution = SOLUTION_EXAMPLE,
    solution_service: SolutionService = Depends(),
):
    return solution_service.check(
        homework_number,
        solution.content
    )



@router.post(
    '/{homework_number}/ai',
    response_model=str,
)
def submit_solution_to_ai(
    homework_number: int,
    solution: Solution = SOLUTION_EXAMPLE,
    solution_service: AISolutionService = Depends(),
):
    return solution_service.submit_solution(
        homework_number,
        solution.content
    )


@router.get(
    '/{homework_number}/ai_prompt',
    response_model=str,
)
def get_ai_prompt(
    homework_number: int,
    solution_service: AISolutionService = Depends(),
):
    return solution_service.get_prompt(
        homework_number
    )
