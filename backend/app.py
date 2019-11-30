from flask import Flask
import os
import BusinessObjects as bo 
import DataObjects as do

app = Flask(__name__)

db_ip = os.getenv("db_ip")

@app.route("/")
def hello():
    c1 = bo.Customer(1, 'DAU xanh', 'Peter', '566 Nui Thanh', 'Danang', '50000', 'Vietnam')
    return c1.CustomerName

@app.route("/create_table")
def create_table():
    ConnectionString = 'database=northwind user=postgres password=postgres host=10.0.2.15 port=5432'
    c2 = do.Customer(ConnectionString)
    s1 = c2.createTable()
    return s1

@app.route("/create_table")
def create_db():
    ConnectionString = 'user=postgres password=postgres host=10.0.2.15 port=5432'
    c2 = do.Customer(ConnectionString)
    s1 = c2.createDB()
    return s1

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)