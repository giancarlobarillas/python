# This application calculates the number of coins in a gui interface and tells the user how much it is worth
# this applications starts by taking inputs from the user and then convert that input into money values.
# Then is sums up all the values and outputs a final value.
import tkinter as tk
from re import sub
from decimal import Decimal


# create instance
win = tk.Tk()
# add title
win.title("Change Calculator")
# add array of types of coins to generate all rows
typesofCoins = ["dollars", "halfdollars", "Quarters", "Dimes", "Nickles", "Pennies"]
# arrayfor all inputs so that the inputs are recorded to be calculated
arrayOfInputs = []

# This for loop goes through the array of coins and generates each row it.
# it creates the 3 columsn of types of coin, the entry and the value label
for index, item in enumerate(typesofCoins):
    tk.Label(win, text=item).grid(column=0, row=index, sticky="E")
    MoneyEntry = tk.Entry(win)
    arrayOfInputs.append(MoneyEntry)
    MoneyEntry.grid(column=1, row=index)
    tk.Label(win, text=item + " Value:").grid(column=2, row=index, sticky="E")

# this function gets all the entry fields and the call get value to output the value of the input and the final price
def getCoins():
    getAllValues = []
    for index, item in enumerate(arrayOfInputs):
        text = item.get()
        values = getValue(text, index)
        getAllValues.append(values)
        label2 = tk.Label(win, text=values)
        label2.grid(column=4, row=index)
    # The final price is calculated by accessing the array of outputs and added the decimal value.
    # The program convert the value back to decimals
    # and once the final calculation is done then it reformats it back to money
    finalPrice = 0
    for val in getAllValues:
        convert = Decimal(sub(r"[^\d.]", "", val))
        finalPrice = finalPrice + convert
    finalLabel = tk.Label(win, text="${:,.2f}".format(finalPrice))
    finalLabel.grid(column=3, row=7, columnspan=2, sticky="WE")


# This function takes in the index and the value of the entry, it calculates the coin value
def getValue(value, index):
    stringOutput = ""
    inputValue = value
    if inputValue == "":
        inputValue = 0
    else:
        inputValue = value
    if index == 0:
        stringOutput = "${:,.2f}".format(float(inputValue))
    elif index == 1:
        halfDollarValue = float(inputValue) / 2
        stringOutput = "${:,.2f}".format(halfDollarValue)
    elif index == 2:
        quarterValue = float(inputValue) / 4
        stringOutput = "${:,.2f}".format(quarterValue)
    elif index == 3:
        dimeValue = float(inputValue) / 10
        stringOutput = "${:,.2f}".format(dimeValue)
    elif index == 4:
        nickleValue = float(inputValue) / 20
        stringOutput = "${:,.2f}".format(nickleValue)
    elif index == 5:
        pennyValue = float(inputValue) / 100
        stringOutput = "${:,.2f}".format(pennyValue)
    return stringOutput


# adding a button
action = tk.Button(win, text="Compute!", command=getCoins)
action.grid(column=0, row=7, columnspan=2, sticky="WE")
# start GUI
win.mainloop()
