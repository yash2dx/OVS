
FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir ./project

WORKDIR /project

COPY requirements.txt /project/

RUN pip install -r requirements.txt

# will have the entire project
COPY . /project/