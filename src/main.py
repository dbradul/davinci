import uvicorn

from davinci.app import app
from davinci.settings import settings


uvicorn.run(
    app,
    host=settings.server_host,
    port=settings.server_port
)
