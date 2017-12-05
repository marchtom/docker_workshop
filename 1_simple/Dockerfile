FROM python:2.7

ADD . /code

RUN pip install flask

WORKDIR /code

EXPOSE 5000

CMD ["python", "flaskAPI.py"]
