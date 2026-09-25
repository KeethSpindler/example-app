import os
from importlib.metadata import version
from base_service.core.util.logging import instantiate_logger

__service_name__ = "ExampleApp"
__version__ = version("example-app")
__logging_level__ = os.getenv("LOGGING_LEVEL", "INFO")

instantiate_logger(__service_name__, __logging_level__)