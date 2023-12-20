# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /app
WORKDIR /usr/src/apaksha

# Copy the entire content of the local docker_gps directory into the container at /app
COPY . /usr/src/apaksha


RUN apt-get update && \
    apt-get install -y --no-install-recommends unixodbc unixodbc-dev curl gnupg && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql17 && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 80



# Specify the command to run on container start
CMD ["python", "gps_data.py"]
