import pymssql
import psycopg2

#conectionToSQL
_sql_server = "localhost"
_sql_database = "B89694"
_sql_server_port = 1433
_sql_user = "antony"
_sql_password = "1992"


#conectionToPostgreSQL
_postgre_server = "localhost"
_postgre_database = "name"
_postgre_server_port = "5432"
_postgre_user = "postgres"
_postgre_password = "postgres"

#SQL Connection
def mssql_connection():
    try:
        cnx=pymssql.connect(server=_sql_server,
                           port=_sql_server_port,
                           user=_sql_user,
                           password=_sql_password,
                           database=_sql_database)
        return cnx
    except:
        print ('Error MSSQL connection')

#Postgre Connection
def postgreSql_Connection():
    try:
        cnx=psycopg2.connect("host="+_postgre_server+
                            "dbname="+_postgre_database+
                            "user="+_postgre_user+
                            "password="+_postgre_password+
                            "port="+_postgre_server_port)
        return cnx
    except:
        print ('Error postgre connection')


def get_data_from_sql(sp):
    try:
        con=mssql_connection()
        cur=con.cursor()
        cur.execute("")
        con.commit()
        
        return
     except IOError as e:
        print ('Error {0} Getting data from MSSQL: {1}'. format(e.errno,e.strerror))    
        






















