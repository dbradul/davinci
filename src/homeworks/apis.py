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
    '/{id}',
    response_model=schemas.Homework,
)
def get_homework(
    id: int,
    homeworks_service: HomeworksService = Depends(),
):
    return homeworks_service.get(
        pk=id,
    )

