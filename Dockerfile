# Use a base image with Python
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the project files into the container
COPY . .

# Command to run the Flask application
CMD ["python", "src/app.py"]
