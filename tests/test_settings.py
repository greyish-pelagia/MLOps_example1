import os

import pytest

from settings import Settings


@pytest.fixture(autouse=True)
def test_environment():
    os.environ["API_KEY"] = "test_api"
    return test_environment


def test_settings():
    settings = Settings()
    assert settings.APP_NAME == "Dev test"
    assert settings.ENVIRONMENT == "test"
    assert settings.API_KEY is not None
