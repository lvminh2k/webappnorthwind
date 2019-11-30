import psycopg2
class Customer:
    def __init__(self, ConnectionString):
        self.ConnectionString = ConnectionString
    def insert(self, customer):
        con = None
        try:
            con = psycopg2.connect(self.ConnectionString)
            cur = con.cursor()
            sql = "INSERT INTO TblCustomers(CustomerName, ContactName, Address, City, PostalCode, Country) VALUES (%s, %s, %s, %s, %s, %s)"
            record_to_insert = (customer.CustomerName, customer.ContactName, customer.Address, customer.City, customer.PostalCode, customer.Country)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert TblCustomers successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
                
if __name__ == "__main__":
    print('this is data object package')