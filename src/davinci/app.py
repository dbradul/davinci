from fastapi import FastAPI

from homeworks import apis as homeworks_apis
from test_samples import apis as test_samples_apis
from solutions import apis as solutions_apis


tags_metadata = [
    {
        'name': 'homeworks',
        'description': 'Retrieving homeworks',
    },
    {
        'name': 'solutions',
        'description': 'Submitting solutions',
    },
]

app = FastAPI(
    title="DaVinci",
    description="Automated h/w checker for Basic Python course",
    version="0.0.1",
    docs_url="/",
    openapi_tags=tags_metadata,
)

app.include_router(homeworks_apis.router)
app.include_router(test_samples_apis.router)
app.include_router(solutions_apis.router)