import os, sys, csv, datetime
from conf import postgreSql_Connection, sqlite_connection
from datetime import datetime
import constants

def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls') # NOTA para Linux tienes que cambiar cls por clear
	print ("Menú_Principal")
	print ("Seleccione la información que desea importar a: "+constants._postgre_version+".")
	print ("\t1 - Clientes del sistema.")
	print ("\t2 - Direcciones de los clientes.")
	print ("\t3 - Tarjetas de crédito de los clientes.")
	print ("\t4 - Direcciones de correo de los clientes.")
	print ("\t5 - Números de teléfono de los clientes.")
	print ("\t6 - Catálogo de productos del sistema.")
	print ("\t7 - Órdenes de compras.")
    #print ("\t8 - Ver Bitácora de BulkLOADs.")
	print ("\t0 - Salir.")	

def upload_csv_file_to_postgre():
    try:    
        con_sbSQLLite = sqlite_connection()
        cursorlite = con_sbSQLLite.cursor()
        con_postgre = postgreSql_Connection()    
        cur = con_postgre.cursor()
        now = datetime.now()
        while True:
            # Mostramos el menu
            menu()
            # solicitamos una opción al usuario
            optionMenu = input("Digitela aquí >> ")

            if optionMenu=="1": 
                RutaCSV = os.path.join(constants._DirProyect, constants._DirClient +'')
                print ("ELEGISTE CLIENTES: Copie el nombre del archivo a importar:")  
                fileslist = os.listdir(RutaCSV)
                for filename in fileslist:
                    print("Nombre del CSV: "+filename)
                namefile = input("Escriba o pegue el nombre del archivo >> ")
                filecsv=namefile
                namefile= RutaCSV+namefile
                print ("CARGANDO ARCHIVO A POSTGRE.......")
                with open(namefile,'r') as f:
                    cur.copy_from(f, '"PROYECT".tblclient', sep=',')
                con_postgre.commit()
                cursorlite.execute("INSERT INTO [tblimport] VALUES(null, 1,'"+filecsv+"', 1,'"+str(now.strftime("%Y-%m-%d %H:%M:%S"))+"');")
                con_sbSQLLite.commit()
                print ("ARCHIVO CARGADO A POSTGRE CON EXITO.......")
                input("\nPulsa una tecla para continuar")

            elif optionMenu=="2":
                RutaCSV = os.path.join(constants._DirProyect, constants._DirAddress +'')
                print ("ELEGISTE DIRECCIONES: Copie el nombre del archivo a importar:")  
                fileslist = os.listdir(RutaCSV)
                for filename in fileslist:
                    print("Nombre del CSV: "+filename)
                namefile = input("Escriba o pegue el nombre del archivo >> ")
                filecsv=namefile
                namefile= RutaCSV+namefile
                print ("CARGANDO ARCHIVO A POSTGRE.......")
                with open(namefile,'r') as f:
                    cur.copy_from(f, '"PROYECT".tbladdress', sep=',')
                con_postgre.commit()
                cursorlite.execute("INSERT INTO [tblimport] VALUES(null, 2,'"+filecsv+"', 1,'"+str(now.strftime("%Y-%m-%d %H:%M:%S"))+"');")
                con_sbSQLLite.commit()
                print ("ARCHIVO CARGADO A POSTGRE CON EXITO.......")
                input("\nPulsa una tecla para continuar")

            elif optionMenu=="3":
                RutaCSV = os.path.join(constants._DirProyect, constants._DirCreditCard +'')
                print ("ELEGISTE TARJETAS DE CRÉDITO: Copie el nombre del archivo a importar:")  
                fileslist = os.listdir(RutaCSV)
                for filename in fileslist:
                    print("Nombre del CSV: "+filename)
                namefile = input("Escriba o pegue el nombre del archivo >> ")
                filecsv=namefile
                namefile= RutaCSV+namefile
                print ("CARGANDO ARCHIVO A POSTGRE.......")
                with open(namefile,'r') as f:
                    cur.copy_from(f, '"PROYECT".tblcreditcard', sep=',')
                con_postgre.commit()
                cursorlite.execute("INSERT INTO [tblimport] VALUES(null, 3,'"+filecsv+"', 1,'"+str(now.strftime("%Y-%m-%d %H:%M:%S"))+"');")
                con_sbSQLLite.commit()
                print ("ARCHIVO CARGADO A POSTGRE CON EXITO.......")
                input("\nPulsa una tecla para continuar")

            elif optionMenu=="4":
                RutaCSV = os.path.join(constants._DirProyect, constants._DirEmail +'')
                print ("ELEGISTE EMAILS: Copie el nombre del archivo a importar:")  
                fileslist = os.listdir(RutaCSV)
                for filename in fileslist:
                    print("Nombre del CSV: "+filename)
                namefile = input("Escriba o pegue el nombre del archivo >> ")
                filecsv=namefile
                namefile= RutaCSV+namefile
                print ("CARGANDO ARCHIVO A POSTGRE.......")
                with open(namefile,'r') as f:
                    cur.copy_from(f, '"PROYECT".tblemail', sep=',')
                con_postgre.commit()
                cursorlite.execute("INSERT INTO [tblimport] VALUES(null, 4,'"+filecsv+"', 1,'"+str(now.strftime("%Y-%m-%d %H:%M:%S"))+"');")
                con_sbSQLLite.commit()
                print ("ARCHIVO CARGADO A POSTGRE CON EXITO.......")
                input("\nPulsa una tecla para continuar")

            elif optionMenu=="5":
                RutaCSV = os.path.join(constants._DirProyect, constants._DirPhone +'')
                print ("ELEGISTE TELÉFONOS: Copie el nombre del archivo a importar:")  
                fileslist = os.listdir(RutaCSV)
                for filename in fileslist:
                    print("Nombre del CSV: "+filename)
                namefile = input("Escriba o pegue el nombre del archivo >> ")
                filecsv=namefile
                namefile= RutaCSV+namefile
                print ("CARGANDO ARCHIVO A POSTGRE.......")
                with open(namefile,'r') as f:
                    cur.copy_from(f, '"PROYECT".tblphone', sep=',')
                con_postgre.commit()
                cursorlite.execute("INSERT INTO [tblimport] VALUES(null, 5,'"+filecsv+"', 1,'"+str(now.strftime("%Y-%m-%d %H:%M:%S"))+"');")
                con_sbSQLLite.commit()
                print ("ARCHIVO CARGADO A POSTGRE CON EXITO.......")
                input("\nPulsa una tecla para continuar")

            elif optionMenu=="6":
                RutaCSV = os.path.join(constants._DirProyect, constants._DirProduct +'')
                print ("ELEGISTE PRODUCTOS: Copie el nombre del archivo a importar:")  
                fileslist = os.listdir(RutaCSV)
                for filename in fileslist:
                    print("Nombre del CSV: "+filename)
                namefile = input("Escriba o pegue el nombre del archivo >> ")
                filecsv=namefile
                namefile= RutaCSV+namefile
                print ("CARGANDO ARCHIVO A POSTGRE.......")
                with open(namefile,'r') as f:
                    cur.copy_from(f, '"PROYECT".tblproduct', sep=',')
                con_postgre.commit()
                cursorlite.execute("INSERT INTO [tblimport] VALUES(null, 6,'"+filecsv+"', 1,'"+str(now.strftime("%Y-%m-%d %H:%M:%S"))+"');")
                con_sbSQLLite.commit()
                print ("ARCHIVO CARGADO A POSTGRE CON EXITO.......")
                input("\nPulsa una tecla para continuar")

            elif optionMenu=="7":
                RutaCSV = os.path.join(constants._DirProyect, constants._DirOrder +'')
                print ("ELEGISTE ORDENES: Copie el nombre del archivo a importar:")  
                fileslist = os.listdir(RutaCSV)
                for filename in fileslist:
                    print("Nombre del CSV: "+filename)
                namefile = input("Escriba o pegue el nombre del archivo >> ")
                filecsv=namefile
                namefile= RutaCSV+namefile
                print ("CARGANDO ARCHIVO A POSTGRE.......")
                with open(namefile,'r') as f:
                    cur.copy_from(f, '"PROYECT".tblorder', sep=',')
                con_postgre.commit()
                cursorlite.execute("INSERT INTO [tblimport] VALUES(null, 7,'"+filecsv+"', 1,'"+str(now.strftime("%Y-%m-%d %H:%M:%S"))+"');")
                con_sbSQLLite.commit()
                print ("ARCHIVO CARGADO A POSTGRE CON EXITO.......")
                input("\nPulsa una tecla para continuar")


            elif optionMenu=="8":
                #Sandbox Conn SQLite
                con_sbSQLLite = sqlite_connection()
                cursorlite = con_sbSQLLite.cursor()
                print ("")
                cursorlite.execute("SELECT tblimport.tblimportid AS 'ID',"+
                                    "tbltable.tbltablename AS 'TABLA DE ORIGEN',"+
                                    "tblimport.tblimportfilecsv AS 'CSV',"+
                                    "tblimport.tblimportcreate AS 'FECHA_EXTRAJO' "+
                                    "FROM tblimport JOIN tbltable ON tblimport.tblimporttableid = tbltable.tbltablesid")
                for i in cursorlite:
                    print("El "+str(i[3])+
                    " se cargó este .CSV: "+str(i[2])+
                    " de la Tabla: "+str(i[1]))

                con_sbSQLLite.commit()
                con_sbSQLLite.close()
                input("\npulsa una tecla para continuar")    

            elif optionMenu=="0":
                break

            else:
                print ("")
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
      
    except IOError as e:
        print("Error {0} Getting data from PostgreSQL: {1}".format(e.errno,e.strerror))
    finally:
        con_sbSQLLite.close()
        con_postgre.close()

upload_csv_file_to_postgre()