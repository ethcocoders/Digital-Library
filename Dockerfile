# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Add the current directory contents into the container at /app
COPY ./backend /app/backend
COPY ./frontend /app/frontend

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# Install Node.js and npm for frontend build
RUN apt-get update && apt-get install -y nodejs npm

# Build frontend
RUN cd /app/frontend && npm install && npm run build

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=backend/app.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
