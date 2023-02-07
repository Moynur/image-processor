FROM python:3.11.1
# Or any preferred Python version.
COPY . .
RUN pip install -r requirements.txt
CMD [“python”, “./main.py”] 