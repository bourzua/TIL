CREATE TABLE `aloha`.`board_zuaseyo` (
  `board_no` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NOT NULL,
  `content` TEXT NULL,
  `writer` VARCHAR(45) NOT NULL,
  `reg_date` TIMESTAMP NOT NULL DEFAULT now(),
  PRIMARY KEY (`board_no`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;
