FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /test_aiti

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

ADD . /test_aiti
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install .

ENV PATH="/test_aiti/.venv/bin:$PATH"
