/* 
https://www.corobori.com/Corobori_Como_encriptar_una_columna_en_una_base_de_datos_SQL_Server-MTI=.aspx 
*/

/*Crear una clave*/  
USE OLDB89694; 
GO 
	CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'w1N'; 
GO 

/*Crear certificado */
USE OLDB89694; 
GO 
	CREATE CERTIFICATE Certificado WITH SUBJECT = 'Proteccion Datos'; 
GO 

/*Y ahora se crea la clave simetrica */
USE OLDB89694; 
GO 
	CREATE SYMMETRIC KEY Clave1 WITH ALGORITHM = AES_128 ENCRYPTION BY CERTIFICATE Certificado; 
GO 

USE OLDB89694; 
GO 
	SELECT * FROM sys.symmetric_keys WHERE name = 'Clave1'; 
GO 