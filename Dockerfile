# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
COPY entrypoint.sh /
RUN pip install -r requirements.txt
RUN chmod +x /entrypoint.sh
COPY . /code/
