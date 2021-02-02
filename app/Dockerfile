FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN cp -f /code/app/.env.docker /code/app/.env

ENTRYPOINT [ "gunicorn"  , "-b", "0.0.0.0:8000", "app:app" ]
