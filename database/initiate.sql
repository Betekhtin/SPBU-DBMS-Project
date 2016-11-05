-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema u871174038_data
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema u871174038_data
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `u871174038_data` DEFAULT CHARACTER SET utf8 ;
USE `u871174038_data` ;

-- -----------------------------------------------------
-- Table `u871174038_data`.`country`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u871174038_data`.`country` (
  `country_id` INT NOT NULL,
  `country_name` VARCHAR(45) NULL,
  PRIMARY KEY (`country_id`))
ENGINE = Aria;


-- -----------------------------------------------------
-- Table `u871174038_data`.`city`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u871174038_data`.`city` (
  `city_id` INT NOT NULL,
  `сountry_id` INT NOT NULL,
  `city_name` VARCHAR(45) NULL,
  PRIMARY KEY (`city_id`),
  INDEX `fk_city_country1_idx` (`сountry_id` ASC),
  CONSTRAINT `fk_city_country1`
    FOREIGN KEY (`сountry_id`)
    REFERENCES `u871174038_data`.`country` (`country_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = Aria;


-- -----------------------------------------------------
-- Table `u871174038_data`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u871174038_data`.`user` (
  `user_id` INT NOT NULL,
  `city_id` INT NOT NULL,
  `login` VARCHAR(25) NULL,
  `password` VARCHAR(64) NULL,
  `salt` VARCHAR(16) NULL,
  `mail_reg` VARCHAR(50) NULL,
  `mail` VARCHAR(50) NULL,
  `last_act` TIMESTAMP(14) NULL,
  `reg_date` VARCHAR(14) NULL,
  PRIMARY KEY (`user_id`, `city_id`),
  INDEX `fk_user_city1_idx` (`city_id` ASC),
  CONSTRAINT `fk_user_city1`
    FOREIGN KEY (`city_id`)
    REFERENCES `u871174038_data`.`city` (`city_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = Aria;


-- -----------------------------------------------------
-- Table `u871174038_data`.`temperature`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u871174038_data`.`temperature` (
  `temperature_id` INT NOT NULL,
  `date` TIMESTAMP(10) NULL,
  `city_id` INT NOT NULL,
  `T` DOUBLE NULL,
  `Tn` DOUBLE NULL,
  `Tx` DOUBLE NULL,
  `Td` DOUBLE NULL,
  `Tg` DOUBLE NULL,
  PRIMARY KEY (`temperature_id`, `city_id`),
  INDEX `fk_temperature_city1_idx` (`city_id` ASC),
  CONSTRAINT `fk_temperature_city1`
    FOREIGN KEY (`city_id`)
    REFERENCES `u871174038_data`.`city` (`city_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = Aria;


-- -----------------------------------------------------
-- Table `u871174038_data`.`other_weather_data`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u871174038_data`.`other_weather_data` (
  `idother_weather_data` INT NOT NULL,
  `date` TIMESTAMP(10) NULL,
  `city_id` INT NOT NULL,
  `U` INT NULL,
  `VV` DOUBLE NULL,
  `RRR` DOUBLE NULL,
  `tR` INT NULL,
  `E` VARCHAR(45) NULL,
  `E'` VARCHAR(45) NULL,
  `sss` INT NULL,
  PRIMARY KEY (`idother_weather_data`, `city_id`),
  INDEX `fk_other_weather_data_city2_idx` (`city_id` ASC),
  CONSTRAINT `fk_other_weather_data_city2`
    FOREIGN KEY (`city_id`)
    REFERENCES `u871174038_data`.`city` (`city_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = Aria;


-- -----------------------------------------------------
-- Table `u871174038_data`.`pressure`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u871174038_data`.`pressure` (
  `pressure_id` INT NOT NULL,
  `date` TIMESTAMP(10) NULL,
  `city_id` INT NOT NULL,
  `P0` DOUBLE NULL,
  `P` DOUBLE NULL,
  `Pa` DOUBLE NULL,
  PRIMARY KEY (`pressure_id`, `city_id`),
  INDEX `fk_pressure_city1_idx` (`city_id` ASC),
  CONSTRAINT `fk_pressure_city1`
    FOREIGN KEY (`city_id`)
    REFERENCES `u871174038_data`.`city` (`city_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = Aria;


-- -----------------------------------------------------
-- Table `u871174038_data`.`weather`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u871174038_data`.`weather` (
  `weather_id` INT NOT NULL,
  `date` TIMESTAMP(10) NULL,
  `city_id` INT NOT NULL,
  `WW` VARCHAR(45) NULL,
  `W1` VARCHAR(45) NULL,
  `W2` VARCHAR(45) NULL,
  PRIMARY KEY (`weather_id`, `city_id`),
  INDEX `fk_weather_city1_idx` (`city_id` ASC),
  CONSTRAINT `fk_weather_city1`
    FOREIGN KEY (`city_id`)
    REFERENCES `u871174038_data`.`city` (`city_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = Aria;


-- -----------------------------------------------------
-- Table `u871174038_data`.`clouds`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u871174038_data`.`clouds` (
  `idclouds` INT NOT NULL,
  `date` TIMESTAMP(10) NULL,
  `city_id` INT NOT NULL,
  `N` INT NULL,
  `Cl` VARCHAR(45) NULL,
  `Nh` INT NULL,
  `H` VARCHAR(45) NULL,
  `Cm` VARCHAR(45) NULL,
  `Ch` VARCHAR(45) NULL,
  PRIMARY KEY (`idclouds`, `city_id`),
  INDEX `fk_clouds_city1_idx` (`city_id` ASC),
  CONSTRAINT `fk_clouds_city1`
    FOREIGN KEY (`city_id`)
    REFERENCES `u871174038_data`.`city` (`city_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = Aria;


-- -----------------------------------------------------
-- Table `u871174038_data`.`wind`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u871174038_data`.`wind` (
  `wind_id` INT NOT NULL,
  `date` TIMESTAMP(10) NULL,
  `city_id` INT NOT NULL,
  `DD` VARCHAR(45) NULL,
  `Ff` VARCHAR(45) NULL,
  `ff10` DOUBLE NULL,
  `ff3` DOUBLE NULL,
  PRIMARY KEY (`wind_id`, `city_id`),
  INDEX `fk_wind_city1_idx` (`city_id` ASC),
  CONSTRAINT `fk_wind_city1`
    FOREIGN KEY (`city_id`)
    REFERENCES `u871174038_data`.`city` (`city_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = Aria;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
