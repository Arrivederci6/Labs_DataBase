-- Country
DELIMITER //

DROP TRIGGER IF EXISTS prevent_modification_country;
CREATE TRIGGER prevent_modification_country
BEFORE UPDATE ON country
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Data modification is not allowed';
END;

//


DROP TRIGGER IF EXISTS prevent_deletion_country;
CREATE TRIGGER prevent_deletion_country
BEFORE DELETE ON accuweather.country
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Deleting rows from the user table is not allowed';
END;
//
DELIMITER ;
