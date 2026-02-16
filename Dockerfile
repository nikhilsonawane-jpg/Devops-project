# Lightweight base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy dependencies first (layer caching best practice)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose application port
EXPOSE 5000

# Start application
CMD ["python", "app.py"]

