USE [OLDB89694]
GO
/****** Object:  StoredProcedure [PROYECT].[spProyect]    Script Date: 10/15/2019 22:07:07 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER PROCEDURE [PROYECT].[spProyect]
	@OPTION_MENU INTEGER,
	@FROMDATE DATETIME,
	@TODATE DATETIME,
	@OUTPUT_IS_SUCCESSFUL INT OUTPUT,
	@OUTPUT_IS_STATUS VARCHAR(25) OUTPUT
	AS
BEGIN 
	OPEN SYMMETRIC KEY Clave1 DECRYPTION BY CERTIFICATE Certificado;
	SET NOCOUNT ON;
	SET @OUTPUT_IS_SUCCESSFUL = 0;
	SET @OUTPUT_IS_STATUS ='Error returning data';
	BEGIN TRY
		IF (@OPTION_MENU=1)
		BEGIN
			SELECT [tblclientid],[tblclientusername] ,[tblclientpassword],[tblclientcreate]
			INTO TEMP1
			FROM [OLDB89694].[PROYECT].[tblclient] 
			WHERE [tblclientmigrate]=0 and ([tblclientcreate] between (@FROMDATE) and (@TODATE));
				
			UPDATE [PROYECT].[tblclient] SET [tblclientmigrate]=1
			FROM [OLDB89694].[PROYECT].[tblclient]
			JOIN TEMP1 ON [PROYECT].[tblclient].[tblclientid] = TEMP1.[tblclientid];
				
			SELECT TEMP1.[tblclientid], CONVERT(varchar, DecryptByKey(TEMP1.[tblclientusername])), 
										CONVERT(varchar, DecryptByKey(TEMP1.[tblclientpassword])), TEMP1.[tblclientcreate]
			FROM [OLDB89694].[PROYECT].[tblclient] C JOIN TEMP1 ON C.[tblclientid] = TEMP1.[tblclientid];
			DROP TABLE TEMP1		
		END
		ELSE IF (@OPTION_MENU=2)
		BEGIN
			SELECT [tbladdressid],[tbladdressclientid],[tbladdressdetail],[tbladdresscreate]
			INTO TEMP2
			FROM [OLDB89694].[PROYECT].[tbladdress] 
			WHERE [tbladdressmigrate]=0 and ([tbladdresscreate] between (@FROMDATE) and (@TODATE));
				
			UPDATE [PROYECT].[tbladdress] SET [tbladdressmigrate]=1
			FROM [OLDB89694].[PROYECT].[tbladdress]
			JOIN TEMP2 ON [PROYECT].[tbladdress].[tbladdressid] = TEMP2.[tbladdressid];
				
			SELECT TEMP2.[tbladdressid],
				   TEMP2.[tbladdressclientid],
				   CONVERT(varchar, DecryptByKey(TEMP2.[tbladdressdetail])),
				   TEMP2.[tbladdresscreate]
			FROM [OLDB89694].[PROYECT].[tbladdress] C JOIN TEMP2 ON C.[tbladdressid] = TEMP2.[tbladdressid];
			DROP TABLE TEMP2				
		END
		ELSE IF (@OPTION_MENU=3)
		BEGIN
			SELECT [tblcreditcardid], [tblcreditcardclientid], [tblcreditcarddetail],[tblcreditcardcreate]
			INTO TEMP3
			FROM [OLDB89694].[PROYECT].[tblcreditcard] 
			WHERE [tblcreditcardmigrate] =0 and ([tblcreditcardcreate] between (@FROMDATE) and (@TODATE));
				
			UPDATE [PROYECT].[tblcreditcard] SET [tblcreditcardmigrate]=1
			FROM [OLDB89694].[PROYECT].[tblcreditcard]
			JOIN TEMP3 ON [PROYECT].[tblcreditcard].[tblcreditcardid] = TEMP3.[tblcreditcardid];
				
			SELECT TEMP3.[tblcreditcardid], TEMP3.[tblcreditcardclientid], 
			CONVERT(varchar, DecryptByKey(TEMP3.[tblcreditcarddetail])), TEMP3.[tblcreditcardcreate]
			FROM [OLDB89694].[PROYECT].[tblcreditcard] C JOIN TEMP3 ON C.[tblcreditcardid] = TEMP3.[tblcreditcardid];	
			
			DROP TABLE TEMP3	

		END
		ELSE IF (@OPTION_MENU=4)
		BEGIN
			SELECT [tblemailid], [tblemailclientid], [tblemaildetail],[tblemailcreate]
			INTO TEMP4
			FROM [OLDB89694].[PROYECT].[tblemail]
			WHERE [tblemailmigrate] =0 and ([tblemailcreate] between (@FROMDATE) and (@TODATE));
				
			UPDATE [PROYECT].[tblemail] SET [tblemailmigrate]=1
			FROM [OLDB89694].[PROYECT].[tblemail]
			JOIN TEMP4 ON [PROYECT].[tblemail].[tblemailid] = TEMP4.[tblemailid];
				
			SELECT TEMP4.[tblemailid], TEMP4.[tblemailclientid], 
						CONVERT(varchar, DecryptByKey(TEMP4.[tblemaildetail])), TEMP4.[tblemailcreate]
			FROM [OLDB89694].[PROYECT].[tblemail] E JOIN TEMP4 ON E.[tblemailid] = TEMP4.[tblemailid];	
			
			DROP TABLE TEMP4;
		END
		ELSE IF (@OPTION_MENU=5)
		BEGIN
			SELECT [tblphoneid], [tblphoneclientid], [tblphonenumber],[tblphonecreate]
			INTO TEMP5
			FROM [OLDB89694].[PROYECT].[tblphone]
			WHERE [tblphonemigrate] =0 and ([tblphonecreate] between (@FROMDATE) and (@TODATE));
				
			UPDATE [PROYECT].[tblphone] SET [tblphonemigrate]=1
			FROM [OLDB89694].[PROYECT].[tblphone]
			JOIN TEMP5 ON [PROYECT].[tblphone].[tblphoneid] = TEMP5.[tblphoneid];
				
			SELECT TEMP5.[tblphoneid], TEMP5.[tblphoneclientid], CONVERT(varchar, DecryptByKey(TEMP5.[tblphonenumber])), TEMP5.[tblphonecreate]
			FROM [OLDB89694].[PROYECT].[tblphone] P JOIN TEMP5 ON P.[tblphoneid] = TEMP5.[tblphoneid];
			DROP TABLE TEMP5;
		END
		ELSE IF (@OPTION_MENU=6)
		BEGIN
			SELECT [tblproductid], [tblproductname], [tblproductprice], [tblproductcreate]
			INTO TEMP6 FROM [OLDB89694].[PROYECT].[tblproduct]
			WHERE [tblproductmigrate] =0 and ([tblproductcreate] between (@FROMDATE) and (@TODATE));
				
			UPDATE [PROYECT].[tblproduct] SET [tblproductmigrate]=1
			FROM [OLDB89694].[PROYECT].[tblproduct]
			JOIN TEMP6 ON [PROYECT].[tblproduct].[tblproductid] = TEMP6.[tblproductid];
				
			SELECT TEMP6.[tblproductid], TEMP6.[tblproductname], TEMP6.[tblproductprice], TEMP6.[tblproductcreate]
			FROM [OLDB89694].[PROYECT].[tblproduct] P JOIN TEMP6 ON P.[tblproductid] = TEMP6.[tblproductid];
			DROP TABLE TEMP6;
		END
		ELSE IF (@OPTION_MENU=7)
		BEGIN
			SELECT [tblorderid], [tblorderidproduct], [tblorderidclient], [tblordermount], [tblordercreate]
			INTO TEMP7
			FROM [OLDB89694].[PROYECT].[tblorder]
			WHERE [tblordermigrate] =0 and ([tblordercreate] between (@FROMDATE) and (@TODATE));
				
			UPDATE [PROYECT].[tblorder] SET [tblordermigrate]=1
			FROM [OLDB89694].[PROYECT].[tblorder]
			JOIN TEMP7 ON [PROYECT].[tblorder].[tblorderid] = TEMP7.[tblorderid];
				
			SELECT TEMP7.[tblorderidproduct], TEMP7.[tblorderidclient], TEMP7.[tblordermount], TEMP7.[tblordercreate]
			FROM [OLDB89694].[PROYECT].[tblorder] P JOIN TEMP7 ON P.[tblorderid] = TEMP7.[tblorderid];
			DROP TABLE TEMP7;
		END	
		SET @OUTPUT_IS_STATUS ='Successful running'
		SET @OUTPUT_IS_SUCCESSFUL = 1
			
	END TRY
	BEGIN CATCH
		SET @OUTPUT_IS_STATUS = @OUTPUT_IS_STATUS +' '+ERROR_MESSAGE()
		SET @OUTPUT_IS_SUCCESSFUL=1
		RAISERROR(@OUTPUT_IS_STATUS,16,1)
	END CATCH 
	-- Close the symmetric key 
	CLOSE SYMMETRIC KEY Clave1;	
END