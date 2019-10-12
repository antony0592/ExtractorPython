import constants
import pymssql
import psycopg2

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
        cnx=psycopg2.connect("host="+constants._postgre_server+
                            "dbname="+constants._postgre_database+
                            "user="+constants._postgre_user+
                            "password="+constants._postgre_password+
                            "port="+constants._postgre_server_port)
        return cnx
    except:
        print ('Error PostgreSQL connection')

#Extracting Data
def get_data_from_sql(sp):
    try:
        con=mssql_connection()
        cur=con.cursor()
        cur.execute("execute {} @output_IS_SUCCESSFUL=0, @output_STATUS=0".format(sp))
        data_return = cur.fetchall()
        con.commit()
        
        return data_return

    except IOError as e:
        print ("Error {0} Getting data from MSSQL: {1}". format(e.errno, e.strerror))    
        