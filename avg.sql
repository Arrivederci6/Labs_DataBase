-- Functions for weather_forecast table
DROP FUNCTION IF EXISTS GetMaxTemperature;
DROP FUNCTION IF EXISTS GetMinTemperature;
DROP FUNCTION IF EXISTS GetAvgTemperature;
DROP FUNCTION IF EXISTS GetSumTemperature;

DELIMITER //

CREATE FUNCTION GetMaxTemperature() RETURNS DECIMAL(2,0)
DETERMINISTIC
BEGIN
    DECLARE max_value DECIMAL(2,0);
    SELECT MAX(temperature) INTO max_value FROM weather_forecast;
    RETURN max_value;
END //

CREATE FUNCTION GetMinTemperature() RETURNS DECIMAL(2,0)
DETERMINISTIC
BEGIN
    DECLARE min_value DECIMAL(2,0);
    SELECT MIN(temperature) INTO min_value FROM weather_forecast;
    RETURN min_value;
END //

CREATE FUNCTION GetAvgTemperature() RETURNS DECIMAL(2,0)
DETERMINISTIC
BEGIN
    DECLARE avg_value DECIMAL(2,0);
    SELECT AVG(temperature) INTO avg_value FROM weather_forecast;
    RETURN avg_value;
END //

CREATE FUNCTION GetSumTemperature() RETURNS DECIMAL(5,2)
DETERMINISTIC
BEGIN
    DECLARE sum_value DECIMAL(5,2);
    SELECT SUM(temperature) INTO sum_value FROM weather_forecast;
    RETURN sum_value;
END //

DELIMITER ;

-- Procedure for weather_forecast table
DROP PROCEDURE IF EXISTS PerformTemperatureOperations;

DELIMITER //

CREATE PROCEDURE PerformTemperatureOperations()
BEGIN
    DECLARE max_value DECIMAL(2,0);
    DECLARE min_value DECIMAL(2,0);
    DECLARE avg_value DECIMAL(2,0);
    DECLARE sum_value DECIMAL(5,2);

    SET max_value = GetMaxTemperature();
    SET min_value = GetMinTemperature();
    SET avg_value = GetAvgTemperature();
    SET sum_value = GetSumTemperature();

    SELECT max_value AS MaxTemperature,
           min_value AS MinTemperature,
           avg_value AS AvgTemperature,
           sum_value AS SumTemperature;
END //

DELIMITER ;

-- Call the procedure
CALL PerformTemperatureOperations();
