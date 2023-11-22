FROM python:slim

RUN python -m venv /venv

COPY requirements.txt requirements.txt
RUN /venv/bin/python -m pip install -r requirements.txt

COPY src /src

WORKDIR /src

RUN /venv/bin/python manage.py migrate
RUN /venv/bin/python manage.py collectstatic

ENV DJANGO_DEBUG_OFF=1

CMD ["/venv/bin/gunicorn", "--bind", ":80", "superlists.wsgi:application"]
