from dataclasses import dataclass
from os import getenv

from dotenv import load_dotenv

load_dotenv()


@dataclass
class PostgresConfig:
    host: str
    port: int
    db: str
    user: str
    password: str

    uri: str

    @staticmethod
    def from_env() -> "PostgresConfig":
        host = getenv("BACKEND_POSTGRES_HOST")
        port = getenv("BACKEND_POSTGRES_PORT")
        db = getenv("BACKEND_POSTGRES_DB")
        user = getenv("BACKEND_POSTGRES_USER")
        password = getenv("BACKEND_POSTGRES_PASSWORD")

        uri = f"postgresql+psycopg://{user}:{password}@{host}:{port}/{db}"

        return PostgresConfig(
            uri=uri, host=host, port=port, db=db, user=user, password=password
        )


@dataclass
class Config:
    postgres_config: PostgresConfig


def create_config() -> Config:
    return Config(
        postgres_config=PostgresConfig.from_env(),
    )
