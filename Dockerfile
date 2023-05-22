# Use a Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the solution files to the working directory
COPY . .

# Specify the command to run when the container starts
CMD ["python", "watch_next.py"]

