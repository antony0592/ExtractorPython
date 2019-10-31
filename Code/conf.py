import pymssql
import psycopg2
import sqlite3
import constants

#SQL Connection
def mssql_connection():
    try:
        cnx=pymssql.connect(server=constants._sql_server,
                           port=constants._sql_server_port,
                           user=constants._sql_user,
                           password=constants._sql_password,
                           database=constants._sql_database)
        return cnx
    except:
        print ('Error MSSQL connection')

#Postgre Connection
def postgreSql_Connection():
    try:
        cnx=psycopg2.connect(host=constants._postgre_server, 
                            database=constants._postgre_database, 
                            user=constants._postgre_user, 
                            password=constants._postgre_password)
        return cnx
    except:
        print ('Error PostgreSQL connection')

#Postgre Connection
def sqlite_connection():
    try:
        cnx=sqlite3.connect(constants._DirDBSQLite)
        return cnx
    except:
        print ('Error SQLite connection')


#Extracting Data
def get_data_from_sql(sp):
    try:
        con = mssql_connection()
        cur = con.cursor()
        cur.execute("execute {} @OUTPUT_IS_SUCCESSFUL=0, @OUTPUT_IS_STATUS=0".format(sp))
        data_return = cur.fetchall()
        con.commit()
        
        return data_return

    except IOError as e:
        print ("Error {0} Getting data from MSSQL: {1}". format(e.errno, e.strerror))    
        