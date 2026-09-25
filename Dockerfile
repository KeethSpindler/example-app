FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# git is needed to resolve the base-service VCS dependency, then removed to keep the image slim
RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && pip install "base-service @ git+https://github.com/KeethSpindler/base-service@master" \
    && apt-get purge -y --auto-remove git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install .

COPY . .

RUN useradd --create-home --uid 1000 app && chown -R app:app /app
USER app

## Run the example application service.py file
CMD ["python", "-m", "example_app.service"]
