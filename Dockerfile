# Dockerfile
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN Daphne (ASGI server)
CMD ["daphne", "-b", "0.0.0.0", "-p", "8080", "smartlight_backend.asgi:application"]
