'''
Project : car rental system

class Custmer, Cars, customers and Rentals
Modules : car inventory, cutomer information, and rental transaction

inventory- how many cars available, 
create cars, cutomers, 
define rentals as per hour/day/monthly,

'''
from car_inventory import Car
from customer_information import Customer
from rental_transaction import Rentals

objCar=Car()
objCustomer=Customer()
objRental=Rentals()

def menu():
    while True:
        print('Choose menu : \n')
        print(f'\t1. Add Car\n\t2. Available Cars\n\t3. Get Car on Rent\n\t4. Return_Car\n\t5. Show all Customers\n\t6. Exit')
        
        menu=int(input('Enter menu : '))
        if menu==1:
            objCar.create_car() 
            
        elif menu==2:
            objCar.display_car()
            
        elif menu==3:
            print()
            Id=int(input('Enter Id of Car you want get on Rent : '))
            objCar.display_car(Id)
            objRental.Get_Car_On_Rent(Id)
            print()
            
        elif menu==4:
            objRental.Return_Car()
            
            
            
        elif menu==5:
            objCustomer.display_customer()
            
            
        elif menu==6:
            print('Program ending...')
            break
    
menu()


'''
we can add cars
we can see available cars 
we get car on rent
we can return a car
we can see list of customers

'''