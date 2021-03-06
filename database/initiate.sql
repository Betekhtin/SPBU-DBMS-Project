-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`country`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`country` (
  `country_id` INT NOT NULL AUTO_INCREMENT,
  `country_name` VARCHAR(45) NULL,
  PRIMARY KEY (`country_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`city`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`city` (
  `city_id` INT NOT NULL AUTO_INCREMENT,
  `country_id` INT NOT NULL,
  `city_name` VARCHAR(45) NULL,
  PRIMARY KEY (`city_id`),
  INDEX `fk_city_country1_idx` (`country_id` ASC),
  CONSTRAINT `fk_city_country1`
    FOREIGN KEY (`country_id`)
    REFERENCES `mydb`.`country` (`country_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(25) NOT NULL,
  `password` VARCHAR(64) NOT NULL,
  `salt` VARCHAR(16) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`temperature`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`temperature` (
  `date` DATETIME NOT NULL,
  `city_id` INT NOT NULL,
  `T` DOUBLE NULL,
  `Tn` DOUBLE NULL,
  `Tx` DOUBLE NULL,
  `Td` DOUBLE NULL,
  `Tg` DOUBLE NULL,
  PRIMARY KEY (`city_id`, `date`),
  INDEX `fk_temperature_city1_idx` (`city_id` ASC),
  CONSTRAINT `fk_temperature_city1`
    FOREIGN KEY (`city_id`)
    REFERENCES `mydb`.`city` (`city_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`other_weather_data`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`other_weather_data` (
  `date` DATETIME NOT NULL,
  `city_id` INT NOT NULL,
  `U` INT NULL,
  `VV` DOUBLE NULL,
  `RRR` VARCHAR(45) NULL,
  `tR` INT NULL,
  `E` VARCHAR(45) NULL,
  `E_` VARCHAR(45) NULL,
  `sss` VARCHAR(45) NULL,
  PRIMARY KEY (`city_id`, `date`),
  INDEX `fk_other_weather_data_city2_idx` (`city_id` ASC),
  CONSTRAINT `fk_other_weather_data_city2`
    FOREIGN KEY (`city_id`)
    REFERENCES `mydb`.`city` (`city_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`pressure`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`pressure` (
  `date` DATETIME NOT NULL,
  `city_id` INT NOT NULL,
  `P0` DOUBLE NULL,
  `P` DOUBLE NULL,
  `Pa` DOUBLE NULL,
  PRIMARY KEY (`city_id`, `date`),
  INDEX `fk_pressure_city1_idx` (`city_id` ASC),
  CONSTRAINT `fk_pressure_city1`
    FOREIGN KEY (`city_id`)
    REFERENCES `mydb`.`city` (`city_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`weather`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`weather` (
  `date` DATETIME NOT NULL,
  `city_id` INT NOT NULL,
  `WW` VARCHAR(45) NULL,
  `W1` VARCHAR(45) NULL,
  `W2` VARCHAR(45) NULL,
  PRIMARY KEY (`city_id`, `date`),
  INDEX `fk_weather_city1_idx` (`city_id` ASC),
  CONSTRAINT `fk_weather_city1`
    FOREIGN KEY (`city_id`)
    REFERENCES `mydb`.`city` (`city_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`clouds`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`clouds` (
  `date` DATETIME NOT NULL,
  `city_id` INT NOT NULL,
  `N` INT NULL,
  `Cl` VARCHAR(45) NULL,
  `Nh` INT NULL,
  `H` VARCHAR(45) NULL,
  `Cm` VARCHAR(45) NULL,
  `Ch` VARCHAR(45) NULL,
  PRIMARY KEY (`city_id`, `date`),
  INDEX `fk_clouds_city1_idx` (`city_id` ASC),
  CONSTRAINT `fk_clouds_city1`
    FOREIGN KEY (`city_id`)
    REFERENCES `mydb`.`city` (`city_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`wind`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`wind` (
  `date` DATETIME NOT NULL,
  `city_id` INT NOT NULL,
  `DD` VARCHAR(45) NULL,
  `Ff` VARCHAR(45) NULL,
  `ff10` DOUBLE NULL,
  `ff3` DOUBLE NULL,
  PRIMARY KEY (`city_id`, `date`),
  INDEX `fk_wind_city1_idx` (`city_id` ASC),
  CONSTRAINT `fk_wind_city1`
    FOREIGN KEY (`city_id`)
    REFERENCES `mydb`.`city` (`city_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
