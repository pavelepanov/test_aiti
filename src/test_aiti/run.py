from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from test_aiti.entrypoint.config import create_config
from test_aiti.entrypoint.ioc import create_async_ioc_container
from test_aiti.entrypoint.setup import (
    configure_app,
    create_app,
)
from test_aiti.infrastructure.persistence_sqla.mappings.map import map_tables
from test_aiti.presentation.http.root_router import root_router


def make_app() -> FastAPI:
    config = create_config()

    app = create_app()
    map_tables()
    configure_app(app=app, root_router=root_router)

    setup_dishka(container=create_async_ioc_container(config=config), app=app)

    return app
