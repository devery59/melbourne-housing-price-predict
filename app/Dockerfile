FROM python:3.9-slim

# Set Working Directory
WORKDIR /app

# Copy Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy App Code
COPY . .

# Expose Port
EXPOSE 8000

# Run App
CMD ["uvicorn", "serve:app", "--host", "0.0.0.0", "--port", "8080"]
