# kafka_consumer.py
from confluent_kafka import Consumer, KafkaError

def consume_messages():
    consumer_conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'user-registration-consumers',  # Replace with your chosen group ID
        'auto.offset.reset': 'earliest'
    }

    consumer = Consumer(consumer_conf)
    consumer.subscribe(['user_registration_logs'])

    try:
        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break

            print('Received message: {}'.format(msg.value().decode('utf-8')))

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == "__main__":
    consume_messages()
