-- Desencriptar los datos  
USE OLDB89694; 
GO 
OPEN SYMMETRIC KEY Clave1 DECRYPTION BY CERTIFICATE Certificado; 
GO 
-- Leer los datos 
SELECT TOP 1000 [tblclientid]
      ,[tblclientusername]
      ,CONVERT(varchar, DecryptByKey([tblclientpassword]))
      ,[tblclientmigrate]
  FROM [OLDB89694].[PROYECT].[tblclient]
   
-- Close the symmetric key 
CLOSE SYMMETRIC KEY Clave1; 
GO 