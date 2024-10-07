from typing import List, Union
from pydantic import BaseSettings, AnyHttpUrl, validator


class Settings(BaseSettings):
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str

    S3_BUCKET: str
    BUCKET_PREFIX: str

    EXECUTION_ROLE: str
    ENDPOINT_NAME: str

    PG_USER: str
    PG_PWD: str
    PG_ENDPOINT: str
    PG_DATABASE: str
    PG_PORT: str
    PG_SCHEMA: str


settings = Settings()
