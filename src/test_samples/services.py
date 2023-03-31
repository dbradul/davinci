from starlette import status
from typing import List

from fastapi import (
    Depends, HTTPException,
)
from sqlalchemy.orm import Session

import homeworks
from davinci.database import get_session
from test_samples import schemas


class TestSampleService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get(
        self,
        homework_number: int,
    ) -> List[schemas.TestSample]:
        homework = (
            self.session
            .query(homeworks.models.Homework)
            .filter(
                homeworks.models.Homework.number == homework_number
            )
            .first()
        )
        if not homework:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        return homework.test_samples
