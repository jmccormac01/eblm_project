"""
All database interaction for the flask-eblm project
"""
from contextlib import contextmanager
import pymysql

# pylint: disable=invalid-name

@contextmanager
def openDb():
    """
    Open a connection to the EBLM db
    """
    with pymysql.connect(host='localhost', db='eblm',
                         password='mysqlpassword',
                         cursorclass=pymysql.cursors.DictCursor) as cur:
        yield cur

def getAllEblmParameters():
    """
    Function to grab the full list of EBLMs from db
    """
    qry = """
        SELECT *
        FROM eblm_parameters
        """
    with openDb() as cur:
        cur.execute(qry)
        results = cur.fetchall()
    return results

def getAllStellarParameters():
    """
    Function to grab all stellar parameters from db
    """
    qry = """
        SELECT *
        FROM dwarf_star_properties
        """
    with openDb() as cur:
        cur.execute(qry)
        results = cur.fetchall()
    return results
