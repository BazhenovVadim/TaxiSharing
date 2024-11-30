from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str
    SECRET_JWT_KEY: str
    TOKEN_EXP_IN_MINUTES: int

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
