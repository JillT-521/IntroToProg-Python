# Title: Pickling and Exception Handling
# Dev: Jill Thompson
# Created: August 25, 2019
# Change log (who, what, when):
#   JThompson, created, 8/25/19

import pickle

#Create file and lists
mystery_file = open("mystery.dat", "wb")
detectives = ["Sherlock Holmes", "Dirk Gently", "Precious Ramotswe"]
authors = ["Sir Arthur Conan Doyle", "Douglas Adams", "Alexander McCall Smith"]
books = ["A Study in Scarlet", "The Long Dark Tea Time of the Soul", "Blue Shoes and Happiness"]

#Pickle lists
pickle.dump(detectives, mystery_file)
pickle.dump(authors, mystery_file)
pickle.dump(books, mystery_file)

#Unpickle lists and print for user
mystery_file = open("mystery.dat", "ab+")
print("Here are the contents of the mystery file:\n")
detectives = pickle.load(mystery_file)
authors = pickle.load(mystery_file)
books = pickle.load(mystery_file)
print("Detectives:", detectives, "\n", "Authors:", authors, "\n", "Books:", books, "\n")

#Ask user for new inputs
type = None
while type != 0:
    try:
        type = int(input("What would you like to add? Choose detective(1), author(2), book(3), or exit(0)\n"))
        if type == 1:
            addition = input("Please input your new addition.\n")
            detectives.append(addition)
        elif type == 2:
            addition = input("Please input your new addition.\n")
            authors.append(addition)
        elif type == 3:
            addition = input("Please input your new addition.\n")
            books.append(addition)
        elif type == 0:
            input("Hit enter to save and view your new list.")
        else:
            print("That is not a valid choice. Please choose a number between 0 and 3.")
    except(ValueError):
        print("That's not an acceptable input. Input must be number, not text.")

#Pickle new lists
pickle.dump(detectives, mystery_file)
pickle.dump(authors, mystery_file)
pickle.dump(books, mystery_file)

#Display new lists
mystery_file = open("mystery.dat", "rb")
pickle.load(mystery_file)
pickle.load(mystery_file)
pickle.load(mystery_file)
print("Here are the new contents of the mystery file:\n")
print(detectives, "\n", authors, "\n", books, "\n")
mystery_file.close()
input("Hit enter to close program.")

