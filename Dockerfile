# Use an official Python runtime as a parent image
FROM python:3.10.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app's code into the container
COPY . /app

# Expose the port the app runs on
EXPOSE 8050

# Define environment variables (optional, depending on your setup)
ENV PYTHONPATH "${PYTHONPATH}:/app/src"

# Run the application
CMD ["python", "main.py"]