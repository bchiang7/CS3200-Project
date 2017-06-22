DROP DATABASE IF EXISTS top500Info;
CREATE DATABASE top500Info;
USE top500Info;

CREATE TABLE continent
(
 continent_name     VARCHAR(30)   PRIMARY KEY,
 climate 	  		VARCHAR(20)   NOT NULL
); 

CREATE TABLE country 
(
 cname 	            VARCHAR(100)	    PRIMARY KEY, 
 currencyName       VARCHAR(100),
 capital            VARCHAR(100),
 c_continent        VARCHAR(30),
 official_lang		VARCHAR(100),
CONSTRAINT region_fk FOREIGN KEY
(c_continent) REFERENCES continent (continent_name) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE attraction
(
 attract_id  		INT            PRIMARY KEY   AUTO_INCREMENT,
 name         		VARCHAR(100)    NOT NULL,
 description  		VARCHAR(200),
 category     		VARCHAR(45)    NOT NULL,
 origin       		ENUM('Man-made', 'Natural')   NOT NULL,
 countryN    		VARCHAR(30)	   NOT NULL,
CONSTRAINT loc_fk FOREIGN KEY
(countryN) REFERENCES country (cname) ON UPDATE CASCADE ON DELETE CASCADE
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

CREATE TABLE review
(
 review_id              INT PRIMARY KEY AUTO_INCREMENT,
 rdate  			 	DATE,
 overall_rating 		INT    CHECK(overall_rating<=10),
 family_rating 			INT    CHECK(family_rating<=10),
 adventure_rating 		INT    CHECK(adventure_rating<=10),
 subject 				INT,
 author 				INT,
CONSTRAINT author_fk FOREIGN KEY
(author) REFERENCES visitor (visitor_id) ON UPDATE CASCADE ON DELETE CASCADE,
CONSTRAINT review_fk FOREIGN KEY 
(subject) REFERENCES attraction (attract_id) ON UPDATE CASCADE ON DELETE CASCADE
);