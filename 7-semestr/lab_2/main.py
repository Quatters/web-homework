import os
from sqlite3 import connect
from pandas import read_sql
from pprint import pprint

DB_PATH = f'{os.path.dirname(os.path.abspath(__file__))}/mydb.sqlite3'

if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

connection = connect(DB_PATH)
cursor = connection.cursor()

cursor.executescript("""
-- -----------------------------------------------------
-- Table `city`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `city` (
  `city_id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `city` VARCHAR(100) NOT NULL
);

-- -----------------------------------------------------
-- Table `route`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `route` (
  `route_number` VARCHAR(5) PRIMARY KEY,
  `distance_km` INTEGER NULL,
  `from` INTEGER NULL,
  `to` INTEGER NOT NULL,
  CONSTRAINT city_route_from_fk
    FOREIGN KEY (`from`)
    REFERENCES `city`(`city_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT city_route_to_fk
    FOREIGN KEY (`to`)
    REFERENCES `city`(`city_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table `bus_model`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bus_model` (
  `model_id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `model` VARCHAR(100) NOT NULL,
  `seats_amount` INTEGER NOT NULL
);

-- -----------------------------------------------------
-- Table `bus`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bus` (
  `bus_number` VARCHAR(6) PRIMARY KEY NOT NULL,
  `model_id` INTEGER NOT NULL,
  CONSTRAINT bus_model_fk
    FOREIGN KEY (`model_id`)
    REFERENCES `bus_model`(`model_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table `route_schedule`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `route_schedule` (
  `schedule_id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `route_number` VARCHAR(5) NOT NULL,
  `departure_time` DATETIME NOT NULL,
  `arrival_time` DATETIME NOT NULL,
  CONSTRAINT route_schedule_bus_fk
    FOREIGN KEY (`route_number`)
    REFERENCES `route` (`route_number`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table `flight`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `flight` (
  `flight_id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `bus_number` VARCHAR(6) NOT NULL,
  `departure_date` DATETIME NOT NULL,
  `price` DECIMAL(8,2) NOT NULL,
  `schedule_id` INTEGER NOT NULL,
  CONSTRAINT flight_bus_fk
    FOREIGN KEY (`bus_number`)
    REFERENCES `bus` (`bus_number`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT flight_schedule_fk
    FOREIGN KEY (`schedule_id`)
    REFERENCES `route_schedule` (`schedule_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table `ticket`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ticket` (
  `ticket_id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `seat_number` INTEGER NOT NULL,
  `flight_id` INTEGER NOT NULL,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `patr` VARCHAR(50) NULL,
  CONSTRAINT ticket_flight_fk
    FOREIGN KEY (`flight_id`)
    REFERENCES `flight` (`flight_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
""")
connection.commit()
