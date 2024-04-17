from typing import Literal
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODE : Literal["DEV","TEST","PROD"]

    DB_PORT : str
    DB_HOST : str
    DB_NAME : str
    DB_USER : str
    DB_PASS : str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES : str
    ALGORITHM : str

    TEST_DB_PORT : str
    TEST_DB_HOST : str
    TEST_DB_NAME : str
    TEST_DB_USER : str
    TEST_DB_PASS : str

    
    def get_test_database_url(self):
        TEST_DATABASE_URL = f"postgresql+asyncpg://{self.TEST_DB_USER}:{self.TEST_DB_PASS}@{self.TEST_DB_HOST}:{self.TEST_DB_PORT}/{self.TEST_DB_NAME}"
        return TEST_DATABASE_URL

    def get_database_url(self):
        DATABASE_URL = f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return DATABASE_URL

    class Config:
        env_file = '.env'

settings = Settings()