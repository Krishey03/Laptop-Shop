import datetime
from write import *

def sell():
    # Get the user information and validate it 
    while True:
        user_name = input("Please enter your name: ")
        if user_name == "":
            print("Empty Textfield.")
        else:
            break
    print("\n")
    
    while True: 
        phone_number = (input("Please enter your phone no: "))
        if phone_number.isdigit():
            phone_number = int(phone_number)
            break
        elif phone_number == "":
            print("Please enter a valid phone number!!!")
        else:
            print("Please enter a valid phone number!!!")

    print("\n")
    while True:
        user_address = input("Please enter your Address: ")
        if user_address == "":
            print("Empty Textfield.")
        else:
            break

    return user_name, phone_number, user_address

def plaptop():
    purchased_laptops = []

    return purchased_laptops

    

def table1():
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("S.N \t\t Laptop Name \t\t Company Name \t\t Price \t\t Quantity \t Processor \t\t GPU")
    print("----------------------------------------------------------------------------------------------------------------------------------------")


#Ask the user for the serial number
def serial():
    serial_no = (input("Provide the serial number of the laptop you want to purchase: ")) 
    print("\n")
    while not serial_no.isdigit():
        serial_no = input("Please enter a valid serial number: ")
    serial_no = int(serial_no)

    return serial_no

#Ask the user for the serial number if the user inputs an invalid serial number
def checkserial():
    print("Please select an available Serial N.O.")
    print("\n")
    serial_no = int(input("Provide the serial number of the laptop you want to purchase: "))
    print("\n")
    
    return serial_no

#Valid the Quantity
def valid(laptop_dictionary, serial_no):    
    selected_laptop_quantity = laptop_dictionary[serial_no][3]

    return selected_laptop_quantity
    
def change_quantity(selected_laptop_quantity):
    while True:
        try:
            user_quantity = input("Enter the number of laptops you want to purchase: ")
            if not user_quantity:
                raise ValueError("Please provide a value")
            user_quantity = int(user_quantity)
            if user_quantity <= 0 or user_quantity > int(selected_laptop_quantity):
                raise ValueError("The quantity you are looking for is unavailable to purchase.")
            return user_quantity
        except ValueError:
            print("Invalid input: ")



#Update the text file     
def update(laptop_dictionary, serial_no, user_quantity):
    laptop_dictionary[serial_no][3] = int(laptop_dictionary[serial_no][3]) - int(user_quantity)

    dictionary(laptop_dictionary)

#get the purchased items from the user
def get(laptop_dictionary, serial_no, user_quantity, purchased_laptops):
    product_name = laptop_dictionary[serial_no][0]
    selected_laptop_quantity = user_quantity
    unit_price = laptop_dictionary[serial_no][2]
    item_price = laptop_dictionary[serial_no][2].replace("$", '')
    total_price = int(item_price)*int(selected_laptop_quantity)
    company_name = laptop_dictionary[serial_no][1]

    purchased_laptops.append([product_name, company_name, selected_laptop_quantity, unit_price, total_price])
    return product_name, unit_price, total_price, company_name
    

#Ask if the user wants to Buy more
def more():
    user_request = input("Would you like to purchase more? If yes press Y. If no press any other button.").upper()
    print("\n")
    shipping_cost = 200

    return shipping_cost, user_request



#Purchase code
#Purchase code
def table2 ():
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("S.N \t\t Laptop Name \t\t Company Name \t\t Price \t\t Quantity \t Processor \t\t GPU")
    print("----------------------------------------------------------------------------------------------------------------------------------------")


    

def serial2 ():
    #Get the provided serial number and validate it 
    serial_no = (input("Provide the serial number of the laptop you want to purchase: ")) 
    print("\n")
    while not serial_no.isdigit():
        serial_no = input("Please enter a valid serial number: ")
    serial_no = int(serial_no)
    return serial_no

    #Valid Quantity
def valid2 (laptop_dictionary, serial_no):
    while True:
        user_input = input("Enter the number of laptops you want to purchase: ")
        if user_input.strip() == "":
            print("Empty input")
        elif not user_input.isdigit():
            print("Invalid input. Please enter a valid number.")
        else:
            user_quantity = int(user_input)
            break


    selected_laptop_quantity = laptop_dictionary[serial_no][3]

    return selected_laptop_quantity, user_quantity

#Update the text file   
def update2(laptop_dictionary, serial_no, user_quantity):
    laptop_dictionary[serial_no][3] = int(laptop_dictionary[serial_no][3]) + int(user_quantity)
    dictionary (laptop_dictionary)

#get the purchased items from the user
def get2(laptop_dictionary, serial_no, user_quantity, purchased_laptops):
    product_name = laptop_dictionary[serial_no][0]
    selected_laptop_quantity = user_quantity
    unit_price = laptop_dictionary[serial_no][2]
    item_price = laptop_dictionary[serial_no][2].replace("$", '')
    total_price = int(item_price)*int(selected_laptop_quantity)
    company_name = laptop_dictionary[serial_no][1]
    
    purchased_laptops.append([product_name, company_name, selected_laptop_quantity, unit_price, total_price])
    return product_name, unit_price, total_price, item_price, company_name
    

#Get the user's request
def more2 ():
    user_request = input("Would you like to buy more? If YES press Y. If NO press any other button.").upper() #Converts value into Upper Case
    print("\n")
    return user_request
 
        
