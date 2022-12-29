FROM python:3.10

ENV PYTHONBUFFERED 1

WORKDIR /todolist

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY todolist/ .

EXPOSE 8000

CMD ['python', 'manage.py', 'runserver', '0.0.0.0:8000']

