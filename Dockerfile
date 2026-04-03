# Use official Python image
FROM python:3.10-slim

WORKDIR /app

# Install Flask
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY app1.py .

EXPOSE 5000

CMD ["python", "app1.py"]

