USE [OLDB89694]
GO
/****** Object:  StoredProcedure [PROYECT].[spDelete]    Script Date: 10/15/2019 22:07:07 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [PROYECT].[spDelete]
	@OUTPUT_IS_SUCCESSFUL INT OUTPUT,
	@OUTPUT_IS_STATUS VARCHAR(25) OUTPUT
	AS
BEGIN 
	TRY
		DELETE FROM [OLDB89694].[PROYECT].[tblclient] WHERE [tblclient].tblclientmigrate = 1
		DELETE FROM [OLDB89694].[PROYECT].[tblorder] WHERE [tblorder].tblordermigrate = 1
		SET @OUTPUT_IS_STATUS ='Successful running'
		SET @OUTPUT_IS_SUCCESSFUL = 1
	END TRY
	BEGIN CATCH
		SET @OUTPUT_IS_STATUS = @OUTPUT_IS_STATUS +' '+ERROR_MESSAGE()
		SET @OUTPUT_IS_SUCCESSFUL=1
		RAISERROR(@OUTPUT_IS_STATUS,16,1)
	END CATCH 
