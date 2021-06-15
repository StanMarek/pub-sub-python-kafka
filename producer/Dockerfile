FROM python:3.8-alpine
COPY ./producer.py .
RUN pip install kafka-python
CMD python producer.py $TOPIC
