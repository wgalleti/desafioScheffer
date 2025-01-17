FROM python:3.12-alpine
LABEL authors="William Galleti <william.galleti@gmail.com>"

RUN \
  apk update && \
  apk add --no-cache gcc musl-dev python3-dev zlib-dev jpeg-dev libffi-dev gettext build-base &&\
  apk add --no-cache postgresql-dev

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV UV_PROJECT_ENVIRONMENT=/app/.venv

ENV PATH="/root/.local/bin/:$PATH"
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

COPY uv.lock  pyproject.toml ./
ADD --chmod=775 https://astral.sh/uv/install.sh /installer.sh
RUN sh /installer.sh && rm /installer.sh
RUN uv sync --frozen --no-install-project --no-dev

COPY . .

ENTRYPOINT []


