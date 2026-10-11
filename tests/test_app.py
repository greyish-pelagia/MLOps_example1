import pytest
from fastapi.testclient import TestClient

from app import app as api_root


@pytest.fixture
def client():
    with TestClient(api_root) as client:
        yield client


def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ML API"}


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
