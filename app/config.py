from pydantic import BaseSettings, BaseModel


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"

settings = Settings()

# from logging.config import dictConfig
# import logging
# from .config import LogConfig

# dictConfig(LogConfig().dict())
# logger = logging.getLogger("mycoolapp")

# logger.info("Dummy Info")
# logger.error("Dummy Error")
# logger.debug("Dummy Debug")
# logger.warning("Dummy Warning")


# class LogConfig(BaseModel):
#     """Logging configuration to be set for the server"""

#     LOGGER_NAME: str = "mycoolapp"
#     LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
#     LOG_LEVEL: str = "DEBUG"

#     # Logging config
#     version = 1
#     disable_existing_loggers = False
#     formatters = {
#         "default": {
#             "()": "uvicorn.logging.DefaultFormatter",
#             "fmt": LOG_FORMAT,
#             "datefmt": "%Y-%m-%d %H:%M:%S",
#         },
#     }
#     handlers = {
#         "default": {
#             "formatter": "default",
#             "class": "logging.StreamHandler",
#             "stream": "ext://sys.stderr",
#         },
#     }
#     loggers = {
#         "mycoolapp": {"handlers": ["default"], "level": LOG_LEVEL},
#     }
