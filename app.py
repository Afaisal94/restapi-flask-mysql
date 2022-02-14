from flask import Flask, request
import mysql.connector
from response import *
from database import database

app = Flask(__name__)

db = database()
cursor = db.cursor()

@app.route('/')
def index():
    return "index page"

@app.route('/users', methods=['GET','POST'])
def users():
    if request.method == 'POST':

        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        input = [{
            'name': name,
            'email': email,
            'password': password
        }]

        sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        val = (name, email, password)
        cursor.execute(sql, val)
        db.commit()
        return success(input, "success")

    else:

        sql = "SELECT * FROM users"
        cursor.execute(sql)
        users = cursor.fetchall()
        data = array_users(users)
        return success(data, "success")

@app.route('/user/<int:id>', methods=['GET','PUT','DELETE'])
def user(id):
    if request.method == 'GET':

        try:
            sql = "SELECT * FROM users WHERE id = " + str(id)
            cursor.execute(sql)
            users = cursor.fetchone()
            data = obj_users(users)
            return success(data, "success")
        except:
            return badRequest([], 'Data Not Found')

    elif request.method == 'PUT':

        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        input = [{
            'name': name,
            'email': email,
            'password': password
        }]

        sql = "UPDATE users SET name = %s, email = %s, password = %s WHERE id = %s"
        val = (name, email, password, id)
        cursor.execute(sql, val)
        db.commit()
        return success(input, "success")

    elif request.method == 'DELETE':

        sql = "DELETE FROM users WHERE id = " + str(id)
        cursor.execute(sql)
        db.commit()
        return success('', 'Success Deleted')

if __name__ == '__main__':
    app.run(debug=True)