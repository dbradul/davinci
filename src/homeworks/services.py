from typing import (
    List,
    Optional,
)

import openai
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from davinci.database import get_session
from davinci.settings import settings
from homeworks import models

openai.api_key = settings.openai_api_key


class HomeworksService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_many(self) -> List[models.Homework]:
        homeworks = (
            self.session
            .query(models.Homework)
            .order_by(
                models.Homework.number.asc()
            )
            .all()
        )
        return homeworks

    def get(self, number: int) -> models.Homework:
        operation = self._get(number)
        return operation

    def _get(self, number: int) -> Optional[models.Homework]:
        homework = (
            self.session
            .query(models.Homework)
            .filter(
                models.Homework.number == number
            )
            .first()
        )
        if not homework:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return homework
