#Title:  Product List
#Dev: RRoot
#Date: September 2, 2019
#Change Log (who, what, when):
#   RRoot, created, unknown
#   JThompson, modified, 9/2/2019


#Data
objFile = None #File Handle
strUserInput = None #A string which holds user input
list = [] #Create list to capture user input

#User Input
#Define class of objects

class Product(object):

    def __init__(self, ID, name, price):
        self.ID = ID
        self.name = name
        self.price = price

    def __str__(self):
        rep = "A new item has been created.\n"
        rep += "ID: " + self.ID + "\nName: " + self.name + "\nPrice:  " + self.price
        return rep

#Processing
#Read data from and write data to file

def WriteProductUserInput():
    objFile = open("Products.txt", "a")
    objFile.write(str(list))

def ReadAllFileData():
    try:
        objfile = open("Products.txt", "r")
        for item in objfile:
            print(item)
    except IOError:
        print("Something went wrong. The file you are trying to access does not exist.")

#main
def main():
    choice = input("Would you like to add a product? Enter Y for yes or N for no.")
    while choice == "Y":
        new_product = Product((input("Please enter ID number: ")),
        (input("Please enter name: ")), (input("Please enter price: ")))
        print(new_product)
        list.append((new_product.ID, new_product.name, new_product.price))
        choice = input("Would you like to add a product? Enter Y for yes or N to save and exit.")

#Run program
main()
WriteProductUserInput()
print("Data has been saved. Here are the contents of the file:")
ReadAllFileData()
input("Good bye.")

