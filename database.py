import mysql.connector

def database():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_simple_api"
    )
    return db