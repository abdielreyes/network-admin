from flask import Flask, jsonify, request
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='n0m3l0',
                        authSource="admin")
    db = client["netadmin_db"]
    return db

@app.route('/')
def ping_server():
    return "Welcome to home"

@app.route('/api/v1/users')
def get_stored_users():
    db = get_db()
    _users = db.user_tb.find()
    users = [{"id" : str(user["_id"]),"username": user["username"], "email" : user["email"]} for user in _users]
    return jsonify({"user":users})

@app.route('/api/v1/users/add',methods=['POST'])
def store_new_user():
    db = get_db()
    username = request.args.get('username')
    email = request.args.get('email')
    password = request.args.get('password')
    user = {
            "username": username,
            "email" : email,
            "password" : password
            }
    user_id = db.user_tb.insert_one(user).inserted_id
    return ''' {} saved '''.format(user_id)

@app.route('/api/v1/users/delete',methods=['DELETE'])
def delete_user():
    db = get_db()
    id = request.args.get('id')
    deleted = db.user_tb.find_one_and_delete({"_id" : ObjectId(id) })
    if deleted :
        return ''' {},{} deleted '''.format(str(deleted["_id"],deleted["username"]))
    else:
        return '''{} not found'''.format(id)

@app.route('/api/v1/users/update',methods=['PATCH'])
def update_user():
    db = get_db()
    id = request.args.get('id')
    others = request.args
    updated = db.user_tb.find_one_and_update({"_id" : ObjectId(id) }, {"$set" : others})
    if updated :
        return ''' {} updated '''.format(str(updated["_id"]))
    else:
        return '''{} not found'''.format(id)

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
