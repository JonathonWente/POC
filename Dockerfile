FROM python:3.4-alpine
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
CMD [ "python", "app.py" ]