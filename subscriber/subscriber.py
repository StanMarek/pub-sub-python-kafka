from confluent_kafka import Consumer
import mysql.connector as connector
from mysql.connector import errorcode
import datetime as dt
import math

consumer_config = {
    'group.id':'clientId',
    'bootstrap.servers':"localhost:29092",
    'auto.offset.reset':"smallest",
    'enable.auto.commit':True
}

database_config = {
    'user':'pubsub',
    'password':'pubsub',
    'host':'127.0.0.1',
    'database':'lab4_kafka',
    'raise_on_warnings':True
}

connection = connector.connect(**database_config)
insert = ("insert into temperature(average, pressure, time_of_insert, total) values (%s, %s, %s, %s)")

def insert_into_database(value, pressure, amount):
    row = (value, pressure, dt.datetime.now(), amount)
    cursor = connection.cursor()
    cursor.execute(insert, row)
    measure = cursor.lastrowid
    connection.commit()
    cursor.close()
    return dt.datetime.now()

def pressure_from_temperature(temperature):
    p0 = 611.213 # p0 = 6.11213 hPa
    t = temperature + 273.15
    x = (17.5043*t)/(241.2+t)
    return p0*math.exp(x)

def main():
    print('LAB-4_KAFKA-PUB-SUB')
    consumer = Consumer(consumer_config)
    consumer.subscribe(['temperature'])
    run = True
    measurements = 0
    sum_of_measures = 0
    dT = 10
    while run:
        message = consumer.poll(timeout=5.0)
        if message is not None:
            measurements += 1
            sum_of_measures += float(message.value().decode('utf-8'))
            if(measurements % dT == 0):
                average = sum_of_measures/dT
                pressure_at_avg = pressure_from_temperature(average) 
                current_time = insert_into_database(average, pressure_at_avg, measurements)
                print(f"INSERTED: {average}\t at: {current_time}\t STAN_MAREK")
                sum_of_measures = 0

        else:
            continue

if __name__ == '__main__':
    main()

