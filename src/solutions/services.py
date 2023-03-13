import json
from typing import (
    List,
    Optional,
)

import epicbox
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

import homeworks
from solutions import models, schemas
from davinci.settings import settings
# from solutions import models, schemas
from davinci.database import get_session
from solutions.schemas import SolutionError

import openai

openai.api_key = settings.openai_api_key


class SolutionService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def check(
        self,
        homework_number: int,
        solution_text: str,
    ) -> schemas.SolutionVerdict:
        solutions = (
            self.session
            .query(models.Solution)
            .join(homeworks.models.Homework)
            .filter(
                homeworks.models.Homework.number == homework_number
            )
            .all()
        )

        if not solutions:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        for solution in solutions:
            epicbox.configure(
                profiles=[
                    epicbox.Profile('python', 'python:3.6.5-alpine')
                ]
            )

            files = [{'name': 'main.py', 'content': solution_text.encode()}]
            limits = {'cputime': 1, 'memory': 64}
            solution_result = epicbox.run(
                profile_name='python',
                command='python3 main.py',
                stdin=solution.input.encode(),
                files=files,
                limits=limits
            )

            actual_output = solution_result['stdout'].decode().strip()
            if actual_output != solution.expected:
                serialized_solution_result = json.dumps({
                    k: v.decode() if isinstance(v, bytes) else v
                    for k, v in solution_result.items()
                })

                error = SolutionError(
                    message=serialized_solution_result,
                    input=solution.input,
                    expected=solution.expected,
                    actual=actual_output,
                )

                result = schemas.SolutionVerdict(
                    verdict=schemas.VerdictKind.FAILED,
                    error=error
                )
                break
        else:
            result = schemas.SolutionVerdict(
                verdict=schemas.VerdictKind.PASSED,
            )

        return result


class AISolutionService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def submit_solution(
        self,
        homework_number: int,
        solution_text: str,
    ) -> str:
        homework = (
            self.session
            .query(homeworks.models.Homework)
            .filter(
                homeworks.models.Homework.number == homework_number
            )
            .first()
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Ось завдання по програмуванню на Python:\n\n{homework.description}"},
                {"role": "assistant", "content": "Ok, got it."},
                {"role": "user", "content": f"Чи є наступний Python код коректним рішенням для цього завдання?:\n\n{solution_text}"}
            ],
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        result = response.choices[0].message.content

        return result


    def get_prompt(
        self,
        homework_number: int
    ) -> str:
        homework = (
            self.session
            .query(homeworks.models.Homework)
            .filter(
                homeworks.models.Homework.number == homework_number
            )
            .first()
        )

        response = openai.ChatCompletion.create(
            # model="text-davinci-003",
            model="gpt-3.5-turbo-0301",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Ось завдання по програмуванню на Python:\n\n{homework.description}"},
                {"role": "assistant", "content": "Ok, got it."},
                {"role": "user", "content": f"Дай підказку як його виконати, але без остаточного рішення."}
            ],
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        result = response.choices[0].message.content

        return result
