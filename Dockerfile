# syntax=docker/dockerfile:1
FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN --mount=type=cache,id=cache-key/pipcache,target=/root/.cache pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
