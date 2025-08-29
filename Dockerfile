FROM python:3.13

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./mysite .

CMD python manage.py migrate && \
    python manage.py create_simple_user && \
    uvicorn mysite.asgi:application --host 0.0.0.0 --port 8000

