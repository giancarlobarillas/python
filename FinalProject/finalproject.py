# This application has 3 classes, Patient,Surgery, and Pharmancy
# The purpose of this application is to calculate the total bill for a person in a hospital
# This application starts by created a patientAccount that takes into account days stayed and daily Charge
# It will then prompt you to do add a surgery, add a medication, or exit which will display the final bill

# The Patient Account deals with the default patient information and displays the bill info
class PatientAccount:
    def __init__(self, days, dailyCharge):
        self.days = days
        self.dailyCharge = dailyCharge
        self.patientCharges = self.days * self.dailyCharge

    def updateCharges(self, value):
        self.patientCharges = float(self.patientCharges) + float(value)

    def displayInfo(self):
        print("This person stayed " + str(self.days) + " days")
        print("The total Charges are " + "${:,.2f}".format(self.patientCharges))


# Surgery has a dictionary of 5 surgeries. It can display the options and get the cost
class Surgery:
    def __init__(self):
        self.SurgeryData = {
            "Appendectomy": 33000,
            "Breast biopsy": 500,
            "Back Surgery": 14000,
            "Cataract": 3429,
            "Cesarean section": 5000,
        }

    def displayOptions(self):
        for name in self.SurgeryData:
            print(name)

    # This checks if the Surgery is offered and displays the corresponding cost and add it to the bill
    def displayCost(self, SurgeryName, patient):
        if SurgeryName in self.SurgeryData:
            print(
                "The cost of that is", "${:,.2f}".format(self.SurgeryData[SurgeryName])
            )
            patient.updateCharges(self.SurgeryData[SurgeryName])
        else:
            print("Surgery not supported. Please try again.")


# Pharmacy class has 5 medications. It can display the options and get the cost
class Pharmacy:
    def __init__(self):
        self.MedicationData = {
            "Vicodin": 273,
            "Simvastatin": 126.64,
            "Lisinopril": 21.59,
            "Levothyroxine": 38.07,
            "Azithromycin": 37.22,
        }

    def displayOptions(self):
        for name in self.MedicationData:
            print(name)

    # This checks if the medication is offered and displays the corresponding cost and add it to the bill
    def displayCost(self, MedicineName, patient):
        if MedicineName in self.MedicationData:
            print(
                "The cost of that is",
                "${:,.2f}".format(self.MedicationData[MedicineName]),
            )
            patient.updateCharges(self.MedicationData[MedicineName])
        else:
            print("This pharamacy does not have this medication. Please try again.")


# This generates the menu. It takes the default information and uses it to get the final bill
def generateMenu(defaultDaysStayped, defaultDailyRate):
    CreatedPatient = PatientAccount(defaultDaysStayped, defaultDailyRate)
    menuInput = 0
    while menuInput != "exit":
        print("Here are our options: Add Surgery, Add medication, View Bill")
        print("Please type Surgery, Medication, Bill, or exit")
        menuInput = input("What would you like to do? ")
        if menuInput == "Surgery":
            AddingSurgery = Surgery()
            print("Here are our options: ")
            AddingSurgery.displayOptions()
            surguryAdded = input("What surgery would you like to add: ")
            AddingSurgery.displayCost(surguryAdded, CreatedPatient)
        elif menuInput == "Medication":
            AddingMedication = Pharmacy()
            print("Here are our options: ")
            AddingMedication.displayOptions()
            medicationAdded = input("What medication would would you like to add: ")
            AddingMedication.displayCost(medicationAdded, CreatedPatient)
        elif menuInput == "Bill":
            CreatedPatient.displayInfo()
        elif menuInput == "exit":
            print("Here is your final Bill.")
            CreatedPatient.displayInfo()
        else:
            print("Please input a proper input")


def main():
    print("Welcome to patient Calculator")
    print("Before we begin let us get some default information")
    DaysStayed = int(input("How long did the patient Stay: "))
    DailyRate = int(input("What is the daily rate: "))
    generateMenu(DaysStayed, DailyRate)


main()
