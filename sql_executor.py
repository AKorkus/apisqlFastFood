# ex_03.py
import sqlite3
from sqlite3 import Error

# Create Connection............................................................................................................
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Połączenie zakonczone sukcesem!")
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn


# Execute SQL Command........................................................................................................
def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
       conn.commit()
       print(f"Działanie {sql[:20]}... zakończone sukcesem!")
   except Error as e:
       print(e)

# Execute Select.............................................................................................................
def selektor(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    print("Select zakończony sukcesem!")
    return result

