FROM python:3.8-alpine
COPY ./subscriber.py .
RUN pip install kafka-python
RUN pip install mysql-connector.python
CMD python consumer.py $TOPIC
