# Dockerfile
FROM python:3.11.1

WORKDIR /image-processor

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .

CMD ["python", "main.py"]