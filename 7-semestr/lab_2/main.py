import os
from sqlite3 import connect
from pandas import read_sql

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
  `seat_number` INTEGER,
  `flight_id` INTEGER NOT NULL,
  `name` VARCHAR(128),
  CONSTRAINT ticket_flight_fk
    FOREIGN KEY (`flight_id`)
    REFERENCES `flight` (`flight_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
""")
connection.commit()

cursor.executescript("""
-- ------------------ --
-- Справочник городов --
-- ------------------ --
INSERT INTO city (city)
VALUES
('Владивосток'),
('Арсеньев'),
('Артём'),
('Большой Камень'),
('Вострецово'),
('Врангель'),
('Дальнегорск'),
('Заводской'),
('Зарубино'),
('Камень-Рыболов'),
('Краскино'),
('Лесозаводск'),
('Лучегорск'),
('Михайловка'),
('Находка'),
('Новопокровка'),
('Новошахтинск'),
('Ольга'),
('Партизанск'),
('Пограничный'),
('Сергеевка'),
('Славянка'),
('Спасск'),
('Терней'),
('Уссурийск'),
('Хороль'),
('Черниговка'),
('Чугуевка'),
('Шмаковка'),
('Южно-Морской'),
('Ярославка');

-- -------------------- --
-- Справочник маршрутов --
-- -------------------- --
INSERT INTO route (route_number, `from`, `to`, distance_km)
VALUES
('547', 1, 2, 234),
('520', 1, 2, 249),
('205МП', 1, 3, 29),
('504', 1, 4, 30),
('542', 1, 5, 513),
('536', 1, 6, 93),
('503', 1, 7, 494),
('224', 1, 8, 48),
('521', 1, 9, 212),
('514', 1, 10, 215),
('528', 1, 11, 233),
('511', 1, 12, 367),
('509', 1, 13, 494),
('545', 1, 14, 129),
('506', 1, 15, 189),
('531', 1, 16, 482),
('530', 1, 17, 147),
('532', 1, 18, 449),
('513', 1, 19, 179),
('525', 1, 20, 200),
('519', 1, 21, 176),
('526', 1, 22, 183),
('502', 1, 23, 230),
('515', 1, 24, 781),
('537', 1, 25, 102),
('546', 1, 25, 107),
('501', 1, 25, 103),
('512', 1, 26, 188),
('524', 1, 27, 191),
('529', 1, 28, 320),
('516', 1, 29, 321),
('544', 1, 30, 173),
('517', 1, 31, 184);

-- -------------------- --
-- Расписание маршрутов --
-- -------------------- --
INSERT INTO route_schedule (route_number, departure_time, arrival_time)
VALUES
('547', '1000-01-01 10:20:00', '1000-01-01 14:28:00'),
('547', '1000-01-01 15:45:00', '1000-01-01 19:53:00'),
('547', '1000-01-01 17:30:00', '1000-01-01 21:38:00'),
('547', '1000-01-01 19:20:00', '1000-01-01 23:28:00'),
('547', '1000-01-01 21:55:00', '1000-01-01 02:03:00'),
('520', '1000-01-01 09:30:00', '1000-01-01 14:35:00'),
('520', '1000-01-01 13:00:00', '1000-01-01 18:06:00'),
('547', '1000-01-01 14:00:00', '1000-01-01 18:00:00'),
('205МП', '1000-01-01 08:25:00', '1000-01-01 09:14:00'),
('205МП', '1000-01-01 10:55:00', '1000-01-01 11:44:00'),
('205МП', '1000-01-01 12:05:00', '1000-01-01 12:54:00'),
('205МП', '1000-01-01 15:00:00', '1000-01-01 15:49:00'),
('205МП', '1000-01-01 18:00:00', '1000-01-01 18:49:00'),
('205МП', '1000-01-01 09:00:00', '1000-01-01 10:10:00'),
('504', '1000-01-01 07:30:00', '1000-01-01 09:01:00'),
('504', '1000-01-01 14:10:00', '1000-01-01 16:41:00'),
('504', '1000-01-01 09:20:00', '1000-01-01 11:51:00'),
('504', '1000-01-01 17:00:00', '1000-01-01 19:31:00'),
('504', '1000-01-01 17:30:00', '1000-01-01 20:01:00'),
('504', '1000-01-01 10:15:00', '1000-01-01 12:46:00'),
('504', '1000-01-01 11:25:00', '1000-01-01 13:56:00'),
('504', '1000-01-01 13:10:00', '1000-01-01 15:41:00'),
('504', '1000-01-01 15:55:00', '1000-01-01 18:26:00'),
('504', '1000-01-01 18:50:00', '1000-01-01 21:21:00'),
('504', '1000-01-01 19:35:00', '1000-01-01 22:06:00'),
('542', '1000-01-01 09:40:00', '1000-01-01 21:14:00'),
('536', '1000-01-01 15:10:00', '1000-01-01 20:20:00'),
('503', '1000-01-01 19:30:00', '1000-01-01 06:08:00'),
('503', '1000-01-01 21:30:00', '1000-01-01 08:08:00'),
('503', '1000-01-01 14:30:00', '1000-01-01 01:08:00'),
('503', '1000-01-01 08:30:00', '1000-01-01 19:08:00'),
('224', '1000-01-01 07:10:00', '1000-01-01 08:56:00'),
('224', '1000-01-01 12:35:00', '1000-01-01 14:21:00'),
('224', '1000-01-01 17:30:00', '1000-01-01 19:16:00'),
('224', '1000-01-01 18:30:00', '1000-01-01 20:16:00'),
('521', '1000-01-01 07:30:00', '1000-01-01 12:25:00'),
('521', '1000-01-01 14:00:00', '1000-01-01 18:55:00'),
('514', '1000-01-01 14:20:00', '1000-01-01 18:38:00'),
('514', '1000-01-01 07:50:00', '1000-01-01 12:08:00'),
('514', '1000-01-01 16:05:00', '1000-01-01 20:23:00'),
('528', '1000-01-01 12:30:00', '1000-01-01 18:00:00'),
('528', '1000-01-01 17:30:00', '1000-01-01 23:00:00'),
('511', '1000-01-01 13:35:00', '1000-01-01 20:59:00'),
('511', '1000-01-01 11:20:00', '1000-01-01 18:44:00'),
('509', '1000-01-01 12:40:00', '1000-01-01 22:00:00'),
('509', '1000-01-01 19:40:00', '1000-01-01 05:00:00'),
('545', '1000-01-01 15:55:00', '1000-01-01 18:05:00'),
('506', '1000-01-01 07:00:00', '1000-01-01 11:15:00'),
('506', '1000-01-01 07:40:00', '1000-01-01 11:55:00'),
('506', '1000-01-01 08:10:00', '1000-01-01 12:25:00'),
('506', '1000-01-01 08:40:00', '1000-01-01 12:55:00'),
('506', '1000-01-01 09:10:00', '1000-01-01 13:25:00'),
('506', '1000-01-01 09:40:00', '1000-01-01 13:55:00'),
('506', '1000-01-01 10:10:00', '1000-01-01 14:25:00'),
('506', '1000-01-01 10:40:00', '1000-01-01 14:55:00'),
('506', '1000-01-01 11:15:00', '1000-01-01 15:30:00'),
('506', '1000-01-01 11:45:00', '1000-01-01 16:00:00'),
('506', '1000-01-01 12:15:00', '1000-01-01 16:30:00'),
('506', '1000-01-01 12:45:00', '1000-01-01 17:00:00'),
('506', '1000-01-01 14:30:00', '1000-01-01 18:45:00'),
('506', '1000-01-01 15:10:00', '1000-01-01 19:25:00'),
('506', '1000-01-01 15:45:00', '1000-01-01 20:00:00'),
('506', '1000-01-01 16:20:00', '1000-01-01 20:35:00'),
('506', '1000-01-01 16:55:00', '1000-01-01 21:10:00'),
('506', '1000-01-01 13:20:00', '1000-01-01 17:35:00'),
('506', '1000-01-01 13:55:00', '1000-01-01 18:10:00'),
('506', '1000-01-01 18:05:00', '1000-01-01 22:20:00'),
('506', '1000-01-01 18:40:00', '1000-01-01 22:55:00'),
('506', '1000-01-01 19:10:00', '1000-01-01 23:25:00'),
('506', '1000-01-01 19:50:00', '1000-01-01 00:05:00'),
('531', '1000-01-01 11:45:00', '1000-01-01 21:12:00'),
('530', '1000-01-01 10:15:00', '1000-01-01 13:50:00'),
('530', '1000-01-01 18:20:00', '1000-01-01 21:55:00'),
('532', '1000-01-01 11:40:00', '1000-01-01 21:50:00'),
('532', '1000-01-01 18:30:00', '1000-01-01 06:13:00'),
('513', '1000-01-01 09:30:00', '1000-01-01 13:15:00'),
('513', '1000-01-01 15:00:00', '1000-01-01 18:45:00'),
('513', '1000-01-01 17:35:00', '1000-01-01 21:20:00'),
('513', '1000-01-01 18:15:00', '1000-01-01 22:00:00'),
('525', '1000-01-01 08:50:00', '1000-01-01 13:40:00'),
('525', '1000-01-01 17:10:00', '1000-01-01 22:00:00'),
('519', '1000-01-01 06:30:00', '1000-01-01 13:10:00'),
('526', '1000-01-01 09:15:00', '1000-01-01 13:05:00'),
('502', '1000-01-01 10:30:00', '1000-01-01 15:40:00'),
('502', '1000-01-01 14:30:00', '1000-01-01 19:40:00'),
('502', '1000-01-01 15:45:00', '1000-01-01 20:55:00'),
('502', '1000-01-01 17:00:00', '1000-01-01 22:10:00'),
('502', '1000-01-01 19:00:00', '1000-01-01 00:10:00'),
('502', '1000-01-01 21:30:00', '1000-01-01 02:40:00'),
('502', '1000-01-01 15:10:00', '1000-01-01 20:20:00'),
('502', '1000-01-01 17:30:00', '1000-01-01 22:40:00'),
('515', '1000-01-01 07:00:00', '1000-01-01 21:43:00'),
('515', '1000-01-01 15:30:00', '1000-01-01 06:13:00'),
('537', '1000-01-01 13:45:00', '1000-01-01 15:35:00'),
('501', '1000-01-01 09:50:00', '1000-01-01 11:40:00'),
('501', '1000-01-01 10:50:00', '1000-01-01 12:40:00'),
('501', '1000-01-01 11:30:00', '1000-01-01 13:20:00'),
('501', '1000-01-01 12:05:00', '1000-01-01 13:55:00'),
('501', '1000-01-01 16:45:00', '1000-01-01 18:35:00'),
('501', '1000-01-01 17:55:00', '1000-01-01 19:45:00'),
('501', '1000-01-01 18:35:00', '1000-01-01 20:25:00'),
('501', '1000-01-01 19:10:00', '1000-01-01 21:00:00'),
('501', '1000-01-01 06:50:00', '1000-01-01 08:40:00'),
('501', '1000-01-01 14:10:00', '1000-01-01 16:00:00'),
('512', '1000-01-01 09:30:00', '1000-01-01 13:10:00'),
('524', '1000-01-01 13:10:00', '1000-01-01 17:19:00'),
('529', '1000-01-01 16:30:00', '1000-01-01 23:07:00'),
('516', '1000-01-01 08:20:00', '1000-01-01 14:53:00'),
('544', '1000-01-01 18:10:00', '1000-01-01 22:04:00'),
('517', '1000-01-01 10:25:00', '1000-01-01 14:04:00'),
('517', '1000-01-01 16:20:00', '1000-01-01 19:59:00'),
('517', '1000-01-01 17:45:00', '1000-01-01 21:24:00');

-- ---------------------------- --
-- Справочник моделей автобусов --
-- ---------------------------- --
INSERT INTO bus_model (model, seats_amount)
VALUES
('МАЗ-232', 35),
('НефАЗ-5299', 46),
('МАЗ-241', 22),
('Volvo 9500', 53),
('МАЗ-251', 49),
("MAN Lion\'s Intercity", 61),
('VolgaBus Дельта', 46),
('Daewoo BH117 Royal Cruistar II', 49),
('МАЗ-231', 51);

-- -------- --
-- Автобусы --
-- -------- --
INSERT INTO bus (model_id, bus_number)
VALUES
(1, 'A001BC'),
(1, 'A002BC'),
(1, 'A003BC'),
(2, 'A004BC'),
(2, 'A005BC'),
(2, 'A006BC'),
(3, 'A007BC'),
(3, 'A008BC'),
(3, 'A009BC'),
(4, 'A010BC'),
(4, 'A011BC'),
(4, 'A012BC'),
(5, 'A013BC'),
(5, 'A014BC'),
(5, 'A015BC'),
(6, 'A016BC'),
(6, 'A017BC'),
(6, 'A018BC'),
(7, 'A019BC'),
(7, 'A020BC'),
(7, 'A021BC'),
(8, 'A022BC'),
(8, 'A023BC'),
(8, 'A024BC'),
(9, 'A025BC'),
(9, 'A026BC'),
(9, 'A027BC');

-- ----- --
-- Рейсы --
-- ----- --
INSERT INTO flight (schedule_id, price, departure_date, bus_number)
VALUES
(1, 840, '2022-04-12 00:00:00', 'A001BC'),
(2, 840, '2022-04-12 00:00:00', 'A002BC'),
(3, 840, '2022-04-12 00:00:00', 'A001BC'),
(4, 840, '2022-04-12 00:00:00', 'A002BC'),
(5, 840, '2022-04-12 00:00:00', 'A001BC'),
(6, 1034, '2022-04-12 00:00:00', 'A003BC'),
(7, 1034, '2022-04-12 00:00:00', 'A004BC'),
(9, 137, '2022-04-12 00:00:00', 'A005BC'),
(10, 137, '2022-04-12 00:00:00', 'A006BC'),
(11, 137, '2022-04-12 00:00:00', 'A005BC'),
(12, 137, '2022-04-12 00:00:00', 'A006BC'),
(13, 137, '2022-04-12 00:00:00', 'A005BC'),
(35, 987, '2022-04-12 00:00:00', 'A007BC'),
(36, 987, '2022-04-12 00:00:00', 'A008BC'),
(37, 987, '2022-04-12 00:00:00', 'A009BC'),
(110, 772, '2022-04-12 00:00:00', 'A010BC'),
(111, 772, '2022-04-12 00:00:00', 'A011BC'),
(112, 772, '2022-04-12 00:00:00', 'A012BC'),
(76, 735, '2022-04-12 00:00:00', 'A013BC'),
(77, 735, '2022-04-12 00:00:00', 'A014BC'),
(78, 735, '2022-04-12 00:00:00', 'A015BC'),
(79, 735, '2022-04-12 00:00:00', 'A016BC'),

(1, 840, '2021-04-12 00:00:00', 'A001BC'),
(2, 840, '2021-04-12 00:00:00', 'A002BC'),
(3, 840, '2021-04-12 00:00:00', 'A001BC'),
(4, 840, '2021-04-12 00:00:00', 'A002BC'),
(5, 840, '2021-04-12 00:00:00', 'A001BC'),
(6, 1034, '2021-04-12 00:00:00', 'A003BC'),
(7, 1034, '2021-04-12 00:00:00', 'A004BC'),
(9, 137, '2021-04-12 00:00:00', 'A005BC'),
(10, 137, '2021-04-12 00:00:00', 'A006BC'),
(11, 137, '2021-04-12 00:00:00', 'A005BC'),
(12, 137, '2021-04-12 00:00:00', 'A006BC'),
(13, 137, '2021-04-12 00:00:00', 'A005BC'),
(35, 987, '2021-04-12 00:00:00', 'A007BC'),
(36, 987, '2021-04-12 00:00:00', 'A008BC'),
(37, 987, '2021-04-12 00:00:00', 'A009BC'),
(110, 772, '2021-04-12 00:00:00', 'A010BC'),
(111, 772, '2021-04-12 00:00:00', 'A011BC'),
(112, 772, '2021-04-12 00:00:00', 'A012BC'),
(76, 735, '2021-04-12 00:00:00', 'A013BC'),
(77, 735, '2021-04-12 00:00:00', 'A014BC'),
(78, 735, '2021-04-12 00:00:00', 'A015BC'),
(79, 735, '2021-04-12 00:00:00', 'A016BC'),

(1, 840, '2022-04-13 00:00:00', 'A001BC'),
(2, 840, '2022-04-13 00:00:00', 'A002BC'),
(3, 840, '2022-04-13 00:00:00', 'A001BC'),
(4, 840, '2022-04-13 00:00:00', 'A002BC'),
(5, 840, '2022-04-13 00:00:00', 'A001BC'),
(6, 1034, '2022-04-13 00:00:00', 'A003BC'),
(7, 1034, '2022-04-13 00:00:00', 'A004BC'),
(9, 137, '2022-04-13 00:00:00', 'A005BC'),
(10, 137, '2022-04-13 00:00:00', 'A006BC'),
(11, 137, '2022-04-13 00:00:00', 'A005BC'),
(12, 137, '2022-04-13 00:00:00', 'A006BC'),
(13, 137, '2022-04-13 00:00:00', 'A005BC'),
(35, 987, '2022-04-13 00:00:00', 'A007BC'),
(36, 987, '2022-04-13 00:00:00', 'A008BC'),
(37, 987, '2022-04-13 00:00:00', 'A009BC'),
(110, 772, '2022-04-13 00:00:00', 'A010BC'),
(111, 772, '2022-04-13 00:00:00', 'A011BC'),
(112, 772, '2022-04-13 00:00:00', 'A012BC'),
(76, 735, '2022-04-13 00:00:00', 'A013BC'),
(77, 735, '2022-04-13 00:00:00', 'A014BC'),
(78, 735, '2022-04-13 00:00:00', 'A015BC'),
(79, 735, '2022-04-13 00:00:00', 'A016BC'),

(1, 840, '2022-04-14 00:00:00', 'A001BC'),
(2, 840, '2022-04-14 00:00:00', 'A002BC'),
(3, 840, '2022-04-14 00:00:00', 'A001BC'),
(4, 840, '2022-04-14 00:00:00', 'A002BC'),
(5, 840, '2022-04-14 00:00:00', 'A001BC'),
(6, 1034, '2022-04-14 00:00:00', 'A003BC'),
(7, 1034, '2022-04-14 00:00:00', 'A004BC'),
(9, 137, '2022-04-14 00:00:00', 'A005BC'),
(10, 137, '2022-04-14 00:00:00', 'A006BC'),
(11, 137, '2022-04-14 00:00:00', 'A005BC'),
(12, 137, '2022-04-14 00:00:00', 'A006BC'),
(13, 137, '2022-04-14 00:00:00', 'A005BC'),
(35, 987, '2022-04-14 00:00:00', 'A007BC'),
(36, 987, '2022-04-14 00:00:00', 'A008BC'),
(37, 987, '2022-04-14 00:00:00', 'A009BC'),
(110, 772, '2022-04-14 00:00:00', 'A010BC'),
(111, 772, '2022-04-14 00:00:00', 'A011BC'),
(112, 772, '2022-04-14 00:00:00', 'A012BC'),
(76, 735, '2022-04-14 00:00:00', 'A013BC'),
(77, 735, '2022-04-14 00:00:00', 'A014BC'),
(78, 735, '2022-04-14 00:00:00', 'A015BC'),
(79, 735, '2022-04-14 00:00:00', 'A016BC');

-- ------ --
-- Билеты --
-- ------ --
INSERT INTO ticket (flight_id, name, seat_number)
VALUES
(1, 'Иванов Иван Иванович', 1),
(1, 'Фадеева Екатерина Павловна', 4),
(1, 'Бачурин Сергей Владимирович', 5),
(1, 'Кагарлицкий Семен Семенович', 6),
(1, 'Гренкин Константин Васильевич', 7),
(1, 'Шевляков Николай Романович', 8),
(1, 'Сидоров Иван Иванович', 3),
(1, 'Барских Светлана Николаевна', 9),
(1, 'Комолов Олег Олегович', 10),
(1, 'Груздь Роман Дмитриевич', 11),
(1, 'Димченко Анатолий Валерьевич', 12),
(1, 'Петров Иван Иванович', 2),
(2, 'Сидоров Петр Иванович', 1),
(2, 'Пушкин Александр Сергеевич', 3),
(2, 'Толстой Лев Николаевич', 8),
(2, 'Шевчук Петр Олегович', 9),
(2, 'Гагарина Анна Дмитриевна', 10),
(2, 'Успенский Дмитрий Анатольевич', 4),
(2, 'Капица София Павловна', 5),
(2, 'Павлова Анастасия Ивановна', 11),
(2, 'Горемыка Василий Георгиевич', 12),
(3, 'Сидоров Петр Петрович', 1),
(3, 'Петров Петр Петрович', 2),
(3, 'Антонова Елизавета Николаевна', 3),
(3, 'Антонова Анастасия Олеговна', 5),
(3, 'Коробчук Семен Романович', 6),
(3, 'Борзых Мария Георгиевна', 4),
(3, 'Коробин Георгий Георгиевич', 10),
(4, 'Иванов Петр Петрович', 1),
(4, 'Колмогоров Роман Васильевич', 2),
(4, 'Хлопков Валерий Федорович', 7),
(4, 'Рзаев Эльмир Вюгар оглы', 5),
(4, 'Федотов Федор Константинович', 6),
(4, 'Середа Алина Олеговна', 9),
(4, 'Щеглова Анна Николаевна', 10),
(4, 'Терентьева Мария Семеновна', 11),
(4, 'Доронина Ульяна Леонидовна', 12),
(4, 'Иванов Петр Иванович', 3),
(4, 'Николаева Наталья Олеговна', 13),
(4, 'Парфенов Николай Георгиевич', 15),
(4, 'Ситцев Леонид Федорович', 16),
(5, 'Сидоров Иван Петрович', 1),
(5, 'Газманов Виталий Сергеевич', 4),
(5, 'Нифедов Олег Олегович', 5),
(5, 'Батурина Лидия Ивановна', 7),
(5, 'Мирских Виоллета Дмитриевна', 2),
(5, 'Шолохова Татьяна Константиновна', 3),
(5, 'Романова Варвара Леонидовна', 8),
(5, 'Чехова Анна Сергеевна', 6),
(5, 'Еремеева Галина Павловна', 9),
(5, 'Конарев Геннадий Николаевич', 10),
(5, 'Дмитриев Игорь Витальевич', 12),
(5, 'Махно Дмитрий Игоревич', 13),

(6, 'Иванов Иван Иванович', 1),
(6, 'Фадеева Екатерина Павловна', 4),
(6, 'Бачурин Сергей Владимирович', 5),
(6, 'Кагарлицкий Семен Семенович', 6),
(6, 'Гренкин Константин Васильевич', 7),
(6, 'Шевляков Николай Романович', 8),
(6, 'Сидоров Иван Иванович', 3),
(6, 'Барских Светлана Николаевна', 9),
(6, 'Комолов Олег Олегович', 10),
(6, 'Груздь Роман Дмитриевич', 11),
(6, 'Димченко Анатолий Валерьевич', 12),
(6, 'Петров Иван Иванович', 2),
(7, 'Сидоров Петр Иванович', 1),
(7, 'Пушкин Александр Сергеевич', 3),
(7, 'Толстой Лев Николаевич', 8),
(7, 'Шевчук Петр Олегович', 9),
(7, 'Гагарина Анна Дмитриевна', 10),
(7, 'Успенский Дмитрий Анатольевич', 4),
(7, 'Капица София Павловна', 5),
(7, 'Павлова Анастасия Ивановна', 11),
(7, 'Горемыка Василий Георгиевич', 12),
(8, 'Сидоров Петр Петрович', 1),
(8, 'Петров Петр Петрович', 2),
(8, 'Антонова Елизавета Николаевна', 3),
(8, 'Антонова Анастасия Олеговна', 5),
(8, 'Коробчук Семен Романович', 6),
(8, 'Борзых Мария Георгиевна', 4),
(8, 'Коробин Георгий Георгиевич', 10),
(9, 'Иванов Петр Петрович', 1),
(9, 'Колмогоров Роман Васильевич', 2),
(9, 'Хлопков Валерий Федорович', 7),
(9, 'Рзаев Эльмир Вюгар оглы', 5),
(9, 'Федотов Федор Константинович', 6),
(9, 'Середа Алина Олеговна', 9),
(9, 'Щеглова Анна Николаевна', 10),
(9, 'Терентьева Мария Семеновна', 11),
(9, 'Доронина Ульяна Леонидовна', 12),
(9, 'Иванов Петр Иванович',3),
(9, 'Николаева Наталья Олеговна', 13),
(9, 'Парфенов Николай Георгиевич', 15),
(9, 'Ситцев Леонид Федорович', 16),
(10, 'Сидоров Иван Петрович', 1),
(10, 'Газманов Виталий Сергеевич', 4),
(10, 'Нифедов Олег Олегович', 5),
(10, 'Батурина Лидия Ивановна', 7),
(10, 'Мирских Виоллета Дмитриевна', 2),
(10, 'Шолохова Татьяна Константиновна', 3),
(10, 'Романова Варвара Леонидовна', 8),
(10, 'Чехова Анна Сергеевна', 6),
(10, 'Еремеева Галина Павловна', 9),
(10, 'Конарев Геннадий Николаевич', 10),
(10, 'Дмитриев Игорь Витальевич', 12),
(10, 'Махно Дмитрий Игоревич', 13),

(11, 'Иванов Иван Иванович', 1),
(11, 'Фадеева Екатерина Павловна', 4),
(11, 'Бачурин Сергей Владимирович', 5),
(11, 'Кагарлицкий Семен Семенович', 6),
(11, 'Гренкин Константин Васильевич', 7),
(11, 'Шевляков Николай Романович', 8),
(11, 'Сидоров Иван Иванович', 3),
(11, 'Барских Светлана Николаевна', 9),
(11, 'Комолов Олег Олегович', 10),
(11, 'Груздь Роман Дмитриевич', 11),
(11, 'Димченко Анатолий Валерьевич', 12),
(11, 'Петров Иван Иванович', 2),
(12, 'Сидоров Петр Иванович', 1),
(12, 'Пушкин Александр Сергеевич', 3),
(12, 'Толстой Лев Николаевич', 8),
(12, 'Шевчук Петр Олегович', 9),
(12, 'Гагарина Анна Дмитриевна', 10),
(12, 'Успенский Дмитрий Анатольевич', 4),
(12, 'Капица София Павловна', 5),
(12, 'Павлова Анастасия Ивановна', 11),
(12, 'Горемыка Василий Георгиевич', 12),
(13, 'Сидоров Петр Петрович', 1),
(13, 'Петров Петр Петрович', 2),
(13, 'Антонова Елизавета Николаевна', 3),
(13, 'Антонова Анастасия Олеговна', 5),
(13, 'Коробчук Семен Романович', 6),
(13, 'Борзых Мария Георгиевна', 4),
(13, 'Коробин Георгий Георгиевич', 10),
(14, 'Иванов Петр Петрович', 1),
(14, 'Колмогоров Роман Васильевич', 2),
(14, 'Хлопков Валерий Федорович', 7),
(14, 'Рзаев Эльмир Вюгар оглы', 5),
(14, 'Федотов Федор Константинович', 6),
(14, 'Середа Алина Олеговна', 9),
(14, 'Щеглова Анна Николаевна', 10),
(14, 'Терентьева Мария Семеновна', 11),
(14, 'Доронина Ульяна Леонидовна', 12),
(14, 'Иванов Петр Иванович',3),
(14, 'Николаева Наталья Олеговна', 13),
(14, 'Парфенов Николай Георгиевич', 15),
(14, 'Ситцев Леонид Федорович', 16),
(15, 'Сидоров Иван Петрович', 1),
(15, 'Газманов Виталий Сергеевич', 4),
(15, 'Нифедов Олег Олегович', 5),
(15, 'Батурина Лидия Ивановна', 7),
(15, 'Мирских Виоллета Дмитриевна', 2),
(15, 'Шолохова Татьяна Константиновна', 3),
(15, 'Романова Варвара Леонидовна', 8),
(15, 'Чехова Анна Сергеевна', 6),
(15, 'Еремеева Галина Павловна', 9),
(15, 'Конарев Геннадий Николаевич', 10),
(15, 'Дмитриев Игорь Витальевич', 12),
(15, 'Махно Дмитрий Игоревич', 13),

(16, 'Иванов Иван Иванович', 1),
(16, 'Фадеева Екатерина Павловна', 4),
(16, 'Бачурин Сергей Владимирович', 5),
(16, 'Кагарлицкий Семен Семенович', 6),
(16, 'Гренкин Константин Васильевич', 7),
(16, 'Шевляков Николай Романович', 8),
(16, 'Сидоров Иван Иванович', 3),
(16, 'Барских Светлана Николаевна', 9),
(16, 'Комолов Олег Олегович', 10),
(16, 'Груздь Роман Дмитриевич', 11),
(16, 'Димченко Анатолий Валерьевич', 12),
(16, 'Петров Иван Иванович', 2),
(17, 'Сидоров Петр Иванович', 1),
(17, 'Пушкин Александр Сергеевич', 3),
(17, 'Толстой Лев Николаевич', 8),
(17, 'Шевчук Петр Олегович', 9),
(17, 'Гагарина Анна Дмитриевна', 10),
(17, 'Успенский Дмитрий Анатольевич', 4),
(17, 'Капица София Павловна', 5),
(17, 'Павлова Анастасия Ивановна', 11),
(17, 'Горемыка Василий Георгиевич', 12),
(18, 'Сидоров Петр Петрович', 1),
(18, 'Петров Петр Петрович', 2),
(18, 'Антонова Елизавета Николаевна', 3),
(18, 'Антонова Анастасия Олеговна', 5),
(18, 'Коробчук Семен Романович', 6),
(18, 'Борзых Мария Георгиевна', 4),
(18, 'Коробин Георгий Георгиевич', 10),
(19, 'Иванов Петр Петрович', 1),
(19, 'Колмогоров Роман Васильевич', 2),
(19, 'Хлопков Валерий Федорович', 7),
(19, 'Рзаев Эльмир Вюгар оглы', 5),
(19, 'Федотов Федор Константинович', 6),
(19, 'Середа Алина Олеговна', 9),
(19, 'Щеглова Анна Николаевна', 10),
(19, 'Терентьева Мария Семеновна', 11),
(19, 'Доронина Ульяна Леонидовна', 12),
(19, 'Иванов Петр Иванович',3),
(19, 'Николаева Наталья Олеговна', 13),
(19, 'Парфенов Николай Георгиевич', 15),
(19, 'Ситцев Леонид Федорович', 16),
(20, 'Сидоров Иван Петрович', 1),
(20, 'Газманов Виталий Сергеевич', 4),
(20, 'Нифедов Олег Олегович', 5),
(20, 'Батурина Лидия Ивановна', 7),
(20, 'Мирских Виоллета Дмитриевна', 2),
(20, 'Шолохова Татьяна Константиновна', 3),
(20, 'Романова Варвара Леонидовна', 8),
(20, 'Чехова Анна Сергеевна', 6),
(20, 'Еремеева Галина Павловна', 9),
(20, 'Конарев Геннадий Николаевич', 10),
(20, 'Дмитриев Игорь Витальевич', 12),
(20, 'Махно Дмитрий Игоревич', 13),
(21, 'Сидоров Петр Иванович', 1),
(21, 'Пушкин Александр Сергеевич', 3),
(21, 'Толстой Лев Николаевич', 8),
(21, 'Шевчук Петр Олегович', 9),
(21, 'Гагарина Анна Дмитриевна', 10),
(21, 'Успенский Дмитрий Анатольевич', 4),
(21, 'Капица София Павловна', 5),
(21, 'Павлова Анастасия Ивановна', 11),
(21, 'Горемыка Василий Георгиевич', 12),

(22, 'Иванов Иван Иванович', 1),
(22, 'Фадеева Екатерина Павловна', 4),
(22, 'Бачурин Сергей Владимирович', 5),
(22, 'Кагарлицкий Семен Семенович', 6),
(22, 'Гренкин Константин Васильевич', 7),
(22, 'Шевляков Николай Романович', 8),
(22, 'Сидоров Иван Иванович', 3),
(22, 'Барских Светлана Николаевна', 9),
(22, 'Комолов Олег Олегович', 10),
(22, 'Груздь Роман Дмитриевич', 11),
(22, 'Димченко Анатолий Валерьевич', 12),
(22, 'Петров Иван Иванович', 2),
(23, 'Сидоров Петр Иванович', 1),
(23, 'Пушкин Александр Сергеевич', 3),
(23, 'Толстой Лев Николаевич', 8),
(23, 'Шевчук Петр Олегович', 9),
(23, 'Гагарина Анна Дмитриевна', 10),
(23, 'Успенский Дмитрий Анатольевич', 4),
(23, 'Капица София Павловна', 5),
(23, 'Павлова Анастасия Ивановна', 11),
(23, 'Горемыка Василий Георгиевич', 12),
(24, 'Сидоров Петр Петрович', 1),
(24, 'Петров Петр Петрович', 2),
(24, 'Антонова Елизавета Николаевна', 3),
(24, 'Антонова Анастасия Олеговна', 5),
(24, 'Коробчук Семен Романович', 6),
(24, 'Борзых Мария Георгиевна', 4),
(24, 'Коробин Георгий Георгиевич', 10),
(25, 'Иванов Петр Петрович', 1),
(25, 'Колмогоров Роман Васильевич', 2),
(25, 'Хлопков Валерий Федорович', 7),
(25, 'Рзаев Эльмир Вюгар оглы', 5),
(25, 'Федотов Федор Константинович', 6),
(25, 'Середа Алина Олеговна', 9),
(25, 'Щеглова Анна Николаевна', 10),
(25, 'Терентьева Мария Семеновна', 11),
(25, 'Доронина Ульяна Леонидовна', 12),
(25, 'Иванов Петр Иванович',3),
(25, 'Николаева Наталья Олеговна', 13),
(25, 'Парфенов Николай Георгиевич', 15),
(25, 'Ситцев Леонид Федорович', 16),
(26, 'Сидоров Иван Петрович', 1),
(26, 'Газманов Виталий Сергеевич', 4),
(26, 'Нифедов Олег Олегович', 5),
(26, 'Батурина Лидия Ивановна', 7),
(26, 'Мирских Виоллета Дмитриевна', 2),
(26, 'Шолохова Татьяна Константиновна', 3),
(26, 'Романова Варвара Леонидовна', 8),
(26, 'Чехова Анна Сергеевна', 6),
(26, 'Еремеева Галина Павловна', 9),
(26, 'Конарев Геннадий Николаевич', 10),
(26, 'Дмитриев Игорь Витальевич', 12),
(26, 'Махно Дмитрий Игоревич', 13),

(27, 'Иванов Иван Иванович', 1),
(27, 'Фадеева Екатерина Павловна', 4),
(27, 'Бачурин Сергей Владимирович', 5),
(27, 'Кагарлицкий Семен Семенович', 6),
(27, 'Гренкин Константин Васильевич', 7),
(27, 'Шевляков Николай Романович', 8),
(27, 'Сидоров Иван Иванович', 3),
(27, 'Барских Светлана Николаевна', 9),
(27, 'Комолов Олег Олегович', 10),
(27, 'Груздь Роман Дмитриевич', 11),
(27, 'Димченко Анатолий Валерьевич', 12),
(27, 'Петров Иван Иванович', 2),
(28, 'Сидоров Петр Иванович', 1),
(28, 'Пушкин Александр Сергеевич', 3),
(28, 'Толстой Лев Николаевич', 8),
(28, 'Шевчук Петр Олегович', 9),
(28, 'Гагарина Анна Дмитриевна', 10),
(28, 'Успенский Дмитрий Анатольевич', 4),
(28, 'Капица София Павловна', 5),
(28, 'Павлова Анастасия Ивановна', 11),
(28, 'Горемыка Василий Георгиевич', 12),
(29, 'Сидоров Петр Петрович', 1),
(29, 'Петров Петр Петрович', 2),
(29, 'Антонова Елизавета Николаевна', 3),
(29, 'Антонова Анастасия Олеговна', 5),
(29, 'Коробчук Семен Романович', 6),
(29, 'Борзых Мария Георгиевна', 4),
(29, 'Коробин Георгий Георгиевич', 10),
(30, 'Иванов Петр Петрович', 1),
(30, 'Колмогоров Роман Васильевич', 2),
(30, 'Хлопков Валерий Федорович', 7),
(30, 'Рзаев Эльмир Вюгар оглы', 5),
(30, 'Федотов Федор Константинович', 6),
(30, 'Середа Алина Олеговна', 9),
(30, 'Щеглова Анна Николаевна', 10),
(30, 'Терентьева Мария Семеновна', 11),
(30, 'Доронина Ульяна Леонидовна', 12),
(30, 'Иванов Петр Иванович',3),
(30, 'Николаева Наталья Олеговна', 13),
(30, 'Парфенов Николай Георгиевич', 15),
(30, 'Ситцев Леонид Федорович', 16),
(31, 'Сидоров Иван Петрович', 1),
(31, 'Газманов Виталий Сергеевич', 4),
(31, 'Нифедов Олег Олегович', 5),
(31, 'Батурина Лидия Ивановна', 7),
(31, 'Мирских Виоллета Дмитриевна', 2),
(31, 'Шолохова Татьяна Константиновна', 3),
(31, 'Романова Варвара Леонидовна', 8),
(31, 'Чехова Анна Сергеевна', 6),
(31, 'Еремеева Галина Павловна', 9),
(31, 'Конарев Геннадий Николаевич', 10),
(31, 'Дмитриев Игорь Витальевич', 12),
(31, 'Махно Дмитрий Игоревич', 13),

(32, 'Иванов Иван Иванович', 1),
(32, 'Фадеева Екатерина Павловна', 4),
(32, 'Бачурин Сергей Владимирович', 5),
(32, 'Кагарлицкий Семен Семенович', 6),
(32, 'Гренкин Константин Васильевич', 7),
(32, 'Шевляков Николай Романович', 8),
(32, 'Сидоров Иван Иванович', 3),
(32, 'Барских Светлана Николаевна', 9),
(32, 'Комолов Олег Олегович', 10),
(32, 'Груздь Роман Дмитриевич', 11),
(32, 'Димченко Анатолий Валерьевич', 12),
(32, 'Петров Иван Иванович', 2),
(33, 'Сидоров Петр Иванович', 1),
(33, 'Пушкин Александр Сергеевич', 3),
(33, 'Толстой Лев Николаевич', 8),
(33, 'Шевчук Петр Олегович', 9),
(33, 'Гагарина Анна Дмитриевна', 10),
(33, 'Успенский Дмитрий Анатольевич', 4),
(33, 'Капица София Павловна', 5),
(33, 'Павлова Анастасия Ивановна', 11),
(33, 'Горемыка Василий Георгиевич', 12),
(34, 'Сидоров Петр Петрович', 1),
(34, 'Петров Петр Петрович', 2),
(34, 'Антонова Елизавета Николаевна', 3),
(34, 'Антонова Анастасия Олеговна', 5),
(34, 'Коробчук Семен Романович', 6),
(34, 'Борзых Мария Георгиевна', 4),
(34, 'Коробин Георгий Георгиевич', 10),
(35, 'Иванов Петр Петрович', 1),
(35, 'Колмогоров Роман Васильевич', 2),
(35, 'Хлопков Валерий Федорович', 7),
(35, 'Рзаев Эльмир Вюгар оглы', 5),
(35, 'Федотов Федор Константинович', 6),
(35, 'Середа Алина Олеговна', 9),
(35, 'Щеглова Анна Николаевна', 10),
(35, 'Терентьева Мария Семеновна', 11),
(35, 'Доронина Ульяна Леонидовна', 12),
(35, 'Иванов Петр Иванович',3),
(35, 'Николаева Наталья Олеговна', 13),
(35, 'Парфенов Николай Георгиевич', 15),
(35, 'Ситцев Леонид Федорович', 16),
(36, 'Сидоров Иван Петрович', 1),
(36, 'Газманов Виталий Сергеевич', 4),
(36, 'Нифедов Олег Олегович', 5),
(36, 'Батурина Лидия Ивановна', 7),
(36, 'Мирских Виоллета Дмитриевна', 2),
(36, 'Шолохова Татьяна Константиновна', 3),
(36, 'Романова Варвара Леонидовна', 8),
(36, 'Чехова Анна Сергеевна', 6),
(36, 'Еремеева Галина Павловна', 9),
(36, 'Конарев Геннадий Николаевич', 10),
(36, 'Дмитриев Игорь Витальевич', 12),
(36, 'Махно Дмитрий Игоревич', 13),

(37, 'Иванов Иван Иванович', 1),
(37, 'Фадеева Екатерина Павловна', 4),
(37, 'Бачурин Сергей Владимирович', 5),
(37, 'Кагарлицкий Семен Семенович', 6),
(37, 'Гренкин Константин Васильевич', 7),
(37, 'Шевляков Николай Романович', 8),
(37, 'Сидоров Иван Иванович', 3),
(37, 'Барских Светлана Николаевна', 9),
(37, 'Комолов Олег Олегович', 10),
(37, 'Груздь Роман Дмитриевич', 11),
(37, 'Димченко Анатолий Валерьевич', 12),
(37, 'Петров Иван Иванович', 2),
(38, 'Сидоров Петр Иванович', 1),
(38, 'Пушкин Александр Сергеевич', 3),
(38, 'Толстой Лев Николаевич', 8),
(38, 'Шевчук Петр Олегович', 9),
(38, 'Гагарина Анна Дмитриевна', 10),
(38, 'Успенский Дмитрий Анатольевич', 4),
(38, 'Капица София Павловна', 5),
(38, 'Павлова Анастасия Ивановна', 11),
(38, 'Горемыка Василий Георгиевич', 12),
(39, 'Сидоров Петр Петрович', 1),
(39, 'Петров Петр Петрович', 2),
(39, 'Антонова Елизавета Николаевна', 3),
(39, 'Антонова Анастасия Олеговна', 5),
(39, 'Коробчук Семен Романович', 6),
(39, 'Борзых Мария Георгиевна', 4),
(39, 'Коробин Георгий Георгиевич', 10),
(40, 'Иванов Петр Петрович', 1),
(40, 'Колмогоров Роман Васильевич', 2),
(40, 'Хлопков Валерий Федорович', 7),
(40, 'Рзаев Эльмир Вюгар оглы', 5),
(40, 'Федотов Федор Константинович', 6),
(40, 'Середа Алина Олеговна', 9),
(40, 'Щеглова Анна Николаевна', 10),
(40, 'Терентьева Мария Семеновна', 11),
(40, 'Доронина Ульяна Леонидовна', 12),
(40, 'Иванов Петр Иванович',3),
(40, 'Николаева Наталья Олеговна', 13),
(40, 'Парфенов Николай Георгиевич', 15),
(40, 'Ситцев Леонид Федорович', 16),
(41, 'Сидоров Иван Петрович', 1),
(41, 'Газманов Виталий Сергеевич', 4),
(41, 'Нифедов Олег Олегович', 5),
(41, 'Батурина Лидия Ивановна', 7),
(41, 'Мирских Виоллета Дмитриевна', 2),
(41, 'Шолохова Татьяна Константиновна', 3),
(41, 'Романова Варвара Леонидовна', 8),
(41, 'Чехова Анна Сергеевна', 6),
(41, 'Еремеева Галина Павловна', 9),
(41, 'Конарев Геннадий Николаевич', 10),
(41, 'Дмитриев Игорь Витальевич', 12),
(41, 'Махно Дмитрий Игоревич', 13),
(42, 'Сидоров Петр Иванович', 1),
(42, 'Пушкин Александр Сергеевич', 3),
(42, 'Толстой Лев Николаевич', 8),
(42, 'Шевчук Петр Олегович', 9),
(42, 'Гагарина Анна Дмитриевна', 10),
(42, 'Успенский Дмитрий Анатольевич', 4),
(42, 'Капица София Павловна', 5),
(42, 'Павлова Анастасия Ивановна', 11),
(42, 'Горемыка Василий Георгиевич', 12);
""")


# запросы со вложенными запросами или табличными выражениями
# триггер: создание flight влечет создание bus_model.seats_amount записей
# в ticket с пустым name (не купленные)
cursor.executescript("""
CREATE TRIGGER create_tickets
AFTER INSERT ON flight
BEGIN
    INSERT INTO ticket (seat_number, flight_id)
    SELECT * FROM (SELECT * FROM (
        WITH RECURSIVE numbers AS (
    		SELECT 1 AS seat_number
    		UNION ALL
    		SELECT seat_number + 1
    		FROM numbers
    		WHERE seat_number < (
                SELECT bus_model.seats_amount
                FROM flight
                LEFT JOIN bus ON bus.bus_number = flight.bus_number
                LEFT JOIN bus_model ON bus_model.model_id = bus.model_id
                WHERE flight_id = new.flight_id
            )
    	)
    	SELECT * FROM numbers
    )
    CROSS JOIN (SELECT new.flight_id));
END;
""")

# запросы на выборку для связанных таблиц с условиями и сортировкой
# таблица маршрутов с наименованиями городов откуда-куда
result = read_sql("""
SELECT
    route_number,
    distance_km,
    r.`from`,
    r.`to`,
    c1.city AS from_city,
    c2.city AS to_city
FROM route r
LEFT JOIN city c1 ON r.`from` = c1.city_id
LEFT JOIN city c2 ON r.`to` = c2.city_id
ORDER BY route_number ASC;
""", connection)
# с временем отправления, прибытия, маршрутом и городами
result = read_sql("""
SELECT
	r.route_number AS route_number,
	departure_time,
	arrival_time,
	r.`from` AS `from`,
	r.`to` AS `to`,
	c1.city AS from_city,
	c2.city AS to_city
FROM route_schedule rs
LEFT JOIN route r ON r.route_number = rs.route_number
LEFT JOIN city c1 ON r.`from` = c1.city_id
LEFT JOIN city c2 ON r.`to` = c2.city_id
ORDER BY from_city, to_city, departure_time
""", connection)

# запросы с группировкой и групповыми функциями
# доход за все время по всем маршрутам
result = read_sql("""
SELECT
  	SUM(price) AS income,
  	COUNT(ticket_id) AS ticket_count,
    city
FROM flight
JOIN ticket ON flight.flight_id = ticket.flight_id
JOIN route_schedule ON route_schedule.schedule_id = flight.schedule_id
JOIN route ON route.route_number = route_schedule.route_number
JOIN city ON city.city_id = route.`to`
GROUP BY city.city_id
ORDER BY income DESC
""", connection)
print('Доход по городам')
print(result)

# самый популярный маршрут (с наибольшим количеством купленных билетов)
result = read_sql("""
SELECT
	r.route_number AS 'route_number',
	COUNT(t.ticket_id) AS 'ticket_count'
FROM route r
JOIN route_schedule rs ON r.route_number = rs.route_number
JOIN flight f ON rs.schedule_id = f.schedule_id
JOIN ticket t ON f.flight_id = t.flight_id
WHERE t.name IS NOT NULL
""", connection)

# запросы корректировки данных (обновление, добавление, удаление и пр)
cursor.executescript("""
INSERT INTO route_schedule (route_number, departure_time, arrival_time)
VALUES ('547', '1000-01-01 11:45:00', '1000-01-01 16:30:00');
""")
cursor.executescript("""
INSERT INTO flight (schedule_id, price, departure_date, bus_number)
VALUES (1, 846, '2022-10-11 00:00:00', 'A001BC');
""")

result = read_sql("""
SELECT * FROM ticket WHERE flight_id = last_insert_rowid();
""", connection)

print(
    'Выборка из ticket по последнему добавленному flight_id (проверка триггера)'
)
print(result)
