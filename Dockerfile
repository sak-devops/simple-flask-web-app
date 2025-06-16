FROM python:3.11-slim

WORKDIR /usr/app

COPY  . .

RUN pip install -r requirements.txt

COPY . .

RUN useradd app
USER app

CMD [ "python", "app.py" ]