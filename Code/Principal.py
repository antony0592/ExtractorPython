import os, sys, csv, datetime
from conf import mssql_connection, get_data_from_sql
from datetime import datetime
import constants

sp_name=""
def extractor(sp_name, option_menu, fromdate, todate):
	try:
		now = datetime.now()
		nameCSV= str(now.strftime("%Y%m%d%H%M%S"))+'_'
		if option_menu <=5:
			query = '['+constants._sql_schema+'].['+constants._sql_SPname1+'] @OPTION_MENU ="'+ str(option_menu) + '", @FROMDATE ="'+ str(fromdate) + '", @TODATE = "'+ str(todate) + '", '
		else:
			query = '['+constants._sql_schema+'].['+constants._sql_SPname2+'] @OPTION_MENU ="'+ str(option_menu) + '", @FROMDATE ="'+ str(fromdate) + '", @TODATE = "'+ str(todate) + '", '
		#Directory_files_exports
		if option_menu == 1: 
			folder = os.path.join(constants._DirProyect, constants._DirClient + nameCSV+'clients'+constants._FileExt)
		elif option_menu == 2: 
			folder = os.path.join(constants._DirProyect, constants._DirAddress + nameCSV+'address'+constants._FileExt)
		elif option_menu == 3: 
			folder = os.path.join(constants._DirProyect, constants._DirCreditCard + nameCSV+'creditcards' +constants._FileExt)
		elif option_menu == 4: 
			folder = os.path.join(constants._DirProyect, constants._DirEmail + nameCSV+'emails'+constants._FileExt)
		elif option_menu == 5: 
			folder = os.path.join(constants._DirProyect, constants._DirPhone + nameCSV+'phones'+constants._FileExt)
		elif option_menu == 6: 
			folder = os.path.join(constants._DirProyect, constants._DirProduct + nameCSV+'products' +constants._FileExt)
		elif option_menu == 7: 
			folder = os.path.join(constants._DirProyect, constants._DirOrder + nameCSV+'orders' +constants._FileExt)
		#Sandbox Conn
		con_sb = mssql_connection()
		data = get_data_from_sql(query)

		if len(data) <=0:
			print('No data retrieved')
			sys.exit(0)
		else:
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
		con_sb.close()

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

def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls') # NOTA para Linux tienes que cambiar cls por clear
	print ("Menú_Principal")
	print ("Selecciona una opción:")
	print ("\t1 - Ejecutar nueva extracción desde "+constants._sql_version+".")
	print ("\t2 - Importar CSV a "+constants._postgre_version+".")
	print ("\t0 - Salir")

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
		print ("")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")

	elif optionMenu=="0":
		break

	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")