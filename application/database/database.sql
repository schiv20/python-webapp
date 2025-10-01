CREATE DATABASE jokeapp;
USE jokeapp;

create table `user` (
	ID int primary key auto_increment,
	Email varchar(100) not null,
	Password varchar(100) not null
);

create table joke (
	ID int primary key auto_increment,
    the_joke varchar(2000) not null
);