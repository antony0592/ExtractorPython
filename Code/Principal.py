import os, sys, csv
from conf import mssql_connection, get_data_from_sql
import constants

def extractor():
	try:
		query = '['+constants._sql_schema+'].['+constants._sql_SPname+']'

		#Sandbox
		con_sb = mssql_connection()
		data = get_data_from_sql(query)

		if len(data) <=0:
			print('No data retrieved')
			sys.exit(0)
		else:
			access = "w"
			newline = {"newline":""}

		#with open("test.csv", "w") as outfile: #newfile avoid empty rows betwen
		with open ("test.csv", access, **newline) as outfile:
			writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
			writer.writerow(
			["ID", "PERSONAL_ID", "NAME", "PHONE", "ADDRESS"]
		)
		for row in data:
			print (row)
			writer.writerow(row)

	except IOError as e:
		print("Error {0} Getting data from MSSQL: {1}".format(e.errno,e.strerror))
	finally:
		con_sb.close()


def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls') # NOTA para Linux tienes que cambiar cls por clear
	print ("Selecciona una opción:")
	print ("\t1 - Ejecutar nueva extracción desde "+constants._sql_version+".")
	print ("\t2 - Importar CSV a "+constants._postgre_version+".")
	print ("\t0 - Salir")

while True:
	# Mostramos el menu
	menu()
	# solicitamos una opción al usuario
	opcionMenu = input("Digitela aquí >> ")

	if opcionMenu=="1":
		print ("")
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")

	elif opcionMenu=="2":
		print ("")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")

	elif opcionMenu=="3":

		print ("")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")

	elif opcionMenu=="0":
		break

	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")