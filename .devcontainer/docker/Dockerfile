FROM mcr.microsoft.com/devcontainers/base:ubuntu24.04

LABEL org.opencontainers.image.source=https://github.com/fhuitelec/fizzbuzz-kata
LABEL org.opencontainers.image.version=ubuntu24.04
LABEL org.opencontainers.image.documentation=https://github.com/fhuitelec/fizzbuzz-kata

RUN apt update \
    && apt install -y \
        vim \
        curl \
        gnupg \
        wget \
        software-properties-common \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:0.6 /uv /bin/uv
RUN uv python install 3.13
