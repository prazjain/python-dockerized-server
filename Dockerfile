FROM python:3.12-alpine

WORKDIR /app 

COPY requirements.txt /app/
COPY ./src /app/src

RUN pip install -r requirements.txt 

CMD [ "python", "./src/main.py"]