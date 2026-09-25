# example-app

A minimal reference application demonstrating how to consume the
[`base_service`](https://github.com/KeethSpindler/base-service) package.

`base_service` provides a `BaseService` container and `BaseComponent` interface
for building component-driven microservices; it's meant to be inherited and
extended rather than run directly. This project shows the smallest realistic
consumer: installing the package, bootstrapping it at import time, and
packaging the result into a container.

## What this project demonstrates

- **Installing `base_service` from Git** — it isn't published to PyPI, so it's
  pulled from the GitHub URL (see [Dockerfile](Dockerfile)).
- **Bootstrapping shared utilities on import** — [src/example_app/\_\_init\_\_.py](src/example_app/__init__.py)
  calls `base_service.core.util.logging.instantiate_logger` with the service
  name and a `LOGGING_LEVEL` environment variable, so any module can call
  `getLogger(__service_name__)` and get a pre-configured logger.
- **Exposing service metadata** — `__service_name__` and `__version__` are
  defined once at package level.
- **A conventional entry point** — [src/example_app/service.py](src/example_app/service.py)
  is the module executed by the container.

## Layout

```
src/example_app/
  __init__.py    # service metadata + logger bootstrap via base_service
  service.py     # entry point
tests/
pyproject.toml
Dockerfile
```

## Requirements

Python 3.13+ (inherited from `base_service`).

## Local development

```bash
pip install "base_service @ git+https://github.com/KeethSpindler/base-service@master"
pip install -e .
python -m example_app.service
```

## Running the tests

```bash
pip install -e . --group dev
pytest
```

## Container

```bash
docker build . -t example-app:v0.1.0
docker run --rm -it example-app:v0.1.0
```

## Configuration

| Variable | Default | Description |
| --- | --- | --- |
| `LOGGING_LEVEL` | `INFO` | Log level passed to `instantiate_logger` |
