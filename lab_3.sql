-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema AccuWeather
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `AccuWeather`;
CREATE SCHEMA IF NOT EXISTS `AccuWeather` DEFAULT CHARACTER SET utf8 ;
USE `AccuWeather`;

-- -----------------------------------------------------
-- Table `AccuWeather`.`country`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `country`;
CREATE TABLE `country` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `country_name` VARCHAR(45) NOT NULL,
  `longtitude` DOUBLE NOT NULL,
  `latitude` DOUBLE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_country_name` (`country_name` ASC) VISIBLE,
  INDEX `idx_location` (`longtitude`, `latitude`) VISIBLE
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `AccuWeather`.`region`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `region`;
CREATE TABLE `region` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `country_id` INT NOT NULL,
  `region_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `country_id_idx` (`country_id` ASC) VISIBLE,
  INDEX `idx_region_name` (`region_name` ASC) VISIBLE,
  INDEX `idx_country_and_region` (`country_id`, `region_name`) VISIBLE,
  CONSTRAINT `country_id`
    FOREIGN KEY (`country_id`)
    REFERENCES `country` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE = InnoDB;


DROP TABLE IF EXISTS `city`;
CREATE TABLE `city` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `region_id` INT NOT NULL,
  `city_name` VARCHAR(45) NOT NULL,
  `latitude` DOUBLE NOT NULL,
  `longtitude` DOUBLE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `region_id_idx` (`region_id` ASC) VISIBLE,
  INDEX `idx_city_name` (`city_name` ASC) VISIBLE,
  INDEX `idx_coordinates` (`latitude`, `longtitude`) VISIBLE,
  CONSTRAINT `region_id`
    FOREIGN KEY (`region_id`)
    REFERENCES `region` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `AccuWeather`.`air_quality`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `air_quality`;
CREATE TABLE `air_quality` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `city_id` INT NOT NULL,
  `date` DATE NOT NULL,
  `air_quality` DECIMAL(3,0) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_air_quality_city_id_idx` (`city_id` ASC) VISIBLE,
  INDEX `idx_air_quality_date` (`date` ASC) VISIBLE,
  INDEX `idx_city_and_date` (`city_id`, `date`) VISIBLE,
  CONSTRAINT `fk_air_quality_city_id`
    FOREIGN KEY (`city_id`)
    REFERENCES `city` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE = InnoDB;

DROP TABLE IF EXISTS `weather`;
CREATE TABLE `weather` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `weather_title` VARCHAR(45) NOT NULL,
  `weather_icon_url` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_weather_title` (`weather_title` ASC) VISIBLE,
  INDEX `idx_weather_icon_url` (`weather_icon_url` ASC) VISIBLE
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `AccuWeather`.`weather_forecast`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `weather_forecast`;
CREATE TABLE `weather_forecast` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `city_id` INT NOT NULL,
  `weather_id` INT NOT NULL,
  `temperature` DECIMAL(2,0) NOT NULL,
  `wind_speed` DECIMAL(2,0) NOT NULL,
  `humidity` DECIMAL(3,0) NOT NULL,
  `precipitation_probability` DECIMAL(3,0) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `city_id_idx` (`city_id` ASC) VISIBLE,
  INDEX `weather_id_idx` (`weather_id` ASC) VISIBLE,
  INDEX `idx_temperature` (`temperature` ASC) VISIBLE,
  INDEX `idx_wind_speed` (`wind_speed` ASC) VISIBLE,
  INDEX `idx_humidity` (`humidity` ASC) VISIBLE,
  INDEX `idx_precipitation_probability` (`precipitation_probability` ASC) VISIBLE,
  CONSTRAINT `city_id`
    FOREIGN KEY (`city_id`)
    REFERENCES `city` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `weather_id`
    FOREIGN KEY (`weather_id`)
    REFERENCES `weather` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `AccuWeather`.`weather_forecast_daily`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `weather_forecast_daily`;
