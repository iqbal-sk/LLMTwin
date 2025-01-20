from loguru import logger
from pydantic_settings import SettingsConfigDict, BaseSettings

class Settings(BaseSettings):
    # MongoDB database
    DATABASE_HOST: str = "mongodb://llm_engineering:llm_engineering@127.0.0.1:27017"
    DATABASE_NAME: str = "twin"



settings = Settings()