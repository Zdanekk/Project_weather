FROM python:3.11

WORKDIR /app

RUN pip install Flask markupsafe pandas pmdarima

COPY . .

EXPOSE 5001

CMD ["python", "app_with_csv.py"]

