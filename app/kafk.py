from kafka import KafkaProducer
import json
import datetime

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


def log_event(user_id: int, action: str):
    event = {
        'user_id': user_id,
        'action': action,
        'timestamp': datetime.datetime.now().isoformat()
    }
    producer.send('insurance-events', event)
