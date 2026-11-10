from base_service.base_service import BaseServiceBuilder, BaseService
from base_service.core.components.fastapi_component import FastAPIComponent
from base_service.core.enums.component_registry import ComponentRegistry
from example_app.routers import get_routes

class ExampleServiceBuilder(BaseServiceBuilder):
    """Example Service Builder"""

    def __init__(self):
        self._service = ExampleService()

    def build(self) -> "ExampleService":
        """Build the example service instance"""
        return self._service

class ExampleService(BaseService):
    """Example Service"""

    def __init__(self):
        super().__init__()

    async def bootstrap(self) -> None:
        """Perform any asynchronous setup required before running components."""

        app: FastAPIComponent = self.get_component(ComponentRegistry.FASTAPI)
        if app is None:
            raise RuntimeError("FastAPI component is not initialized.")

        for route in get_routes():
            app.add_api_router(route)

        