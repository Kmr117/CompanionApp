-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema gamedatabase
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema gamedatabase
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `gamedatabase` DEFAULT CHARACTER SET utf8 ;
USE `gamedatabase` ;

-- -----------------------------------------------------
-- Table `gamedatabase`.`character`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gamedatabase`.`character` (
  `idCharacter` INT(11) NOT NULL,
  `nameCharacter` VARCHAR(45) NOT NULL,
  `Class` VARCHAR(45) NOT NULL,
  `Attribute` VARCHAR(45) NOT NULL,
  `Alliance` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCharacter`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `gamedatabase`.`event`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gamedatabase`.`event` (
  `idEvent` INT(11) NOT NULL,
  `Desciption` VARCHAR(45) NOT NULL,
  `Type` VARCHAR(45) NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idEvent`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `gamedatabase`.`guild`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gamedatabase`.`guild` (
  `idGuild` INT(11) NOT NULL,
  `GuildName` VARCHAR(45) NOT NULL,
  `Manager` VARCHAR(45) NOT NULL,
  `GuildLevel` INT(11) NOT NULL,
  `Size` INT(11) NOT NULL,
  `Leader` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idGuild`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `gamedatabase`.`npc`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gamedatabase`.`npc` (
  `idNPC` INT(11) NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Position` VARCHAR(45) NOT NULL,
  `Attribute` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idNPC`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `gamedatabase`.`interact`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gamedatabase`.`interact` (
  `NPCid` INT(11) NOT NULL,
  `Characterid` INT(11) NOT NULL,
  PRIMARY KEY (`NPCid`, `Characterid`),
  INDEX `Characterid_idx` (`Characterid` ASC),
  CONSTRAINT `idc`
    FOREIGN KEY (`Characterid`)
    REFERENCES `gamedatabase`.`character` (`idCharacter`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idn`
    FOREIGN KEY (`NPCid`)
    REFERENCES `gamedatabase`.`npc` (`idNPC`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `gamedatabase`.`inventory`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gamedatabase`.`inventory` (
  `idBag` INT(11) NOT NULL,
  `size` INT(11) NOT NULL,
  PRIMARY KEY (`idBag`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `gamedatabase`.`item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gamedatabase`.`item` (
  `idItem` INT(11) NOT NULL,
  `ItemName` VARCHAR(45) NOT NULL,
  `Category` VARCHAR(45) NOT NULL,
  `Descrption` VARCHAR(45) NOT NULL,
  `Quantity` INT(11) NOT NULL,
  `Attribute` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idItem`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `gamedatabase`.`join`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gamedatabase`.`join` (
  `GuildID` INT(11) NOT NULL,
  `CharacterID` INT(11) NOT NULL,
  PRIMARY KEY (`GuildID`, `CharacterID`),
  INDEX `CharacterID_idx` (`CharacterID` ASC),
  CONSTRAINT `idCharacter`
    FOREIGN KEY (`CharacterID`)
    REFERENCES `gamedatabase`.`character` (`idCharacter`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idGuild`
    FOREIGN KEY (`GuildID`)
    REFERENCES `gamedatabase`.`guild` (`idGuild`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `gamedatabase`.`skill`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gamedatabase`.`skill` (
  `idSkill` INT(11) NOT NULL,
  `DamageType` VARCHAR(45) NOT NULL,
  `Value` INT(11) NOT NULL,
  `Class` VARCHAR(45) NOT NULL,
  `LevelRequirement` INT(11) NOT NULL,
  `status` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idSkill`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `gamedatabase`.`learned`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gamedatabase`.`learned` (
  `SkillID` INT(11) NOT NULL,
  `CharacterID` INT(11) NOT NULL,
  PRIMARY KEY (`SkillID`, `CharacterID`),
  INDEX `CharacterID_idx` (`CharacterID` ASC),
  CONSTRAINT `cid`
    FOREIGN KEY (`CharacterID`)
    REFERENCES `gamedatabase`.`character` (`idCharacter`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `sid`
    FOREIGN KEY (`SkillID`)
    REFERENCES `gamedatabase`.`skill` (`idSkill`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `gamedatabase`.`player`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gamedatabase`.`player` (
  `Player_ID` INT(11) NOT NULL,
  `PlayerFirstName` VARCHAR(45) NOT NULL,
  `PlayerLastName` VARCHAR(45) NOT NULL,
  `Player_Email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Player_ID`, `Player_Email`, `password`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `gamedatabase`.`make_friend`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gamedatabase`.`make_friend` (
  `Username1` INT(11) NOT NULL,
  `Username2` INT(11) NOT NULL,
  PRIMARY KEY (`Username1`, `Username2`),
  INDEX `Username2_idx` (`Username2` ASC),
  CONSTRAINT `Username1`
    FOREIGN KEY (`Username1`)
    REFERENCES `gamedatabase`.`player` (`Player_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Username2`
    FOREIGN KEY (`Username2`)
    REFERENCES `gamedatabase`.`player` (`Player_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `gamedatabase`.`participate`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gamedatabase`.`participate` (
  `CharacterID` INT(11) NOT NULL,
  `EventID` INT(11) NOT NULL,
  PRIMARY KEY (`CharacterID`, `EventID`),
  INDEX `ide_idx` (`EventID` ASC),
  CONSTRAINT `carc`
    FOREIGN KEY (`CharacterID`)
    REFERENCES `gamedatabase`.`character` (`idCharacter`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `ide`
    FOREIGN KEY (`EventID`)
    REFERENCES `gamedatabase`.`event` (`idEvent`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `gamedatabase`.`team`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gamedatabase`.`team` (
  `idTeam` INT(11) NOT NULL,
  `Size` INT(11) NULL DEFAULT NULL,
  `Leader` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idTeam`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
