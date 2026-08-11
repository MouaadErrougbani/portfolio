from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # =========================
    # Application
    # =========================

    APP_NAME: str
    APP_ENV: str
    APP_HOST: str
    APP_PORT: int

    # =========================
    # Database
    # =========================

    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    # =========================
    # Security
    # =========================

    # SECRET_KEY: str
    # ALGORITHM: str
    # ACCESS_TOKEN_EXPIRE_MINUTES: int

    # =========================
    # CORS
    # =========================

    # CORS_ORIGINS: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


@lru_cache
def get_settings() -> Settings:
    """
    Charge le fichier .env une seule fois,
    puis retourne toujours la même instance.
    """
    return Settings()

if __name__ == "__main__" : 
    from pprint import pprint
    pprint(get_settings())