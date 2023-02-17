import json
import pika
import django
from sys import path
from os import environ


environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangomq.settings')
django.setup()

import environ
env = environ.Env()
environ.Env.read_env()

from Inbox.models import Inbox

connection = pika.BlockingConnection(
    pika.ConnectionParameters('rabbitmq' if env('MODE') == "container" else "localhost",
    heartbeat=600, blocked_connection_timeout=300))

channel = connection.channel()
channel.queue_declare(queue='inbox')

def callback(ch, method, properties, body):
    print("Received in Inbox...")
    print(body)
    data = json.loads(body)
    print(data)

    if properties.content_type == 'message_created':
        inbox = Inbox.objects.create(id=data['id'],
        subject=data['subject'],
        email=data['email'],
        message=data['message']
        )
        inbox.save()
        print("message created")
    elif properties.content_type == 'message_updated':
        inbox = Inbox.objects.get(id=data['id'])
        inbox.subject = data['subject']
        inbox.email = data['email']
        inbox.message = data['message']

        inbox.save()
        print("message updated")
    elif properties.content_type == 'message_deleted':
        quote = Inbox.objects.get(id=data)
        quote.delete()
        print("message deleted")
channel.basic_consume(queue='inbox', on_message_callback=callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()