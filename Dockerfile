FROM python:3.6.9-alpine3.9
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY send.py .
ENTRYPOINT python send.py
