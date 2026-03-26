# Microsoft Python Dev Container image
FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set environment variables for uv
ENV UV_LINK_MODE=copy
ENV UV_COMPILE_BYTECODE=1