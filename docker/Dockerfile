# Dockerfile for Maths Python Streamlit App
# Multi-stage build optimised for minimal image size
# syntax=docker/dockerfile:1

# Stage 1: Builder - install dependencies
FROM python:3.13-slim-bookworm AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \n    build-essential \n    && rm -rf /var/lib/apt/lists/*

# Install uv for faster dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies to a virtual environment with BuildKit cache
RUN --mount=type=cache,target=/root/.cache/uv \n    uv venv /opt/venv && \n    . /opt/venv/bin/activate && \n    uv export --no-dev --format requirements-txt > requirements.txt && \n    uv pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime - minimal image
FROM python:3.13-slim-bookworm

WORKDIR /app

# Install only runtime dependencies (curl for health checks)
RUN apt-get update && apt-get install -y --no-install-recommends \n    curl \n    && apt-get clean \n    && rm -rf /var/lib/apt/lists/*

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy application code
COPY app/ ./app/

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash appuser && \n    chown -R appuser:appuser /app
USER appuser

# Expose Streamlit default port
EXPOSE 8501

# Health check for load balancers
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \n    CMD curl --fail http://localhost:8501/maths/_stcore/health || exit 1

# Run Streamlit
ENTRYPOINT ["streamlit", "run", "app/maths_python.py", \n    "--server.port=8501", \n    "--server.address=0.0.0.0", \n    "--server.headless=true", \n    "--server.baseUrlPath=maths", \n    "--browser.gatherUsageStats=false"]