CREATE TABLE `weather_forecast_daily` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `forecast_id` INT NOT NULL UNIQUE,
  `date` DATE NOT NULL,
  `day_period` TINYINT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `forecast_id_idx` (`forecast_id` ASC) VISIBLE,
  INDEX `idx_date` (`date` ASC) VISIBLE,
  INDEX `idx_day_period` (`day_period` ASC) VISIBLE,
  CONSTRAINT `fk_daily_forecast_id`
    FOREIGN KEY (`forecast_id`)
    REFERENCES `weather_forecast` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `AccuWeather`.`weather_forecast_hourly`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `weather_forecast_hourly`;
CREATE TABLE `weather_forecast_hourly` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `forecast_id` INT NOT NULL UNIQUE,
  `date` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_forecast_hourly_forecast_id_idx` (`forecast_id` ASC) VISIBLE,
  INDEX `idx_date` (`date` ASC) VISIBLE,
  CONSTRAINT `fk_forecast_hourly_forecast_id`
    FOREIGN KEY (`forecast_id`)
    REFERENCES `weather_forecast` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `AccuWeather`.`weather_cataclysm_warning`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `weather_cataclysm_warning`;
CREATE TABLE `weather_cataclysm_warning` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `city_id` INT NOT NULL,
  `warning_description` VARCHAR(255) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `city_id_idx` (`city_id` ASC) VISIBLE,
  INDEX `idx_date` (`date` ASC) VISIBLE,
  CONSTRAINT `fk_weather_warning_city_id`
    FOREIGN KEY (`city_id`)
    REFERENCES `city` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `AccuWeather`.`water_temperature`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `water_temperature`;
CREATE TABLE `water_temperature` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `city_id` INT NOT NULL,
  `water_temperature` DECIMAL(2,0) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_water_temperature_city_id_idx` (`city_id` ASC) VISIBLE,
  INDEX `idx_date` (`date` ASC) VISIBLE,
  CONSTRAINT `fk_water_temperature_city_id`
    FOREIGN KEY (`city_id`)
    REFERENCES `city` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE = InnoDB;

DROP TABLE IF EXISTS `weather_forecast_monthly`;

CREATE TABLE weather_forecast_monthly (
    id INT AUTO_INCREMENT PRIMARY KEY,
    forecast_id INT,
    dateStart DATE NOT NULL,
    dateEnd DATE NOT NULL,
    txt VARCHAR(14) NOT NULL,
    FOREIGN KEY (forecast_id) REFERENCES weather_forecast(id)
) ENGINE = InnoDB;	

INSERT INTO weather_forecast_monthly (forecast_id, dateStart, dateEnd, txt) VALUES (1, '2024-01-01', '2024-01-31', 'test');

INSERT INTO weather_forecast_monthly (forecast_id, dateStart, dateEnd, txt)
SELECT NULL, CURRENT_DATE, CURRENT_DATE, CONCAT('Noname', numbers.n) AS txt
FROM (
    SELECT 1 AS n UNION ALL
    SELECT 2 UNION ALL
    SELECT 3 UNION ALL
    SELECT 4 UNION ALL
    SELECT 5 UNION ALL
    SELECT 6 UNION ALL
    SELECT 7 UNION ALL
    SELECT 8 UNION ALL
    SELECT 9 UNION ALL
    SELECT 10
) AS numbers;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


