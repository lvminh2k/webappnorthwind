from flask import Flask
from flask_restful import Resource, reqparse, request
import os
import BusinessObjects as bo 
import DataObjects as do

app = Flask(__name__)

db_ip = os.getenv('db_ip') #'10.0.2.15'
ConnectionData = {}
ConnectionData['user'] = 'postgres'
ConnectionData['password'] = 'postgres'
ConnectionData['host'] = str(db_ip)
ConnectionData['port'] = '5432'
ConnectionData['database'] = 'northwind'

@app.route('/')
def hello():    
    return 'this is backend'

@app.route('/test_insert')
def test_insert():
    #ConnectionString = 'database=northwind user=postgres password=postgres host=10.0.2.15 port=5432'
    c2 = do.Customer(ConnectionData)
    c1 = bo.Customer(1, 'DAU xanh', 'Peter', '566 Nui Thanh', 'Danang', '50000', 'Vietnam')
    s1 = c2.insert(c1)
    return s1

@app.route('/user/get_by_id', methods=['POST'])
def user_get_by_id():
    user_id = request.data['user_id']
    return user_id

@app.route('/user/insert', methods=['POST'])
def user_insert():
    return 'ok'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)