from read import *
from write import *
from operations import *
import datetime
now = datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d %H-%M-%S")
# import operations


print("\n")
print("=======================================================")
print("\t Welcome to Laptop Shop")
print("=======================================================")
print("\t Bafal, Kathmandu")
print("=======================================================")

laptop_dictionary = laptops()

# Asking and validating what the user wants to do
loop = True
while loop == True:
    print("1 to Sell")
    print("2 to Purchase")
    print("3 to Exit")
    
    while True:
        try:
            user_input = int(input("What do you want to do?"))
            if user_input <=0 or user_input > 3:
                raise ValueError("Please provide a valid number")
            break
        except ValueError:
            print("please provide a valid number")
        

    if user_input == 1:
        user_name, phone_number, user_address = sell()
        purchased_laptops = plaptop()

        buy_more = True
        while buy_more == True:
            table1()

            # Calling the function from read.py
            items()

            #Calling the function from operation.py
            serial_no = serial()

            #Valid the serial number
            while serial_no <= 0 or serial_no > len(laptop_dictionary):
                #Calling the function from operation.py
                serial_no  = checkserial()


            #Valid Quantity 
            selected_laptop_quantity = valid(laptop_dictionary, serial_no)


            #Valid Quantity
            user_quantity = change_quantity(selected_laptop_quantity)
            #Valid Quantity

            #Update the text file     
            update(laptop_dictionary, serial_no, user_quantity)
            #Update the text file


            #getting user purchased items
            product_name, unit_price, total_price, company_name = get(laptop_dictionary, serial_no, user_quantity, purchased_laptops)

            shipping_cost, user_request = more()

            #Validating the user input
            if user_request =="Y":
                buy_more = True
            else:
                total = 0
                for i in purchased_laptops:
                    total+=int(i[4])
                sum_total = total + shipping_cost

                # calling the function from write.py
                printsell(now, user_name, phone_number, user_address, shipping_cost, sum_total, purchased_laptops)

                # calling the function from write.py
                sellbill(user_name, date_time, now, phone_number, user_address, purchased_laptops, shipping_cost, sum_total)

                buy_more = False

                

    elif user_input == 2:
        #Getting the Distributor Name
        while True:
            distributor_name = input("Please enter the name of Distributor: ")
            if distributor_name == "":
                print("Textfield is empty.")
            else:
                break

        purchased_laptops = plaptop()

        buy_more = True
        while buy_more == True:
            table2()

            #calling the function from read.py
            items()

            serial_no = serial2()
            #Validate the privided serial number
            while serial_no <= 0 or serial_no > len(laptop_dictionary):
                serial_no  = checkserial()


            #Valid Quantity
            selected_laptop_quantity, user_quantity = valid2(laptop_dictionary, serial_no)
            #Valid Quantity

            #Update the text file   

            update2 (laptop_dictionary, serial_no, user_quantity)
            #Update the text file  

            #getting user purchased items
            product_name, unit_price, total_price, item_price, company_name = get2(laptop_dictionary, serial_no, user_quantity, purchased_laptops)

            user_request = more2()
            
            # Loop the code if the user inputs y
            if user_request =="Y":
                buy_more = True

            else:
                # Print bill if the user inputs any other value except y
                buy_more = False

                # print the bill in terminal
                printbuy(now, distributor_name, purchased_laptops)

                # Write the bill in a text file
                buybill(distributor_name, date_time, now, purchased_laptops)

    # If the user inputs '3' terminate the program
    elif user_input == 3:
        loop = False
        print ("Exit")


                

