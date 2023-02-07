# Use an Alpine base image
FROM python:3.11-alpine

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the necessary dependencies
RUN apk add --no-cache build-base && \
    apk add --no-cache --virtual .build-deps \
        python3-dev && \
    pip install -r requirements.txt && \
    apk del .build-deps 
RUN apk add tesseract-ocr

# Copy the application files
COPY . .

# Set the default command to run the app
CMD ["python","-u","app.py"]
