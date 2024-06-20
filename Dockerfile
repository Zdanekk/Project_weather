FROM python:3.11-slim

RUN python3 -m venv .venv

WORKDIR /app

RUN pip install Flask pandas pmdarima scikit-learn markupsafe==2.0.1 numpy==1.26.4

COPY . .

EXPOSE 5001

CMD ["python", "app_with_csv.py"]

