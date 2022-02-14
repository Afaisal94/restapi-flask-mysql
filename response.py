from flask import jsonify, make_response

# RESPONSE SUCCESS
def success(values, message):
    res = {
        'data' : values,
        'message': message
    }

    return make_response(jsonify(res)), 200

# RESPONSE BAD REQUEST
def badRequest(values, message):
    res = {
        'data' : values,
        'message': message
    }

    return make_response(jsonify(res)), 400

# ARRAY TABLE USERS
def array_users(datas):
    values = []

    for data in datas:
        dict = {}
        dict['id'] = data[0]
        dict['name'] = data[1]
        dict['email'] = data[2]
        dict['password'] = data[3]

        values.append(dict)

    return values

# SINGLE OBJECT TABLE USERS
def obj_users(data):

    dict = {}
    dict['id'] = data[0]
    dict['name'] = data[1]
    dict['email'] = data[2]
    dict['password'] = data[3]

    return dict