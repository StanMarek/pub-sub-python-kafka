FROM mysql
ENV MYSQL_ALLOW_EMPTY_PASSWORD=true
COPY ./database_schema.sql /docker-entrypoint-initdb.d/
