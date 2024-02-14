# syntax=docker/dockerfile:1

# Set container base image, from which build our image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy script to working dir 
COPY main.py /app

# Run the script through python
CMD ["python", "main.py"]