-- Country
INSERT INTO `country` (`country_name`, `longtitude`, `latitude`) VALUES ('Ukraine', 30.5234, 50.4501);
INSERT INTO `country` (`country_name`, `longtitude`, `latitude`) VALUES ('United States', -95.7129, 37.0902);
INSERT INTO `country` (`country_name`, `longtitude`, `latitude`) VALUES ('China', 104.1954, 35.8617);
INSERT INTO `country` (`country_name`, `longtitude`, `latitude`) VALUES ('Brazil', -51.9253, -14.2350);
INSERT INTO `country` (`country_name`, `longtitude`, `latitude`) VALUES ('Finland', 105.3188, 61.5240);
INSERT INTO `country` (`country_name`, `longtitude`, `latitude`) VALUES ('Australia', 133.7751, -25.2744);
INSERT INTO `country` (`country_name`, `longtitude`, `latitude`) VALUES ('Canada', -106.3468, 56.1304);
INSERT INTO `country` (`country_name`, `longtitude`, `latitude`) VALUES ('India', 78.9629, 20.5937);
INSERT INTO `country` (`country_name`, `longtitude`, `latitude`) VALUES ('South Africa', 22.9375, -30.5595);
INSERT INTO `country` (`country_name`, `longtitude`, `latitude`) VALUES ('Japan', 138.2529, 36.2048);

-- Region
INSERT INTO `region` (`country_id`, `region_name`) VALUES (1, 'Kyiv Oblast');
INSERT INTO `region` (`country_id`, `region_name`) VALUES (2, 'California');
INSERT INTO `region` (`country_id`, `region_name`) VALUES (3, 'Beijing');
INSERT INTO `region` (`country_id`, `region_name`) VALUES (4, 'São Paulo');
INSERT INTO `region` (`country_id`, `region_name`) VALUES (5, 'Southern Finland');
INSERT INTO `region` (`country_id`, `region_name`) VALUES (6, 'New South Wales');
INSERT INTO `region` (`country_id`, `region_name`) VALUES (7, 'Alberta');
INSERT INTO `region` (`country_id`, `region_name`) VALUES (8, 'Maharashtra');
INSERT INTO `region` (`country_id`, `region_name`) VALUES (9, 'Gauteng');
INSERT INTO `region` (`country_id`, `region_name`) VALUES (10, 'Kanto');

-- City
INSERT INTO `city` (`region_id`, `city_name`, `latitude`, `longtitude`) VALUES (1, 'Kyiv', 50.4501, 30.5234);
INSERT INTO `city` (`region_id`, `city_name`, `latitude`, `longtitude`) VALUES (2, 'Los Angeles', 34.0522, -118.2437);
INSERT INTO `city` (`region_id`, `city_name`, `latitude`, `longtitude`) VALUES (3, 'Beijing', 39.9042, 116.4074);
INSERT INTO `city` (`region_id`, `city_name`, `latitude`, `longtitude`) VALUES (4, 'São Paulo', -23.5505, -46.6333);
INSERT INTO `city` (`region_id`, `city_name`, `latitude`, `longtitude`) VALUES (5, 'Helsinki', 60.1695, 24.9354);
INSERT INTO `city` (`region_id`, `city_name`, `latitude`, `longtitude`) VALUES (6, 'Sydney', -33.8688, 151.2093);
INSERT INTO `city` (`region_id`, `city_name`, `latitude`, `longtitude`) VALUES (7, 'Calgary', 51.0447, -114.0719);
INSERT INTO `city` (`region_id`, `city_name`, `latitude`, `longtitude`) VALUES (8, 'Mumbai', 19.0760, 72.8777);
INSERT INTO `city` (`region_id`, `city_name`, `latitude`, `longtitude`) VALUES (9, 'Johannesburg', -26.2041, 28.0473);
INSERT INTO `city` (`region_id`, `city_name`, `latitude`, `longtitude`) VALUES (10, 'Tokyo', 35.6895, 139.6917);

