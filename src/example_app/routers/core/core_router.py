from fastapi import APIRouter
from example_app import __version__


def get_core_router() -> APIRouter:
    router = APIRouter()

    @router.get("/health")
    async def health_check():
        return {"status": "ok"}

    @router.get("/info")
    async def info():
        return {"app": "example_app", "version": __version__}

    return router