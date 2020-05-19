FROM python:latest
RUN python models.py

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install werkzeug==0.16.1
RUN pip install -r requirements.txt

COPY . /code

CMD ["flask", "run", "--host=0.0.0.0"]

RUN python models.py