USE OLDB89694;
GO 
-- Abrir la clave Clave1 
OPEN SYMMETRIC KEY Clave1 DECRYPTION BY CERTIFICATE Certificado; 
GO 

	INSERT INTO [OLDB89694].[PROYECT].[tblclient]([tblclientusername],[tblclientpassword],[tblclientmigrate])
	VALUES (EncryptByKey(Key_GUID('Clave1'),'asalazar'), EncryptByKey(Key_GUID('Clave1'),'12345'),0);      
GO
-- Cerrar la clave 
CLOSE SYMMETRIC KEY Clave1; 
GO 

