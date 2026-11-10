"""Entry point for the example application."""
from logging import getLogger
from example_app import __service_name__
from example_app.core.service import ExampleServiceBuilder, ExampleService

logger = getLogger(f"{__service_name__}.Main")

def construct_service():
    """
    Constructs the example service.
    
    Retrieves the necessary components and configurations from the base service.

    Args:
        None
    Returns:
        None
    """
    logger.info("Constructing the example service...")
    service = ExampleServiceBuilder().with_fastapi().build()
    logger.info("Example service constructed successfully.")
    return service
    


if __name__ == "__main__":
    logger.info("Starting the example application.")
    service = construct_service()
    service.run()
