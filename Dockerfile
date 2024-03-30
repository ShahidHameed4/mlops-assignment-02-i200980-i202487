# Use the official Python image as a base
FROM python:3.9-slim AS base

# Set the working directory in the container
WORKDIR /app

# Copy just the requirements file to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Second stage for actual application code
FROM base AS app

# Copy the rest of the application code
COPY . .

# Expose port 5000 to the outside world
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
