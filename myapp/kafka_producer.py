from confluent_kafka import Producer

def produce_message(topic, message):
    producer = Producer({'bootstrap.servers': 'localhost:9092'})

    def delivery_report(err, msg):
        if err is not None:
            print(f'Message delivery failed: {err}')
        else:
            print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

    producer.produce(topic, message, callback=delivery_report)
    producer.poll(0)
    producer.flush()
