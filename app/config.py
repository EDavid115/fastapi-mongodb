from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGODB_URI: str
    MONGODB_DATABASE: str

    ACCESS_TOKEN_EXPIRES_IN: int
    REFRESH_TOKEN_EXPIRES_IN: int

    JWT_ALGORITHM: str
    JWT_PUBLIC_KEY: str
    JWT_PRIVATE_KEY: str

    CLIENT_ORIGIN: str

    class Config:
        env_file = './.env'


settings = Settings()