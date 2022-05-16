from pydantic import BaseSettings, BaseModel


class Settings(BaseSettings):
    database_link: str

    class Config:
        env_file = ".env"

settings = Settings()
