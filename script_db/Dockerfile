FROM python:3.7-slim

WORKDIR /app

COPY . .

RUN pip3 install -r /app/requirements.txt --no-cache-dir

# RUN celery -A script_db worker --loglevel=info  --pool=solo

# RUN celery -A script_db beat -l INFO

# CMD ["gunicorn", "script_db.wsgi:application", "--bind", "0:8000" ]
