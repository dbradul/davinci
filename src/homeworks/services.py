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
                models.Homework.id.asc()
            )
            .all()
        )
        return homeworks

    def get(
        self,
        homework_number: int
    ) -> models.Homework:
        operation = self._get(homework_number)
        return operation

    def _get(self, homework_number: int) -> Optional[models.Homework]:
        homework = (
            self.session
            .query(models.Homework)
            .filter(
                models.Homework.number == homework_number
            )
            .first()
        )
        if not homework:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return homework
