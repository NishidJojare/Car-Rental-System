
from car_inventory import Car
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="pythonprojectsdb")


class Rentals:
    def Get_Car_On_Rent(self,Id=None):
        self.which_car=Id
        mycursor=mydb.cursor()
        mycursor.execute('SELECT * FROM tblCar WHERE CarId=%s AND IsAvailable=%s',(self.which_car,1))
        record=mycursor.fetchone()
        
 
        if record:
            print() # CustId, Name, Address, Mobile, CarId, CarName, Amount_payable
            self.name = input('Enter your name: ')
            self.address = input('Enter your address: ')
            self.mobile = int(input('Enter your mobile number: '))
            self.cost = 0

            print('How do you want to rent a Car\n\t1. per Hour\n\t2. per Day\n\t3. per Month')
            self.rent_type = int(input('Enter Choice: '))

            if self.rent_type == 1:
                rent = 100
                hours = int(input("Enter number of Hours for rental: "))
                self.cost = hours * rent
                self.flag = 1

            elif self.rent_type == 2:
                rent = 1500
                days = int(input("Enter number of Days for rental: "))
                self.cost = days * rent
                self.flag = 1

            elif self.rent_type == 3:
                rent = 10000
                months = int(input("Enter number of Months for rental: "))
                self.cost = months * rent
                self.flag = 1

            print()
            print(f"Name: {self.name}\nAddress: {self.address}\nMobile: {self.mobile}\nCar: {record[1]}")
            print(f'Total cost will be: {self.cost} Rs.')


            mycursor.execute('SELECT * FROM tblCar WHERE CarId=%s',(self.which_car,))
            car_detail=mycursor.fetchone()


            # Storing data into table tblCustomer
            mycursor.execute('INSERT INTO tblCustomer(Name,Address,Mobile,CarId,CarName,Amount_payable) VALUES(%s,%s,%s,%s,%s,%s)',(self.name, self.address, self.mobile, self.which_car, car_detail[1], self.cost))
            mydb.commit()
            
            
            if self.flag == 1:
                
                mycursor.execute('UPDATE tblCar SET IsAvailable=%s WHERE CarId=%s', (0, self.which_car))
                mydb.commit()

        else:
            print("Car is not available for rent or does not exist.")

        mycursor.close()
        
        
        
    def Return_Car(self):
        
        self.CarId=int(input('Enter the car Id : '))
        mycursor=mydb.cursor()
        mycursor.execute('SELECT * FROM tblCar WHERE CarId=%s and IsAvailable=%s',(self.CarId,0))
        data=mycursor.fetchone()
        print(data)
        print()
        if data:
            print('Car returned successfully...')
            mycursor.execute('UPDATE tblCar SET IsAvailable=%s WHERE CarId=%s', (1, self.CarId))
            mycursor.execute('DELETE FROM tblCustomer WHERE CarId=%s',(self.CarId,))
            mydb.commit()
         
        else:
            print('Car was not given on rent or may be does not exist.')   
        mycursor.close()
            
        