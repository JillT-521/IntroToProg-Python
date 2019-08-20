# ToDo List
# Dev:  Jill Thompson
# Date:  August 19, 2019
# Change log (who, what, when):
#   Jill Thompson, created, 8/19/2019

# -- Data --#

dictionary = {}
list = []

# -- Input/Output --#

# User can see a menu
def display_menu():
    """Display menu of options to user"""
    print(
        """
        Please choose one of the following options:
    
        0 - Exit
        1 - Show current list
        2 - Add a new item to list
        3 - Delete item from list
        4 - Save list to file
        """
    )
    choice = str(input("Choice:"))
    return choice

# User can see data
def display_list():
    """Display current to-do list to user"""
    print("This is your current to-do list: \n")
    print("TO-DO / PRIORITY")
    for entry in list:
        task, priority = entry
        print(task, "/", priority)

# User can insert or delete data
class List_Item(object):

    def add_item(entry):
        """Add item to to-do list"""
        task = input("Type the item you would like to add: \n")
        priority = input("Type the priority of the item:  \n")
        global list
        list = []
        dictionary[task] = priority
        list_item = dictionary.items()
        for entry in list_item:
            list.append(entry)
        print(entry, "has been added to the list.")

    def delete_item(entry):
        """Delete item from to-do list"""
        task = input("What term do you want to delete? \n")
        if task in dictionary:
            del dictionary[task]
            print("It has been deleted.")
            global list
            list = []
            list_item = dictionary.items()
            for entry in list_item:
                list.append(entry)
        else:
            print("That task is not on the list.")


# User can save to file
def file_save():
    """Save current list to file"""
    confirm = input("Hit Y to save to file.")
    if confirm == "Y":
        objFile = open("New_ToDo.txt", "a")
        objFile.write(str(list))
        input("Data successfully saved to file.")
    else:
        print("File has not been saved. Please make another selection.")

# -- Processing --#

# When the program starts, load the data you have
# in a text file called ToDo.txt into a python List and Dictionary.

def create_dictionary():
    file = open("ToDo.txt", "r")
    for line in file:
        x = line.split(",")
        task = x[0]
        y = x[1]
        priority = y[0:(len(y) - 1)]  # Strip out the "\n" code imported for each line
        priority = priority.strip()
        dictionary[task] = priority


def create_list():
    list_item = dictionary.items()
    for entry in list_item:
        list.append(entry)


# Define the beginning of the program
def initiate():
    create_dictionary()
    create_list()
    display_list()


initiate()
choice = display_menu()
while choice != "0":
    if choice == "1":
        display_list()
    elif choice == "2":
        entry = List_Item
        entry.add_item(entry)
    elif choice == "3":
        entry = List_Item
        entry.delete_item(entry)
    elif choice == "4":
        file_save()
    elif choice == "0":
        break
    else:
        print("Not a valid input. Please make another selection.")
    choice = display_menu()

input("Press the enter key to exit.")
