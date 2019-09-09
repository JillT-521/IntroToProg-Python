# Employee Data List
# Takes user input and saves to text file
# Dev:  Jill Thompson
# Date: September 8, 2019
# Change log (who, what, when):
#   JThompson, created, 9/08/19

#Data
list = []
empFile = None

#User Input

#Define class of objects

class Employee(object):

    def __init__(self, ID, firstName, lastName):
        self.ID = ID
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        rep = "A new employee has been added."
        rep += "\nEmployee ID: " + self.ID + "\nFirst Name: " + self.firstName + "\nLast Name:  " + \
               self.lastName
        return rep

# Save user input to file

def WriteUserInput():
    empFile = open("EmployeeData.txt", "a")
    empFile.write(str(list))

#main
def main():
    choice = input("Would you like to add a new employee? Enter Y for yes or N for no. ")
    while choice == "Y":
        new_employee = Employee(input("Please enter ID number: "), input("Please enter first name: "), input("Please enter last name: "))
        print(new_employee)
        list.append((new_employee.ID, new_employee.firstName, new_employee.lastName))
        choice = input("Would you like to add a new employee? Enter Y for yes or N to save and exit.")

#Run program
main()
import ReadData
WriteUserInput()
print("Data has been saved. Here are the contents of the file:")
ReadData.ReadAllFileData()
input("Good bye.")

