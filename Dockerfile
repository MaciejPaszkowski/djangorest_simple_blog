FROM python:3.10

WORKDIR /app
ENV PYTHONPATH /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libc-dev \
    postgresql-client \
    gettext \
    netcat \
    && rm rm -rf /varlib/apt/lists/*

COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
RUN pip3 install git+https://github.com/seomoz/shovel

COPY . /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONNUNBUFFERED=1

EXPOSE 8000
ENTRYPOINT ["shovel"]
CMD ["run_api_dev"]
