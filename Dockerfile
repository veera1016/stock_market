# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and requests
RUN pip install --no-cache-dir Flask requests

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
