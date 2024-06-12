FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY requirements.txt .

EXPOSE 5001

CMD ["python", "app_with_csv.py"]

