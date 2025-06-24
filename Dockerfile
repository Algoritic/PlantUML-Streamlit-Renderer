# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable for PlantUML server URL
# This can be overridden when running the container or via docker-compose
ENV PLANTUML_SERVER_URL="http://plantuml-server:8080"

# Run streamlit when the container launches
ENTRYPOINT ["streamlit", "run", "plantuml_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
