import os, sys, csv, datetime
from conf import mssql_connection, get_data_from_sql, sqlite_connection
from datetime import datetime
import constants

sp_name=""
def extractor(sp_name, option_menu, fromdate, todate):
	try:
		#Sandbox Conn SQLite
		con_sbSQLLite = sqlite_connection()
		#Sandbox Conn SQLserver
		con_sbSQLServer = mssql_connection()

		cursorlite = con_sbSQLLite.cursor()
		now = datetime.now()
		nameCSV= str(now.strftime("%Y%m%d%H%M%S"))+'_'
		if option_menu <=5:
			query = '['+constants._sql_schema+'].['+constants._sql_SPname1+'] @OPTION_MENU ="'+ str(option_menu) + '", @FROMDATE ="'+ str(fromdate) + '", @TODATE = "'+ str(todate) + '", '
		else:
			query = '['+constants._sql_schema+'].['+constants._sql_SPname2+'] @OPTION_MENU ="'+ str(option_menu) + '", @FROMDATE ="'+ str(fromdate) + '", @TODATE = "'+ str(todate) + '", '
			
		data = get_data_from_sql(query)
		if len(data) <=0:
			print('No datos para extraer')
			input("Se cerrará el programa... Vuelva a ejecutarlo.")
			sys.exit(0)
		else:
			#Directory_files_exports
			if option_menu == 1: 
				folder = os.path.join(constants._DirProyect, constants._DirClient + nameCSV+'clients'+constants._FileExt)
				cursorlite.execute("INSERT INTO [tblexport] VALUES(null, 1,'"+constants._DirClient+nameCSV+'clients'+constants._FileExt+"','"+str(fromdate)+"','"+str(todate)+"', 1, 0,'"+str(now.strftime("%Y-%m-%d %H:%M:%S"))+"');")
			elif option_menu == 2: 
				folder = os.path.join(constants._DirProyect, constants._DirAddress + nameCSV+'address'+constants._FileExt)
				cursorlite.execute("INSERT INTO [tblexport] VALUES(null, 2,'"+constants._DirAddress+nameCSV+'address'+constants._FileExt+"','"+str(fromdate)+"','"+str(todate)+"', 1, 0,'"+str(now.strftime("%Y-%m-%d %H:%M:%S"))+"');")
			elif option_menu == 3: 
				folder = os.path.join(constants._DirProyect, constants._DirCreditCard + nameCSV+'creditcards' +constants._FileExt)
				cursorlite.execute("INSERT INTO [tblexport] VALUES(null, 3,'"+constants._DirCreditCard+nameCSV+'creditcards'+constants._FileExt+"','"+str(fromdate)+"','"+str(todate)+"', 1, 0,'"+str(now.strftime("%Y-%m-%d %H:%M:%S"))+"');")
			elif option_menu == 4: 
				folder = os.path.join(constants._DirProyect, constants._DirEmail + nameCSV+'emails'+constants._FileExt)
				cursorlite.execute("INSERT INTO [tblexport] VALUES(null, 4,'"+constants._DirEmail+nameCSV+'emails'+constants._FileExt+"','"+str(fromdate)+"','"+str(todate)+"', 1, 0,'"+str(now.strftime("%Y-%m-%d %H:%M:%S"))+"');")
			elif option_menu == 5: 
				folder = os.path.join(constants._DirProyect, constants._DirPhone + nameCSV+'phones'+constants._FileExt)
				cursorlite.execute("INSERT INTO [tblexport] VALUES(null, 5,'"+constants._DirPhone+nameCSV+'phones'+constants._FileExt+"','"+str(fromdate)+"','"+str(todate)+"', 1, 0,'"+str(now.strftime("%Y-%m-%d %H:%M:%S"))+"');")
			elif option_menu == 6: 
				folder = os.path.join(constants._DirProyect, constants._DirProduct + nameCSV+'products' +constants._FileExt)
				cursorlite.execute("INSERT INTO [tblexport] VALUES(null, 6,'"+constants._DirProduct+nameCSV+'products'+constants._FileExt+"','"+str(fromdate)+"','"+str(todate)+"', 1, 0,'"+str(now.strftime("%Y-%m-%d %H:%M:%S"))+"');")
			elif option_menu == 7: 
				folder = os.path.join(constants._DirProyect, constants._DirOrder + nameCSV+'orders' +constants._FileExt)
				cursorlite.execute("INSERT INTO [tblexport] VALUES(null, 7,'"+constants._DirOrder+nameCSV+'orders'+constants._FileExt+"','"+str(fromdate)+"','"+str(todate)+"', 1, 0,'"+str(now.strftime("%Y-%m-%d %H:%M:%S"))+"');")

			access = "w"
			newline = {"newline": ""}
		print (folder)
		#with open("test.csv", "w") as outfile: #newfile avoid empty rows betwen
		with open (folder, access, **newline) as outfile:
			writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
			#writer.writerow(["tblclientid", "tblclientusername", "tblclientpassword", "tblclientmigrate"])
			for row in data:
				print (row)
				writer.writerow(row)
		return "0"	
	except IOError as e:
		print("Error {0} Getting data from MSSQL: {1}".format(e.errno,e.strerror))
	finally:
		con_sbSQLLite.commit()
		con_sbSQLServer.close()
		con_sbSQLLite.close()

