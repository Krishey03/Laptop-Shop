# Displays the data from the dictionary in the terminal
def dictionary(laptop_dictionary): 
    file = open("Items.txt", "w")
    for values in laptop_dictionary.values():
        file.write(str(values[0]) +"," +str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")
    file.close()

#SELL BILL (WRITE)
def sellbill(user_name, date_time, now, phone_number, user_address, purchased_laptops, shipping_cost, sum_total):
    filename = f"{user_name} {date_time}.txt"
    file = open(filename, "w")
    file.write("\t\t\t\t\t\tKrish's Laptop Shop")
    file.write("\n")
    file.write("\t\t\t\tBafal, Kathmandu | Phone No: 000000000000")
    file.write("\n")
    file.write("\t\t\t\t\t Sales invoice")
    file.write("\n")
    file.write("Date/Time"+str(now),)
    file.write("\n")
    file.write("Customer Name: "+str(user_name))
    file.write("\n")
    file.write("Customer Phone No: "+str(phone_number))
    file.write("\n")
    file.write("Customer address: "+str(user_address))
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------------" "\n")
    file.write("Laptop Name| \t\t |Company Name \t\t |Quantity \t\t |Price \t\t\t " " |Total| " "\n")
    file.write("---------------------------------------------------------------------------------------------------" "\n")
    for i in purchased_laptops:
        file.write (str(i[0])+"\t     " +str(i[1])+ " \t\t    "+"     "+str(i[2])+ "\t      "+str(i[3]) + "\t\t\t     " + "$"+ str(i[4]) + "\n")
    file.write("---------------------------------------------------------------------------------------------------" "\n")
    file.write("\n")
    file.write("Shipping Cost: "+ str(shipping_cost))
    file.write("\n")
    file.write("Sum Total: $"+str(sum_total))
    file.write("\n")

    


#PURCHASE BILL (WRITE)
def buybill(distributor_name, date_time, now, purchased_laptops):
    total = 0
    for i in purchased_laptops:
        total+=int(i[4])
    sum_total = total
    vat = sum_total * (13/100)
    vat_amt = sum_total + vat
    filename = f"{distributor_name} {date_time}.txt"
    file = open(filename, "w")
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write("\t\t\t\t\t\t" " " "Date/Time"+str(now),)
    file.write("\n")
    file.write("\t\t\t\t\t\t Sasto Laptops | Phone No: 9999999999")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t Sales Receipt")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("\n")
    file.write("Distributor Name: " + str(distributor_name))
    file.write("\n")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("Laptop Name| \t\t |Company Name \t\t |Quantity \t\t |Price \t\t |Total| ")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------" "\n")
    for i in purchased_laptops:
        file.write (str(i[0])+"\t     " " "+str(i[1])+ " \t\t    " +"     "+str(i[2])+ "\t\t      "+str(i[3]) + "\t      "+"$"+str(i[4]) + "\n")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("\n")
    file.write("Sum Total: $"+str(sum_total))
    file.write("\n")
    file.write("VAT amount: "+str(vat))
    file.write("\n")
    file.write("Total Amount with VAT: "+str(vat_amt))
    

#SELL BILL
def printsell(now, user_name, phone_number, user_address, shipping_cost, sum_total, purchased_laptops):
    print("\n")
    print("\t\t\t\t\t\tKrish's Laptop Shop")
    print("\n")
    print("\t\t\t\tBafal, Kathmandu | Phone No: 000000000000")
    print("\n")
    print("\t\t\t\t\t Sales invoice")
    print("\n")
    print("Date|Time: "+str(now),)
    print("Customer Name: "+str(user_name))
    print("Customer Phone No: "+str(phone_number))
    print("Customer Address: "+str(user_address))
    print("\n")
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    print("Laptop Name| \t\t\t |Company Name \t\t\t |Quantity \t\t |Price \t\t\t |Total| ")
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    for i in purchased_laptops:
        print (i[0], "\t\t\t", i[1], "\t\t\t", "     ", i[2], "\t\t", i[3],  "\t\t\t", "$",i[4], "\n")#, i[4], "\t\t\t", i[5])
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    print("Shipping Cost: "+ str(shipping_cost))
    print("Sum Total: $"+str(sum_total))
    print("\n")
    print("\n")
    print("\n")


#PURCHASE BILL
def printbuy(now, distributor_name, purchased_laptops):
    total = 0
    for i in purchased_laptops:
        total+=int(i[4])
    sum_total = total
    vat = sum_total * (13/100)
    vat_amt = sum_total + vat
    print("\n")
    print("\t\t\t\t\t\tSasto Laptop Store")
    print("\n")
    print("\t\t\t\tHattiban, Lalitpur | Phone No: 9999999999")
    print("\n")
    print("\t\t\t\t\t Sales Receipt")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("Print Date|Time: "+str(now),)
    print("\n")
    print("Customer Name: "+str(distributor_name))
    print("\n")
    print("Purchased products: ")
    print("\n")
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print("Laptop Name| \t\t\t |Company Name \t\t\t "   " |Quantity \t\t |Price \t\t\t |Total| ")
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    for i in purchased_laptops:
        print (i[0], "\t\t\t", i[1], "\t\t\t","     ", i[2], "\t\t", i[3], "\t\t\t", "$",i[4], "\n")#, i[4], "\t\t\t", i[5])
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("Sum Total: $"+str(sum_total))
    print("\n")
    print("VAT amount: "+str(vat))
    print("\n")
    print("Total amount with VAT Amount: "+str(vat_amt))
    print("\n")


                           
