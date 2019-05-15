# This application allows someone to add new employees and view them
# The user can manage the employees attibutes
# This app create an employee superclass and that is inherited by productionWorker

# This is the employee class. This class manages the name and employee number of all workers
class Employee:
    def __init__(self, name, number):
        self.employeeName = name
        self.employeeNumber = number

    def displayName(self):
        print(self.employeeName)

    # mutator methods
    def changeName(self, newName):
        self.employeeName = newName

    def changeNumber(self, newEmployeeNumber):
        self.employeeNumber = newEmployeeNumber


# This is the productionWorker subclass, it deals with rates and shifts
class ProductionWorker(Employee):
    def __init__(self, name, number, shift, rate):
        super().__init__(name, number)
        self.employeeShift = shift
        self.employeeRate = rate

    # Mutator methods
    def changeShift(self, newShift):
        self.employeeShift = newShift

    def changeRate(self, newRate):
        self.employeeRate = newRate

    def displayAllInfo(self):
        print(
            "Name: "
            + self.employeeName
            + "\tEmployee Number: "
            + str(self.employeeNumber)
            + "\tEmployee Shift: "
            + str(self.employeeShift)
            + "\tEmployee Rate: "
            + "${:,.2f}".format(self.employeeRate)
        )


def main():
    # default data
    data = []
    userInput = 1

    print("Welcome to our employee registry")
    print("What would you like to do?")
    print(
        "In this application you can add employees, veiw employees and modify employees"
    )
    while userInput != "exit":
        userInput = input("Type add, view, modify, or exit: ")
        if userInput == "add":
            userName = input("What is the employee's name: ")
            userNumber = input("What is the employee's number: ")
            userShift = input("What is the employee's shift: ")
            userRate = input("What is the employee's rate: ")
            # try to verify that usershift is a int
            try:
                test = int(userShift)
            except ValueError:
                print("please enter an integer for the employee shift")
                userShift = input("What is the employee's shift: ")
            x = ProductionWorker(userName, userNumber, int(userShift), float(userRate))
            data.append(x)
        elif userInput == "view":
            for x in data:
                x.displayAllInfo()
                # print(x.employeeName)
        elif userInput == "modify":
            # default check
            if data == []:
                print("Please add a employee first before modifing")
            else:
                searchEmployee = input("What is the name of the employee: ")
                # look through the data and find the employee
                for y in data:
                    if y.employeeName == searchEmployee:
                        print("Employee Was found")
                        options = input(
                            "What would you like to modify(type name, number, shift or rate): "
                        )
                        if options == "name":
                            newName = input("What is the employee's new name: ")
                            y.changeName(newName)
                        elif options == "number":
                            newNumber = input("What is the employee's new number: ")
                            y.changeNumber(newNumber)
                        elif options == "shift":
                            newShift = input("What is the employee's new shift: ")
                            y.changeShift(newShift)
                        elif options == "rate":
                            newRate = input("What is the employee's new hourly rate: ")
                            y.changeRate(newRate)
                        else:
                            print(
                                "Please type a proper field to change. Returning you back to menu"
                            )
                        break
                    else:
                        print("Employee Not found")
        elif userInput == "exit":
            continue
        else:
            print("Invalid Input")
            print("Please ype add, view, modify, or exit")


main()