def submenu():
	os.system('cls') # NOTA para Linux tienes que cambiar cls por clear
	print ("Seleccione la información que desea extraer:")
	print ("\t1 - Clientes del sistema.")
	print ("\t2 - Direcciones de los clientes.")
	print ("\t3 - Tarjetas de crédito de los clientes.")
	print ("\t4 - Direcciones de correo de los clientes.")
	print ("\t5 - Números de teléfono de los clientes.")
	print ("\t6 - Catálogo de productos del sistema.")
	print ("\t7 - Órdenes de compras.")
	print ("\t0 - Volver al Menú_Principal.")	

def submenu2():
	os.system('cls') # NOTA para Linux tienes que cambiar cls por clear
	print ("Seleccione la información que desea importar a: "+constants._postgre_version+".")
	print ("\t1 - Clientes del sistema.")
	print ("\t2 - Direcciones de los clientes.")
	print ("\t3 - Tarjetas de crédito de los clientes.")
	print ("\t4 - Direcciones de correo de los clientes.")
	print ("\t5 - Números de teléfono de los clientes.")
	print ("\t6 - Catálogo de productos del sistema.")
	print ("\t7 - Órdenes de compras.")
	print ("\t0 - Volver al Menú_Principal.")		

def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls') # NOTA para Linux tienes que cambiar cls por clear
	print ("Menú_Principal")
	print ("Selecciona una opción:")
	print ("\t1 - Ejecutar nueva extracción desde "+constants._sql_version+".")
	print ("\t2 - Eliminar órdenes de compra y clientes.")
	print ("\t3 - Ver bitácora de eventos desde "+constants._sqlite_version+".")
	print ("\t0 - Salir.")

while True:
	# Mostramos el menu
	menu()
	# solicitamos una opción al usuario
	optionMenu = input("Digitela aquí >> ")

	if optionMenu=="1":
		submenu()
		cont = 0;	
		while True:
			if cont>0:
				submenu()
			# solicitamos una opción al usuario
			optionSubMenu = int(input("Digitela aquí >> "))
			from_date = ""
			to_date = ""
			now2 = datetime.now()
			if optionSubMenu <=7 and optionSubMenu>=1:
				print ("")
				print ("Por favor brinde fechas solicitadas con formato: (Año-Mes-Día), Ejemplo: "+str(now2.strftime("%Y-%m-%d")))
				from_date = input("FROM >> ")
				to_date = input("TO >> ")
				extractor(constants._sql_SPname1, 
							optionSubMenu, 
							datetime.strptime(from_date, "%Y-%m-%d"), 
							datetime.strptime(to_date, "%Y-%m-%d"))
				input("\npulsa una tecla para continuar")
				cont=cont+1
			elif optionSubMenu==0:
				break
			else:
				print ("")
				input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")	
		
	elif optionMenu=="2":
		print ("qw")

	elif optionMenu=="3":
		#Sandbox Conn SQLite
		con_sbSQLLite = sqlite_connection()
		cursorlite = con_sbSQLLite.cursor()
		print ("")
		cursorlite.execute("SELECT tblexport.tblexportid AS 'ID',"+
							"tbltable.tbltablename AS 'TABLA DE ORIGEN',"+
							"tblexport.tblexportfilecsv AS 'CSV',"+
							"tblexport.tblexportcreate AS 'FECHA_EXTRAJO' "+
							"FROM tblexport JOIN tbltable ON tblexport.tblexporttableid = tbltable.tbltablesid")
		for i in cursorlite:
			print("El "+str(i[3])+
			" se extrajo este .CSV: "+str(i[2])+
			" de la Tabla: "+str(i[1]))
			print("\n")

		con_sbSQLLite.commit()
		con_sbSQLLite.close()
		input("\npulsa una tecla para continuar")

	elif optionMenu=="0":
		break

	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")