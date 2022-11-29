FROM python:3.10.7-alpine3.16

RUN apk add --update \
    build-base libffi-dev openssl-dev \
    xmlsec xmlsec-dev \
  && rm -rf /var/cache/apk/*

ADD requirements.txt /tmp
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

EXPOSE 9001
CMD python manage.py runserver 0.0.0.0:9001
