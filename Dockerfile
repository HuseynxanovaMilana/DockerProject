# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt
COPY req.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r req.txt

# Copy the Django project files
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "DockerProject.wsgi:application", "--bind", "0.0.0.0:8000"]
