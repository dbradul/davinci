import pytest
from davinci.app import app
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    return TestClient(app)