FROM python:3.10-slim

ARG APP_VERSION
ENV APP_VERSION=$APP_VERSION

WORKDIR /hivebox-app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]