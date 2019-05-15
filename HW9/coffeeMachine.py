# This program is for coffee machines, they have a default stock and default price
# A user is able to insert money into the machine and select a cup of coffee from the machine
# If the user does not have exact changes the machine will not give him a coffee cup
class coffeeMachine:
    def __init__(self, cupsAvailable, cost):  # Only the stock and price are default
        self.cupsAvailable = cupsAvailable
        self.cost = cost
        self.moneyInserted = 0
        self.quarters = 0
        self.dimes = 0
        self.nickles = 0

    def menu(self):  # displays a menu of the coffe machine
        output = (
            "The number of cups available are: "
            + str(self.cupsAvailable)
            + ".\nThe cost of 1 cup is: "
            + "${:,.2f}".format(self.cost)
        )
        return output

    def stockMachine(self, addedCoffee):  # This added more stock to the machine
        self.cupsAvailable = self.cupsAvailable + addedCoffee

    def insert(
        self, quarters, dimes, nickles
    ):  # this take in the number of coins input
        self.quarters = quarters
        self.dimes = dimes
        self.nickles = nickles
        value = quarters * 0.25 + dimes * 0.10 + nickles * 0.05
        self.moneyInserted = value

    def select(
        self
    ):  # This is only called when exact change is input and if the machine has stock
        if self.cupsAvailable == 0:
            print("Sorry we are out of stock")
        else:
            self.cupsAvailable = self.cupsAvailable - 1
            self.moneyInserted = 0

    def refund(self):  # refunds the amount input and reset the values to 0
        output = (
            "Returning: "
            + str(self.quarters)
            + " quarters, "
            + str(self.dimes)
            + " dimes, "
            + str(self.nickles)
            + " nickles"
        )
        self.moneyInserted = 0
        self.quarters = 0
        self.nickles = 0
        self.dimes = 0
        print(output)


def main():
    machine = coffeeMachine(0, 3.25)  # default machine
    print("Welcome to the coffee machines")
    print(
        "Our options today are: \nmenu, insert, select, refund, restock or exit(type the word to select option)"
    )
    # This while loop is for the user inputs so the user can order more than 1 coffee cup
    userinput = 1
    while userinput != 0:
        userinput = input("What would you like to do: ")
        if userinput == "menu":
            print(machine.menu())
        elif userinput == "insert":
            quarters = input("Please input the number of quarters: ")
            dimes = input("Please input the number of dimes: ")
            nickles = input("Please input the number of nickles: ")
            machine.insert(int(quarters), int(dimes), int(nickles))
            print("${:,.2f}".format(machine.moneyInserted))
        elif userinput == "select":
            if machine.moneyInserted == machine.cost:
                print("Here is your cup of coffee")
                machine.select()
                machine.quarters = 0
                machine.dimes = 0
                machine.nickles = 0
            else:
                print("Please input exact change, refunding your money")
                machine.refund()
        elif userinput == "restock":
            newStock = input("How many cups of coffee would you like to add: ")
            machine.stockMachine(int(newStock))
        elif userinput == "refund":
            machine.refund()
        elif userinput == "exit":
            userinput = 0
        else:
            print("Please input a proper input")


main()
