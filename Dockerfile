
# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and the API files to the working directory
COPY requirements.txt .
COPY /app .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Expose the port on which the FastAPI server will run
EXPOSE 80

# Start the FastAPI server
ENTRYPOINT ["uvicorn","app:app","--host","0.0.0.0", "--port", "80"]