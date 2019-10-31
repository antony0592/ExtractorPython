
CREATE TABLE "PROYECT".tblclient(
  tblclientid INT NOT NULL,
  tblclientusername VARCHAR(50) NOT NULL,
  tblclientpassword VARCHAR(50) NOT NULL,
  tblclientcreate TIMESTAMP(3) NOT NULL);
  
CREATE TABLE "PROYECT".tblphone(
  tblphoneid INT NOT NULL,
  tblphoneclientid INT NOT NULL,
  tblphonenumber VARCHAR(50) NOT NULL,
  tblphonecreate TIMESTAMP(3) NOT NULL);

CREATE TABLE "PROYECT".tbladdress(
  tbladdressid INT NOT NULL,
  tbladdressclientid INT NOT NULL,
  tbladdressdetail VARCHAR(100) NOT NULL,
  tbladdresscreate TIMESTAMP(3) NOT NULL);

CREATE TABLE "PROYECT".tblemail(
  tblemailid INT NOT NULL,
  tblemailclientid INT NOT NULL,
  tblemaildetail VARCHAR(45) NOT NULL,
  tblemailcreate TIMESTAMP(3) NOT NULL);
  
CREATE TABLE "PROYECT".tblcreditcard(
  tblcreditcardid INT NOT NULL,
  tblcreditcardclientid INT NOT NULL,
  tblcreditcarddetail VARCHAR(100) NOT NULL,
  tblcreditcardcreate TIMESTAMP(3) NOT NULL);

CREATE TABLE "PROYECT".tblproduct(
  tblproductid INT NOT NULL,
  tblproductname VARCHAR(50) NOT NULL,
  tblproductprice DECIMAL(10,2) NOT NULL,
  tblproductcreate TIMESTAMP(3) NOT NULL);
  
CREATE TABLE "PROYECT".tblorder(
  tblorderid INT NOT NULL,
  tblorderidproduct INT NOT NULL,
  tblorderidclient INT NOT NULL,
  tblordermount DECIMAL(10,2) NOT NULL,
  tblordercreate TIMESTAMP(3) NOT NULL);