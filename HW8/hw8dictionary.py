# This application create a dictionary of emails and name
# It has a menu that allows users to add,delete,and search names to find emails
# Once the user exits it will save the data into a file.
# This app starts with a user input for the menu options then goes thouogh with the features discussed
import csv

# Main function starts the menu and then uses another function to interpret the input
def main():
    userInput = ""
    data = {}
    while userInput != "exit":
        userInput = input(
            """What would you like to do:
        Search
        add email(Type add)
        update email(type update)
        delete email(type delete)
        exit\n"""
        )
        validateInput(userInput, data)


# This function takes the user input from the menu and calls the correstponding function for each feature
def validateInput(userString, data):
    if userString.lower() == "search":
        print("Search for a user by name")
        inputName = input("What is the name you want to find: ")
        print(searchName(data, inputName))
    elif userString.lower() == "add":
        print("Adding a new email and name")
        name = input("What is the name you want to input: ")
        email = input("What is the email you want: ")
        addEmail(data, name, email)
        print(data)
    elif userString.lower() == "update":
        print("Updating a existing email")
        updateName = input("What is the name you want to update: ")
        updateEmail(data, updateName)
    elif userString.lower() == "delete":
        print("delete record")
        deleteName = input("What is the name of the person you want to delete: ")
        deleteRecord(data, deleteName)
    elif userString.lower() == "exit":
        print("Exiting Application")
        w = csv.writer(open("dataSave.csv", "w"))
        for key, val in data.items():
            w.writerow([key, val])
    else:
        print("Please type a proper input")


# Adds an email to the dictionary
def addEmail(data, name, email):
    data[name] = email


# checks and updates an email in the dictionary
def updateEmail(data, name):
    if name in data.keys():
        newEmail = input("What is the new email:")
        data[name] = newEmail
        print("Email was updated")
    else:
        print("There is no such name in the data")


# deletes a record from the dictionary
def deleteRecord(data, name):
    if name in data.keys():
        data.pop(name)
        print("record was deleted")
    else:
        print("There is no such name in the data")


# search for a name in the dictionary
def searchName(data, name):
    if data:
        if name in data.keys():
            return data[name]
        else:
            return "There is no email for that name"
    else:
        return "No data has been input. Please add a email first."


main()
