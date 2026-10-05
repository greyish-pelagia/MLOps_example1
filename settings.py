from pydantic import field_validator
from pydantic_settings import BaseSettings

_ALLOWED_ENV_TYPES = {"dev", "test", "prod"}


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    API_KEY: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value):
        if value not in _ALLOWED_ENV_TYPES:
            raise ValueError(
                f"Please assign one of the values {_ALLOWED_ENV_TYPES} to ENVIRONMENT env variable"
            )
        return value
