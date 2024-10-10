# Use the official Python image as the base image
FROM python:3.11-slim-buster

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code into the container
COPY . /app/

# Expose port 8000 to allow external access
EXPOSE 8000

# Define the command to run your app using the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
