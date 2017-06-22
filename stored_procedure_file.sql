USE top500Info;


-- Procedure new_visitor processes information necessary
-- for the creation of a new visitor in the visitor relation
-- and returns the visitor id number  
-- 
-- Assumes country data validation ensured via drop-down menu

DROP PROCEDURE IF EXISTS new_visitor;
DELIMITER $$
CREATE PROCEDURE new_visitor(IN nameF VARCHAR(20), IN nameL CHAR(1), IN inage INT,
IN homeCountry VARCHAR(30))
BEGIN

 INSERT INTO visitor (first_name, last_initial, age, home_country) 
 VALUES (nameF, nameL, inage, homeCountry);

 SELECT visitor_id AS your_id 
 FROM visitor WHERE 
   first_name = nameF AND
   last_initial=nameL AND 
   age = inage AND
   home_country = homeCountry
   LIMIT 1;
   
END
$$ DELIMITER ;


-- Procedure update_visitor processes information necessary
-- to update an existing visitor in the visitor relation
-- 
-- Assumes country data validation ensured via drop-down menu

DROP PROCEDURE IF EXISTS update_visitor;
DELIMITER $$
CREATE PROCEDURE update_visitor(IN id INT, IN nameF VARCHAR(20), IN nameL CHAR(1), IN inage INT,
IN homeCountry VARCHAR(30))
BEGIN

 UPDATE visitor 
 SET first_name = nameF, last_initial = nameL, age = inage, home_country = homeCountry
 WHERE visitor_id = id;

END
$$ DELIMITER ;



-- Procedure delete_visitor deletes an existing visitor
-- in the visitor relation based on visitor_id
-- 
-- Assumes country data validation ensured via drop-down menu

DROP PROCEDURE IF EXISTS delete_visitor;
DELIMITER $$
CREATE PROCEDURE delete_visitor(IN id INT)
BEGIN

 DELETE FROM visitor WHERE visitor_id = id;

END
$$ DELIMITER ;




/*
Procedure new_review processes information necessary
for the creation of a new review in the review relation 

Assumes visitor (author) and attraction (subject) validated in front end code

Note: 
user will select/type in the name of the location that they're reviewing,
but we need the attraction id in order to create an entry in the review table.
--> must do join to get attraction.attract_id based on attraction.name
--> we need to do data validation with attraction table ANYWAY, so we could (1) retrieve
    attract_id then and pass it into this parameter OR (2) pass in name, 
    find ID from join inside this parameter

*/

DROP PROCEDURE IF EXISTS new_review;
DELIMITER $$
CREATE PROCEDURE new_review(IN date_of_review DATE, IN author_id INT, IN attraction_id INT,
IN overall INT, IN family INT, IN adventure INT)
BEGIN

	DECLARE Roverall INT;
    DECLARE Rfamily INT;
    DECLARE Radventure INT;
    
    IF (overall > 10)
     THEN SET Roverall = 10;
     ELSE SET Roverall = overall;
	END IF;
    
    IF (family > 10)
     THEN SET Rfamily = 10;
     ELSE SET Rfamily = family;
	END IF;
    
    IF (adventure > 10)
     THEN SET Radventure = 10;
     ELSE SET Radventure = adventure;
	END IF;
		

 INSERT INTO review (rdate, overall_rating, family_rating, adventure_rating, subject, author) 
 VALUES (date_of_review, Roverall, Rfamily, Radventure, attraction_id, author_id);

END
$$ DELIMITER ;


-- Procedure delete_visitor deletes an existing review
-- in the review relation based on visitor_id

DROP PROCEDURE IF EXISTS delete_review;
DELIMITER $$
CREATE PROCEDURE delete_review(IN id INT)
BEGIN

 DELETE FROM review WHERE review_id = id;

END
$$ DELIMITER ;