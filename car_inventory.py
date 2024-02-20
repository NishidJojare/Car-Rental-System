
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="pythonprojectsdb")
class Car:
    def create_car(self):
        self.CarName=input('Enter car name : ')
        self.CarModel=input('Enter car model : ')
        self.CarNo=input('Enter car number : ')
        self.Rent=input('Enter car rent : ')
        self.IsAvailable=int(input('Is car available for rent ?\n\tPress 1 for Yes\n\tPress 0 for No)'))
        
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO tblCar(CarName,CarModel,CarNo,Rent,IsAvailable) VALUES(%s,%s,%s,%s,%s)",(self.CarName,self.CarModel,self.CarNo,self.Rent,self.IsAvailable))
        mydb.commit()
        mycursor.close()
    
    
    
    def display_car(self,Id=None):
        self.which_car=Id
        
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM tblCar")
        data=mycursor.fetchall()
            
        if self.which_car:
            for row in data:
                if row[5]==1:
                    if self.which_car==row[0]:
                        print(f'Car Details : {row}')
                        break
                    
        else:
            for row in data:
                if row[5]==1:
                    print(f'Car Id : {row[0]}\tCar Name : {row[1]}')
                    
                    
        mycursor.close()
         
         
                    
    
    
        
        
    
        
    
        
            
    

