
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="pythonprojectsdb")

class Customer:
    def display_customer(self):
        mycursor = mydb.cursor()
        # fetching records in descending order
        # fetching records in descending order
        mycursor.execute("SELECT * FROM tblCustomer ORDER BY CustId DESC")
        data=mycursor.fetchall()
        for row in data:
            print(row)
            
        mycursor.close()