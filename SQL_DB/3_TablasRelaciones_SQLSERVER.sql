GO
USE [OLDB89694];
GO
-- -----------------------------------------------------
-- Table tblclient
-- -----------------------------------------------------
CREATE TABLE [PROYECT].[tblclient](
  [tblclientid] INT NOT NULL IDENTITY,
  [tblclientusername] VARBINARY(MAX) NOT NULL,
  [tblclientpassword] VARBINARY(MAX) NOT NULL,
  [tblclientcreate] DATETIME NOT NULL,
  [tblclientmigrate] TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY ([tblclientid]));
  
-- -----------------------------------------------------
-- Table tblphone
-- -----------------------------------------------------  
CREATE TABLE [PROYECT].[tblphone](
  [tblphoneid] INT NOT NULL IDENTITY,
  [tblphoneclientid] INT NOT NULL,
  [tblphonenumber] VARBINARY(MAX) NOT NULL,
  [tblphonecreate] DATETIME NOT NULL,
  [tblphonemigrate] TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY ([tblphoneid]),
  CONSTRAINT [fk_1] 
		FOREIGN KEY ([tblphoneclientid]) 
		REFERENCES [PROYECT].[tblclient] ([tblclientid])
		ON DELETE NO ACTION
		ON UPDATE NO ACTION);

-- -----------------------------------------------------
-- Table tbladdress
-- -----------------------------------------------------  
CREATE TABLE [PROYECT].[tbladdress](
  [tbladdressid] INT NOT NULL IDENTITY,
  [tbladdressclientid] INT NOT NULL,
  [tbladdressdetail] VARBINARY(MAX) NOT NULL,
  [tbladdresscreate] DATETIME NOT NULL,
  [tbladdressmigrate] TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY ([tbladdressid]),
  CONSTRAINT [fk_2] 
		FOREIGN KEY ([tbladdressclientid]) 
		REFERENCES [PROYECT].[tblclient] ([tblclientid])
		ON DELETE NO ACTION
		ON UPDATE NO ACTION);

-- -----------------------------------------------------
-- Table tblemail
-- -----------------------------------------------------  
CREATE TABLE [PROYECT].[tblemail](
  [tblemailid] INT NOT NULL IDENTITY,
  [tblemailclientid] INT NOT NULL,
  [tblemaildetail] VARBINARY(MAX) NOT NULL,
  [tblemailcreate] DATETIME NOT NULL,
  [tblemailmigrate] TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY ([tblemailid]),
  CONSTRAINT [fk_3] 
		FOREIGN KEY ([tblemailclientid]) 
		REFERENCES [PROYECT].[tblclient] ([tblclientid])
		ON DELETE NO ACTION
		ON UPDATE NO ACTION);
 
-- -----------------------------------------------------
-- Table tblcreditcard
-- -----------------------------------------------------   
CREATE TABLE [PROYECT].[tblcreditcard](
  [tblcreditcardid] INT NOT NULL IDENTITY,
  [tblcreditcardclientid] INT NOT NULL,
  [tblcreditcarddetail] VARBINARY(MAX) NOT NULL,
  [tblcreditcardcreate] DATETIME NOT NULL,
  [tblcreditcardmigrate] TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY ([tblcreditcardid]),
  CONSTRAINT [fk_4] 
		FOREIGN KEY ([tblcreditcardclientid]) 
		REFERENCES [PROYECT].[tblclient] ([tblclientid])
		ON DELETE NO ACTION
		ON UPDATE NO ACTION);

-- -----------------------------------------------------
-- Table tblproduct
-- -----------------------------------------------------    
CREATE TABLE [PROYECT].[tblproduct](
  [tblproductid] INT NOT NULL IDENTITY,
  [tblproductname] VARCHAR(50) NOT NULL,
  [tblproductprice] DECIMAL(10,2) NOT NULL,
  [tblproductcreate] DATETIME NOT NULL,
  [tblproductmigrate] TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY ([tblproductid]));
  
-- -----------------------------------------------------
-- Table tblorder
-- -----------------------------------------------------  
CREATE TABLE [PROYECT].[tblorder](
  [tblorderid] INT NOT NULL IDENTITY,
  [tblorderidproduct] INT NOT NULL,
  [tblorderidclient] INT NOT NULL,
  [tblordermount] DECIMAL(10,2) NOT NULL,
  [tblordercreate] DATETIME NOT NULL,
  [tblordermigrate] TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY ([tblorderid]),
  CONSTRAINT [fk_5] 
		FOREIGN KEY ([tblorderidproduct]) 
		REFERENCES [PROYECT].[tblproduct] ([tblproductid])
		ON DELETE NO ACTION
		ON UPDATE NO ACTION,
  CONSTRAINT [fk_6] 
		FOREIGN KEY ([tblorderidclient]) 
		REFERENCES [PROYECT].[tblclient] ([tblclientid])
		ON DELETE NO ACTION
		ON UPDATE NO ACTION);