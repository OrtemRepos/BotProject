from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    redis_host: str
    redis_port: int

    expire_time: int

    bootstrap_server: str

    model_config = SettingsConfigDict()


settings = Config()  # type: ignore
