# Reading from text file and storing the data in dictionary
def laptops():
    file = open ("Items.txt", "r")
    laptop_dictionary ={}
    laptop_id = 1
    for line in file:
        line = line.replace("\n", "")
        laptop_dictionary.update({laptop_id: line.split(",")})
        laptop_id = laptop_id + 1
    file.close

    return laptop_dictionary

#Reads every line and shows the data in terminal
def items():
    file = open("Items.txt", "r")
    a = 1 #serial no
    for line in file:
        print(a, "\t\t"+line.replace(",","\t\t"))
        a = a+1 #Serial Number
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    file.close()

    
