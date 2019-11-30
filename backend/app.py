from flask import Flask
import BusinessObjects as bo 

app = Flask(__name__)

@app.route("/")
def hello():
    c1 = bo.Customer(1, 'DAU xanh', 'Peter', '566 Nui Thanh', 'Danang', '50000', 'Vietnam')
    return c1.CustomerName

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)