-- Air Quality
INSERT INTO `air_quality` (`city_id`, `date`, `air_quality`) VALUES (1, '2023-11-23', 80);
INSERT INTO `air_quality` (`city_id`, `date`, `air_quality`) VALUES (2, '2023-11-23', 65);
INSERT INTO `air_quality` (`city_id`, `date`, `air_quality`) VALUES (3, '2023-11-23', 90);
INSERT INTO `air_quality` (`city_id`, `date`, `air_quality`) VALUES (4, '2023-11-23', 75);
INSERT INTO `air_quality` (`city_id`, `date`, `air_quality`) VALUES (5, '2023-11-23', 60);
INSERT INTO `air_quality` (`city_id`, `date`, `air_quality`) VALUES (6, '2023-11-23', 85);
INSERT INTO `air_quality` (`city_id`, `date`, `air_quality`) VALUES (7, '2023-11-23', 70);
INSERT INTO `air_quality` (`city_id`, `date`, `air_quality`) VALUES (8, '2023-11-23', 95);
INSERT INTO `air_quality` (`city_id`, `date`, `air_quality`) VALUES (9, '2023-11-23', 78);
INSERT INTO `air_quality` (`city_id`, `date`, `air_quality`) VALUES (10, '2023-11-23', 88);

-- Weather
INSERT INTO `weather` (`weather_title`, `weather_icon_url`) VALUES ('Sunny', 'sunny_icon.png');
INSERT INTO `weather` (`weather_title`, `weather_icon_url`) VALUES ('Cloudy', 'cloudy_icon.png');
INSERT INTO `weather` (`weather_title`, `weather_icon_url`) VALUES ('Rainy', 'rainy_icon.png');
INSERT INTO `weather` (`weather_title`, `weather_icon_url`) VALUES ('Snowy', 'snowy_icon.png');
INSERT INTO `weather` (`weather_title`, `weather_icon_url`) VALUES ('Windy', 'windy_icon.png');
INSERT INTO `weather` (`weather_title`, `weather_icon_url`) VALUES ('Foggy', 'foggy_icon.png');
INSERT INTO `weather` (`weather_title`, `weather_icon_url`) VALUES ('Thunderstorm', 'thunderstorm_icon.png');
INSERT INTO `weather` (`weather_title`, `weather_icon_url`) VALUES ('Clear Night', 'clear_night_icon.png');
INSERT INTO `weather` (`weather_title`, `weather_icon_url`) VALUES ('Partly Cloudy', 'partly_cloudy_icon.png');
INSERT INTO `weather` (`weather_title`, `weather_icon_url`) VALUES ('Misty', 'misty_icon.png');

-- Weather forecast
INSERT INTO `weather_forecast` (`city_id`, `weather_id`, `temperature`, `wind_speed`, `humidity`, `precipitation_probability`) VALUES (1, 1, 25, 10, 70, 20);
INSERT INTO `weather_forecast` (`city_id`, `weather_id`, `temperature`, `wind_speed`, `humidity`, `precipitation_probability`) VALUES (2, 2, 18, 15, 80, 30);
INSERT INTO `weather_forecast` (`city_id`, `weather_id`, `temperature`, `wind_speed`, `humidity`, `precipitation_probability`) VALUES (3, 3, 12, 8, 60, 10);
INSERT INTO `weather_forecast` (`city_id`, `weather_id`, `temperature`, `wind_speed`, `humidity`, `precipitation_probability`) VALUES (4, 4, -2, 5, 45, 5);
INSERT INTO `weather_forecast` (`city_id`, `weather_id`, `temperature`, `wind_speed`, `humidity`, `precipitation_probability`) VALUES (5, 5, 28, 20, 75, 25);
INSERT INTO `weather_forecast` (`city_id`, `weather_id`, `temperature`, `wind_speed`, `humidity`, `precipitation_probability`) VALUES (6, 6, 15, 12, 90, 40);
INSERT INTO `weather_forecast` (`city_id`, `weather_id`, `temperature`, `wind_speed`, `humidity`, `precipitation_probability`) VALUES (7, 7, 8, 6, 55, 15);
INSERT INTO `weather_forecast` (`city_id`, `weather_id`, `temperature`, `wind_speed`, `humidity`, `precipitation_probability`) VALUES (8, 8, 22, 18, 65, 30);
INSERT INTO `weather_forecast` (`city_id`, `weather_id`, `temperature`, `wind_speed`, `humidity`, `precipitation_probability`) VALUES (9, 9, 20, 14, 75, 20);
INSERT INTO `weather_forecast` (`city_id`, `weather_id`, `temperature`, `wind_speed`, `humidity`, `precipitation_probability`) VALUES (10, 10, 10, 8, 50, 10);

