FROM ghcr.io/keethspindler/base-service:v0.1.0

USER root

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install .

COPY . .

RUN chown -R app:app /app
USER app

## Run the example application service.py file
CMD ["python", "-m", "example_app.service"]
