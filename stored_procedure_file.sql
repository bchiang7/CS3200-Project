USE top500Info;

/*
Procedure new_visitor processes information necessary
for the creation of a new visitor in the visitor relation
and returns the visitor id number  

Assumes country data validation ensured via drop-down menu
*/

DROP PROCEDURE IF EXISTS new_visitor;
DELIMITER //
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
// DELIMITER ;



/*
Procedure new_review processes information necessary
for the creation of a new review in the review relation 

Assumes visitor (author) and attraction (subject) validated in front end code

*/

DROP PROCEDURE IF EXISTS new_review;
DELIMITER //
CREATE PROCEDURE new_review(IN author_id INT, IN attraction_name VARCHAR(100),
IN overall INT, IN family INT, IN adventure INT)
BEGIN

	DECLARE Roverall INT;
    DECLARE Rfamily INT;
    DECLARE Radventure INT;
    
    DECLARE locationID INT;

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
    
    SELECT attract_id INTO locationID
    FROM attraction 
    WHERE name = attraction_name
    LIMIT 1;
    

  INSERT INTO review (rdate, overall_rating, family_rating, adventure_rating, subject, author) 
  VALUES (NOW(), Roverall, Rfamily, Radventure, locationID, author_id);

END
// DELIMITER ;
