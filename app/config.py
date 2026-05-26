from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):

    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ROUNDS: int

    model_config = ConfigDict(env_file="app/.env", extra="ignore")

settings = Settings()