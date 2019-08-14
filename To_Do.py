# ToDo List
# Dev:  Jill Thompson
# Date:  August 10, 2019
# Change log (who, what, when):
#   Jill Thompson, created, 8/10/2019

#Load data from file into dictionary
dictionary = {}
file = open("ToDo.txt", "r")
for line in file:
    x = line.split(",")
    task = x[0]
    y = x[1]
    priority = y[0:(len(y)-1)]  #Strip out the "\n" code imported for each line
    priority = priority.strip()
    dictionary[task] = priority

#Add dictionary items to a new list
list = []
list_item = dictionary.items()
for entry in list_item:
    list.append(entry)

#Display current list to user
print("This is your current to-do list: \n")
print("TO-DO / PRIORITY")
for entry in list:
    task, priority = entry
    print(task, "/", priority)

#Display menu of options to user
choice = None
while choice != "0":
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
    choice = input("Choice: ")

    #Display to-do list
    if choice == "1":
        print("This is your current to-do list: \n")
        print("TO-DO / PRIORITY")
        for entry in list:
            task, priority = entry
            print(task, "/", priority)

    #Add item
    elif choice == "2":
        task = input("Type the item you would like to add: \n")
        priority = input("Type the priority of the item:  \n")
        dictionary[task] = priority
        list = []
        list_item = dictionary.items()
        for entry in list_item:
            list.append(entry)

    #Delete item
    elif choice == "3":
        task = input("What term do you want to delete? \n")
        if task in dictionary:
            del dictionary[task]
            print("It has been deleted.")
            list = []
            list_item = dictionary.items()
            for entry in list_item:
                list.append(entry)
        else:
            print("That task is not on the list.")

    #Save to file
    elif choice == "4":
        confirm = input("Hit Y to save to file.")
        if confirm == "Y":
            objFile = open("New_ToDo.txt", "a")
            objFile.write(str(list))
            input("Data successfully saved to file.")
        else:
            print("File has not been saved. Please make another selection.")

    elif choice == "0":
        break

    #"Safety" for invalid user input
    else:
        print("Not a valid input. Please make another selection.")

if choice == "0":
    print("Good bye.")
    input()



