# Use an official Python runtime as the base image
FROM python:3.10-slim-buster

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.3.1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
COPY pyproject.toml /app

# Install Poetry
RUN pip3 install poetry
RUN poetry config virtualenvs.create false

# # Use Poetry to install the required packages
RUN poetry install --only main


# Set the environment variable for Streamlit
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Expose the default Streamlit port
EXPOSE 8501

WORKDIR /app/aloha_team_sai

# Run the Streamlit command
CMD ["streamlit", "run", "🌺_Home.py", "--server.port=8501", "--server.address=0.0.0.0"]
