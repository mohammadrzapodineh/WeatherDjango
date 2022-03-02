FROM python:3.9
LABEL maintainer = "mohammadrzapodineh@gmail.com"
LABEL version="1.0"
WORKDIR /code/
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/