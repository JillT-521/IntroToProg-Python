class Employee(object):

    def __init__(self, ID, firstName, lastName):
        self.ID = ID
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        string = "Employee ID: " + self.ID + "\nFirst Name: " + self.firstName + "\nLast Name:  " + self.lastName
        return string