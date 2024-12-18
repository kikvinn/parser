# Dockerfile
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY ./app /app
COPY ./db /app/db
COPY Pipfile* /app/

# Install dependencies
RUN pip install pipenv && pipenv sync --system --deploy

# Expose port for Flask
EXPOSE 5000

# Run the application
CMD ["python", "server.py"]