-- Weather forecast daily
INSERT INTO `weather_forecast_daily` (`forecast_id`, `date`, `day_period`) VALUES (1, '2023-11-23', 1);
INSERT INTO `weather_forecast_daily` (`forecast_id`, `date`, `day_period`) VALUES (2, '2023-11-23', 2);
INSERT INTO `weather_forecast_daily` (`forecast_id`, `date`, `day_period`) VALUES (3, '2023-11-23', 1);
INSERT INTO `weather_forecast_daily` (`forecast_id`, `date`, `day_period`) VALUES (4, '2023-11-23', 2);
INSERT INTO `weather_forecast_daily` (`forecast_id`, `date`, `day_period`) VALUES (5, '2023-11-23', 1);
INSERT INTO `weather_forecast_daily` (`forecast_id`, `date`, `day_period`) VALUES (6, '2023-11-23', 2);
INSERT INTO `weather_forecast_daily` (`forecast_id`, `date`, `day_period`) VALUES (7, '2023-11-23', 1);
INSERT INTO `weather_forecast_daily` (`forecast_id`, `date`, `day_period`) VALUES (8, '2023-11-23', 2);
INSERT INTO `weather_forecast_daily` (`forecast_id`, `date`, `day_period`) VALUES (9, '2023-11-23', 1);
INSERT INTO `weather_forecast_daily` (`forecast_id`, `date`, `day_period`) VALUES (10, '2023-11-23', 2);

-- Weather forecast hourly
INSERT INTO `weather_forecast_hourly` (`forecast_id`, `date`) VALUES (1, '2023-11-23 00:00:00');
INSERT INTO `weather_forecast_hourly` (`forecast_id`, `date`) VALUES (2, '2023-11-23 01:00:00');
INSERT INTO `weather_forecast_hourly` (`forecast_id`, `date`) VALUES (3, '2023-11-23 02:00:00');
INSERT INTO `weather_forecast_hourly` (`forecast_id`, `date`) VALUES (4, '2023-11-23 03:00:00');
INSERT INTO `weather_forecast_hourly` (`forecast_id`, `date`) VALUES (5, '2023-11-23 04:00:00');
INSERT INTO `weather_forecast_hourly` (`forecast_id`, `date`) VALUES (6, '2023-11-23 05:00:00');
INSERT INTO `weather_forecast_hourly` (`forecast_id`, `date`) VALUES (7, '2023-11-23 06:00:00');
INSERT INTO `weather_forecast_hourly` (`forecast_id`, `date`) VALUES (8, '2023-11-23 07:00:00');
INSERT INTO `weather_forecast_hourly` (`forecast_id`, `date`) VALUES (9, '2023-11-23 08:00:00');
INSERT INTO `weather_forecast_hourly` (`forecast_id`, `date`) VALUES (10, '2023-11-23 09:00:00');

-- Weather cataclysm warning
INSERT INTO `weather_cataclysm_warning` (`city_id`, `warning_description`, `date`) VALUES (1, 'Heavy Rainfall Warning', '2023-11-23');
INSERT INTO `weather_cataclysm_warning` (`city_id`, `warning_description`, `date`) VALUES (2, 'High Wind Advisory', '2023-11-23');
INSERT INTO `weather_cataclysm_warning` (`city_id`, `warning_description`, `date`) VALUES (3, 'Severe Thunderstorm Warning', '2023-11-23');
INSERT INTO `weather_cataclysm_warning` (`city_id`, `warning_description`, `date`) VALUES (4, 'Snowstorm Alert', '2023-11-23');
INSERT INTO `weather_cataclysm_warning` (`city_id`, `warning_description`, `date`) VALUES (5, 'Extreme Heat Advisory', '2023-11-23');
INSERT INTO `weather_cataclysm_warning` (`city_id`, `warning_description`, `date`) VALUES (6, 'Fog Alert', '2023-11-23');
INSERT INTO `weather_cataclysm_warning` (`city_id`, `warning_description`, `date`) VALUES (7, 'Wildfire Warning', '2023-11-23');
INSERT INTO `weather_cataclysm_warning` (`city_id`, `warning_description`, `date`) VALUES (8, 'Air Quality Alert', '2023-11-23');
INSERT INTO `weather_cataclysm_warning` (`city_id`, `warning_description`, `date`) VALUES (9, 'Flooding Alert', '2023-11-23');
INSERT INTO `weather_cataclysm_warning` (`city_id`, `warning_description`, `date`) VALUES (10, 'Tornado Watch', '2023-11-23');

