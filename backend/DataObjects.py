import psycopg2
class Customer:
    def __init__(self, ConnectionString):
        self.ConnectionString = ConnectionString
    def createTable(self):
        #database='postgres-northwind', user='postgres', password='postgres', host="127.0.0.1", port="5432"
        con = None
        try:
            con = psycopg2.connect(self.ConnectionString)
            cur = con.cursor()
            cur.execute("CREATE TABLE TblCustomers (CustomerID int IDENTITY(1,1) PRIMARY KEY, CustomerName varchar(255), ContactName varchar(255), Address varchar(255), City varchar(255), PostalCode varchar(255), Country varchar(255));")
            con.commit()
            con.close()
            return 'Create TblCustomers successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
    def createDB(self):
        con = None
        try:
            con = psycopg2.connect(self.ConnectionString)
            cur = con.cursor()
            cur.execute("CREATE DATABASE northwind;")
            con.commit()
            con.close()
            return 'Create DB northwind successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
if __name__ == "__main__":
    print('this is data object package')