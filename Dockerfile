FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y tesseract-ocr libgl1 libglib2.0-0 tesseract-ocr-por && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
