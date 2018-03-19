FROM python:3

ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD requirements.txt /app/
ADD . /app
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN pip install -r requirements.txt