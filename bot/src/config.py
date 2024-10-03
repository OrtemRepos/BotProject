from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    token: str
    bootstrap_server: str

    model_config = SettingsConfigDict(extra="ignore")


settings = Config()  # type: ignore
