from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI


def create_app() -> FastAPI:
    app = FastAPI()

    return app


def configure_app(app: FastAPI, root_router: APIRouter) -> None:
    app.include_router(root_router)
