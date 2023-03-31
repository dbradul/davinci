from fastapi import (
    Depends,
)
from sqlalchemy.orm import Session

from davinci.database import get_session


class TestSampleService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
