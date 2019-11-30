# Use an official Python runtime as a parent image
FROM python:3.6-slim

RUN apt-get update
RUN apt-get install -y libpq-dev python3-dev build-essential postgresql-server-dev-all

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080


# Run app.py when the container launches
CMD ["python", "app.py"]