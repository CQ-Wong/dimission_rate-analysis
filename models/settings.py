from typing import List, Optional

from pydantic import BaseSettings
from pydantic.main import BaseModel


class DBConnetion(BaseModel):
    host: str
    port: int


class DBUser(BaseModel):
    username: str
    password: str


class DBConfig(BaseModel):
    DB_POOL_MAX_OVERFLOW: int = 50
    DB_POOL_SIZE: int = 20


class Settings(BaseSettings):
    DB_SQLSERVER: Optional[DBConnetion]
    DB_USER: Optional[DBUser]
    HR_DB_NAME: Optional[str]
    DB_Config: Optional[DBConfig] = DBConfig()

    class Config:
        env_file = ".env"


settings = Settings()
