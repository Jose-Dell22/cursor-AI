from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Platziflix"
    VERSION: str = "0.1.0"
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/platziflix"

    model_config = SettingsConfigDict(env_file=".env")
