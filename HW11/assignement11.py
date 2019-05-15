# this application allows you to create a list of ships
# It will ask you what type of ship you want to input and capture that
# information. It will then display it when you are finished
# This app will also determine what type of object it is

# This is the ship object with just the name and year
class Ship:
    def __init__(self, shipName, buildYear):
        self.shipName = shipName
        self.buildYear = buildYear

    def showShip(self):
        print("This is a", self.shipName)
        print("It was made in", self.buildYear)


# This is the cruise object and inherit ship and overrides showship
class CruiseShip(Ship):
    def __init__(self, shipName, buildYear, numberOfPassangers):
        super().__init__(shipName, buildYear)
        self.numberOfPassangers = numberOfPassangers

    def showShip(self):
        print("This is a", self.shipName)
        print("The number of passangers on this ship is:", self.numberOfPassangers)


# This is the Cargo object and inherit ship and overrides showship
class CargoShip(Ship):
    def __init__(self, shipName, buildYear, cargoCapacity):
        super().__init__(shipName, buildYear)
        self.cargoCapacity = cargoCapacity

    def showShip(self):
        print("This is a", self.shipName)
        print("The ships capacity is:", self.cargoCapacity)


# This function generates the list of boats by calling addBoat
def generateBoatList():
    print("Welcome to the boat generator")
    list = []
    userInput = ""
    while userInput != "exit":
        userInput = input(
            "Would you like to add a new boat or exit(type add or exit): "
        )
        if userInput == "add":
            addBoat(list)
        elif userInput == "exit":
            print("Exiting")
        else:
            print("Please type add or exit")
    return list


# Addboat adds the type of boat you want to input and returns that
# list of boats. Its argument is the default list
# It will allow you to create 1 of 3 ships
def addBoat(list):
    print("Our boat option are: Ship, Cruise, and Cargo")
    boatInput = input("What type of boat would you like to add: ")
    if boatInput == "Ship":
        boatName = input("What is the name of the boat:  ")
        boatYear = input("What year was your boat made: ")
        try:
            test = int(boatYear)
        except ValueError:
            print("please enter an integer for the boat year: ")
            boatYear = input("What year was your boat made: ")
        ship = Ship(boatName, boatYear)
    elif boatInput == "Cruise":
        boatName = input("What is the name of the boat:  ")
        boatYear = input("What year was your boat made: ")
        try:
            test = int(boatYear)
        except ValueError:
            print("please enter an integer for the boat year: ")
            boatYear = input("What year was your boat made: ")
        boatMax = input("What is the boats maximum number of passangers: ")
        try:
            test = int(boatMax)
        except ValueError:
            print("please enter an integer for the boat max load: ")
            boatMax = input("What is the boats maximum number of passangers: ")
        ship = CruiseShip(boatName, boatYear, boatMax)
    elif boatInput == "Cargo":
        boatName = input("What is the name of the boat:  ")
        boatYear = input("What year was your boat made: ")
        try:
            test = int(boatYear)
        except ValueError:
            print("please enter an integer for the boat year: ")
            boatYear = input("What year was your boat made: ")
        boatCargo = input("What is the boats capacity: ")
        try:
            test = int(boatCargo)
        except ValueError:
            print("please enter an integer for the boat max load: ")
            boatCargo = input("What is the boats capacity: ")
        ship = CargoShip(boatName, boatYear, boatCargo)
    else:
        print("Please type one of the following next time: Ship, Cruise or Cargo")

    list.append(ship)


# This determines what type of ship you created without
# explicitly knowing beforehand
def getType(shipObject):
    if isinstance(shipObject, CruiseShip):
        print("This boat is a Cruise")
    elif isinstance(shipObject, CargoShip):
        print("This boat is a Cargo")
    elif isinstance(shipObject, Ship):
        print("This boat is a Ship")
    else:
        print("This is not a boat")


# main function only deal with generating the list of boats and
# displaying the information
def main():
    listOfBoats = generateBoatList()
    # print(len(listOfBoats))
    print()
    print("DISPLAYING DATA")
    if listOfBoats == []:
        print("No Data inputed")
    else:
        for a in listOfBoats:
            getType(a)
            a.showShip()


main()
