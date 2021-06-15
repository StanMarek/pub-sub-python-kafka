create user if not exists 'pubsub'@'localhost' identified by 'pubsub';
grant all privileges on * . * to pubsub;
create database if not exists lab4_kafka;

use lab4_kafka;

drop table if exists temperature;

create table temperature(
	id int primar key auto_increment,
	average float,
	pressure float,
	time_of_insert datetime,
	total int
);