-- Water temperature
INSERT INTO `water_temperature` (`city_id`, `water_temperature`, `date`) VALUES (1, 12, '2023-11-23');
INSERT INTO `water_temperature` (`city_id`, `water_temperature`, `date`) VALUES (2, 18, '2023-11-23');
INSERT INTO `water_temperature` (`city_id`, `water_temperature`, `date`) VALUES (3, 10, '2023-11-23');
INSERT INTO `water_temperature` (`city_id`, `water_temperature`, `date`) VALUES (4, 2, '2023-11-23');
INSERT INTO `water_temperature` (`city_id`, `water_temperature`, `date`) VALUES (5, 15, '2023-11-23');
INSERT INTO `water_temperature` (`city_id`, `water_temperature`, `date`) VALUES (6, 8, '2023-11-23');
INSERT INTO `water_temperature` (`city_id`, `water_temperature`, `date`) VALUES (7, 5, '2023-11-23');
INSERT INTO `water_temperature` (`city_id`, `water_temperature`, `date`) VALUES (8, 20, '2023-11-23');
INSERT INTO `water_temperature` (`city_id`, `water_temperature`, `date`) VALUES (9, 14, '2023-11-23');
INSERT INTO `water_temperature` (`city_id`, `water_temperature`, `date`) VALUES (10, 6, '2023-11-23');


INSERT INTO weather_forecast_monthly (forecast_id, dateStart, dateEnd, txt) VALUES (1, '2024-01-01', '2024-01-31', 'asdasdasd');
INSERT INTO weather_forecast_monthly (forecast_id, dateStart, dateEnd, txt) VALUES (2, '2024-02-01', '2024-02-28', 'asdasdassdas');
INSERT INTO weather_forecast_monthly (forecast_id, dateStart, dateEnd, txt) VALUES (3, '2024-03-01', '2024-03-31', 'asdasdarqw');
INSERT INTO weather_forecast_monthly (forecast_id, dateStart, dateEnd, txt) VALUES (4, '2024-04-01', '2024-04-30', 'kjkdfdvkajk');
INSERT INTO weather_forecast_monthly (forecast_id, dateStart, dateEnd, txt) VALUES (5, '2024-05-01', '2024-05-31', 'kjepgpjrgr');
INSERT INTO weather_forecast_monthly (forecast_id, dateStart, dateEnd, txt) VALUES (6, '2024-06-01', '2024-06-30', 'lkwwfissfg');
INSERT INTO weather_forecast_monthly (forecast_id, dateStart, dateEnd, txt) VALUES (7, '2024-07-01', '2024-07-31', 'lrigijskd');
INSERT INTO weather_forecast_monthly (forecast_id, dateStart, dateEnd, txt) VALUES (8, '2024-08-01', '2024-08-31', 'kdjgaeorrg');
INSERT INTO weather_forecast_monthly (forecast_id, dateStart, dateEnd, txt) VALUES (9, '2024-09-01', '2024-09-30', 'dlfkgkeorgk');
INSERT INTO weather_forecast_monthly (forecast_id, dateStart, dateEnd, txt) VALUES (10, '2024-10-01', '2024-10-31', 'ekrpogj');



