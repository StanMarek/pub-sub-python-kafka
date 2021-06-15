from confluent_kafka import Producer
import time
import random

broker = 'localhost:29092'
config = {
    'bootstrap.servers': broker
}
topic = 'temperature'

def message_info(message, error):
    if error is not None:
        print(f'ERROR-{error}')
    else:
        print(f'MESSAGE HAS BEEN SENT\tTOPIC-{message.topic()}\tPARTITION-{message.partition()}')

def generate_temperature():
    temp = random.randint(0,1000)
    return temp

def main():
    producer = Producer(config)
    run = True
    while (run):
        producer.poll(0)
        producer.produce(topic, format(generate_temperature(), '.2f').encode('utf-8'), callback=message_info)
        time.sleep(1)
        producer.flush()

if __name__ == '__main__':
    main()
