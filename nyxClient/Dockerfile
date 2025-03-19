# Use an official Python image as a base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy only the requirements.txt first, and install dependencies
COPY requirements.txt /app/

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy only the source code files that are likely to change frequently
COPY src/ /app/src/

# Expose the port for the app to be accessible
EXPOSE 8080

# Define the command to run your application
CMD ["python", "./src/nyxmaster-client.py"]
