FROM alpine:latest AS builder
EXPOSE 8080
WORKDIR /app 
COPY requirements.txt /app

RUN apk add --no-cache python3 bash py3-pip && \
    pip3 install -r requirements.txt --no-cache-dir && \
    apk del python3

COPY . /app
RUN wget -O wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh
RUN chmod +x wait-for-it.sh
RUN chmod +x consumer.py

ENTRYPOINT ["/bin/bash" , "-c"]
# CMD ["/app/wait-for-it.sh rabbitmq:5672 --timeout=30 -- python3 manage.py runserver 8080"]