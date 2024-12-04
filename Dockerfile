FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/app
ENV FLASK_APP=src.app

CMD flask run --host=0.0.0.0 --port=8000 --reload --debugger
