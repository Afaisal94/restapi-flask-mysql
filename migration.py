import mysql.connector
from database import database

db = database()
cursor = db.cursor()

def create_table_users():
    try:
        sql = """CREATE TABLE users (
              id INT AUTO_INCREMENT PRIMARY KEY,
              name VARCHAR(255),
              email VARCHAR(255),
              password VARCHAR(255)
              )
              """
        cursor.execute(sql)
        print("- Users Table created successfully .....")
    except:
        print("- Users Table Already Exist ! .....")

# Execute :
if db.is_connected():
  print("- Connecting to Database successfully .....")
  create_table_users()