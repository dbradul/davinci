from typing import List

from fastapi import APIRouter, Depends

from homeworks import schemas
from homeworks.services import HomeworksService

router = APIRouter(
    prefix="/homeworks",
    tags=["homeworks"],
)


@router.get(
    '/',
    response_model=List[schemas.Homework],
)
def get_homeworks(
    homeworks_service: HomeworksService = Depends(),
):
    return homeworks_service.get_many()


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


# @router.put(
#     '/{number}',
#     response_model=schemas.Homework,
# )
def update_homework(
    number: int,
    homework_data: schemas.HomeworkUpdate,
    homeworks_service: HomeworksService = Depends(),
):
    return homeworks_service.update(
        number=number,
        homework_data=homework_data
    )
