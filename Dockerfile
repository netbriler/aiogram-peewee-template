# preparatory actions stage
FROM python:3.11-slim-buster as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libc-dev libffi-dev python3-dev musl-dev

RUN pip install virtualenv

RUN virtualenv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

# final stage
FROM python:3.11-slim-buster

RUN addgroup --system app && adduser --system --group app --home /app

COPY --from=builder /opt/venv /opt/venv

WORKDIR /app

ENV PATH="/opt/venv/bin:$PATH"

COPY . .

RUN chown -R app:app ./* && chmod -R 777 ./*

USER app

ENTRYPOINT ['/bin/entrypoint.sh']