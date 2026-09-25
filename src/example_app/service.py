"""Entry point for the example application."""
from logging import getLogger
from example_app import __service_name__

logger = getLogger(f"{__service_name__}.Main")


if __name__ == "__main__":
    logger.info("Starting the example application.")
    print("Hello, World!")