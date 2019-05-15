import matplotlib.pyplot as plt
import csv
#This program displays a pie chart from a given text file where the
#label and amount is on.
def main():
    #create arrays for both labels and values
    pieLabels=[]
    pieValues=[]
    #read Text file
    with open("expenses.txt") as f:
        reader = csv.reader(f,delimiter=",")
        for row in reader:
            pieLabels.append(row[0])
            pieValues.append(row[1])
    f.close()
    #diplay pie chart with proper labels and values and title
    plt.pie(pieValues,labels=pieLabels)
    plt.title('Monthly Expenses')
    plt.show()

main()
