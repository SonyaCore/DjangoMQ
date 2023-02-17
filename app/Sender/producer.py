import json
import pika
import environ

env = environ.Env()
environ.Env.read_env()

connection = pika.BlockingConnection(
    pika.ConnectionParameters('rabbitmq' if env('MODE') == "container" else "localhost",
    heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='inbox', body=json.dumps(body), properties=properties)