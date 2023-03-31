from typing import List

from fastapi import APIRouter, Depends

from test_samples import schemas
from test_samples.services import TestSampleService

router = APIRouter(
    prefix="/test_samples",
    tags=["test_samples"],
)


@router.get(
    '/{homework_number}',
    response_model=List[schemas.TestSample],
)
def get_test_samples(
    homework_number: int,
    test_sample_service: TestSampleService = Depends(),
):
    return test_sample_service.get(
        homework_number=homework_number,
    )
