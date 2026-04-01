FROM python:3.12-slim-bullseye

# Install system dependencies.
RUN apt-get update && apt-get install -y --no-install-recommends make && rm -rf /var/lib/apt/lists/*

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy the application into the container.
COPY . /app

# Install the application dependencies.
WORKDIR /app
RUN uv sync --locked --no-group dev

EXPOSE 8000

# Run the application.
CMD ["make", "prod"]