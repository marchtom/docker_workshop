FROM python:3.6-slim

ADD . /code

WORKDIR /code

RUN pip install flask

EXPOSE 5000

CMD ["python", "flaskAPI.py"]
