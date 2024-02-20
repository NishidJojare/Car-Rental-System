# Car Rental System

## Project Overview
This Python-based Car Rental System is designed to manage car inventory, customer information, and rental transactions. The system allows users to perform various operations such as adding cars, checking available cars, renting a car, returning a car, and viewing a list of customers.

## Modules
1. **car_inventory.py:** Manages car-related operations, including creating cars and displaying available cars.
2. **customer_information.py:** Handles customer information and provides functionality to display customer details.
3. **rental_transaction.py:** Implements rental transactions, allowing users to rent and return cars.

## Classes
### 1. Car Class
- **Attributes:**
  - CarName
  - CarModel
  - CarNo
  - Rent
  - IsAvailable

- **Methods:**
  - `create_car`: Adds a new car to the inventory.
  - `display_car`: Displays information about available cars.

### 2. Customer Class
- **Methods:**
  - `display_customer`: Fetches and displays customer information in descending order.

### 3. Rentals Class
- **Methods:**
  - `Get_Car_On_Rent`: Allows customers to rent a car based on various rental options (per hour, per day, per month).
  - `Return_Car`: Handles the return of a rented car.

## Main Script (main.py)
The main script integrates the functionality of the three modules and provides a user-friendly menu for interaction.

### Menu Options:
1. **Add Car:** Add a new car to the inventory.
2. **Available Cars:** Display available cars.
3. **Get Car on Rent:** Rent a specific car by providing its ID.
4. **Return Car:** Return a rented car.
5. **Show all Customers:** Display a list of all customers.
6. **Exit:** End the program.

## How to Use
1. Run `main.py`.
2. Choose from the menu options to perform desired operations.
3. Follow on-screen instructions for specific tasks such as renting a car.

## Example Usage
```python
# Run the main script
menu()
