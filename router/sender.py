import pika
import json

data = {
    "tg_id": 794853716,
    "social_media": "tg",
    "text": "Открыт новый урок"
}

# Устанавливаем соединение с сервером
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Создание очереди
channel.queue_declare(queue='data_to_send')

# Отправка сообщения в точку обмена exchange
channel.basic_publish(exchange='', routing_key='data_to_send', body=json.dumps(data))
print(f" [x] Sent {json.dumps(data)}")

connection.close()
