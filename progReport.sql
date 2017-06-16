DROP DATABASE IF EXISTS top500Info;
CREATE DATABASE top500Info;
USE top500Info;

CREATE TABLE region
(
loc_id        INT         PRIMARY KEY    AUTO_INCREMENT,
climate 	  VARCHAR(20) NOT NULL
); 

CREATE TABLE country 
(
cname 	     VARCHAR(30)	PRIMARY KEY, 
continent    ENUM('Asia', 'North America', 'South America', 'Europe', 'Africa', 'Antarctica', 'Oceania'),
official_lang		VARCHAR(30),
exchange_rate 	    DECIMAL(11,2),
cregion             INT,
CONSTRAINT region_fk FOREIGN KEY
(cregion) REFERENCES region (loc_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE visitor
(
visitor_id     INT PRIMARY KEY AUTO_INCREMENT,
first_name     VARCHAR(20),
last_initial   CHAR(1),
age            INT,
home_country   VARCHAR(30),
CONSTRAINT country_fk FOREIGN KEY
(home_country) REFERENCES country (cname) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE attraction
(
attract_id  		INT            PRIMARY KEY   AUTO_INCREMENT,
name         		VARCHAR(60)    NOT NULL,
description  		VARCHAR(100),
category     		VARCHAR(45)    NOT NULL,
origin       		ENUM('Man-made', 'Natural')   NOT NULL,
countryN    		VARCHAR(30)	   NOT NULL,
continentN          VARCHAR(30),    
attendance_cost 	DECIMAL(11,2),
costFromBOS  		DECIMAL(11,2),
CONSTRAINT loc_fk FOREIGN KEY
(countryN) REFERENCES country (cname) ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE review
(
review_id           INT PRIMARY KEY AUTO_INCREMENT,
rdate  			 	DATE,
overall_rating 		INT,
family_rating 		INT,
adventure_rating 	INT,
subject 			INT,
author 				INT,
CONSTRAINT author_fk FOREIGN KEY
(author) REFERENCES visitor (visitor_id) ON UPDATE CASCADE ON DELETE CASCADE,
CONSTRAINT review_fk FOREIGN KEY 
(subject) REFERENCES attraction (attract_id) ON UPDATE CASCADE ON DELETE CASCADE
);

