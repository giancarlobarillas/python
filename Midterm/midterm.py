#This program generates a monthly schedual for a loan
#It takes into account the loan amount, number of years and the annual interest rate
#The program displays the schedual in a table format
def main():
    #get inputs from the user
    loanAmount=int(input("Loan Amount:"))
    numberYears=int(input("Number of Years:"))
    annualInterestRate=int(input("Annual Interest Rate:"))
    
    #calulate total periods and montly interest rate for the PMT
    totalPeriods=numberYears*12
    decimalInterestRate=annualInterestRate*0.01
    interstRate=decimalInterestRate/12

    #calculate the montly payments and all data for the result
    monthlyPayments=calculateMonthlyPayments(loanAmount,interstRate,totalPeriods)
    resultTable=generateTable(loanAmount,monthlyPayments,interstRate,totalPeriods)

    #display result such as montly payments and the table
    displayPayments(monthlyPayments,loanAmount,resultTable)
    print("\nDisplaying ALL months of the schedual\n")
    displayData(resultTable,totalPeriods)
    print("\nDisplaying similar to the midterm example format\n")
    newDisplayData(resultTable,totalPeriods)


#display the monthly interest and total payment 
def displayPayments(payment,loan,table):
    print("Monthly Interest: "+'${:,.2f}'.format(payment))
    totalPayment=0
    for x in table:
        totalPayment+=x[0]
    totalPayment+=loan
    print("Total Payment: "+'${:,.2f}'.format(totalPayment))


 #display full table of all months   
def displayData(generatedTable,periods):
    print("Payments #\t"+"|{:<15}|{:^15}|{:>15}|".format('Interest','Principal','Balance'))
    for x in range(periods):
        outputString=str(x+1)+"\t\t"+"|{:<15}|{:^15}|{:>15}|".format('${:,.2f}'.format(generatedTable[x][0]),'${:,.2f}'.format(generatedTable[x][1]),'${:,.2f}'.format(abs(generatedTable[x][2])))
        print(outputString)

#display table in same format as midterm example
def newDisplayData(generatedTable,periods):
    print("Payments #\t"+"|{:<15}|{:^15}|{:>15}|".format('Interest','Principal','Balance'))
    displayArray=[0,1,'line',periods-2,periods-1]
    for x in displayArray:
        #'${:,.2f}'.format(generatedTable[x][0])
        if(x=='line'):
            print("...")
        else:
            outputString=str(x+1)+"\t\t"+"|{:<15}|{:^15}|{:>15}|".format('${:,.2f}'.format(generatedTable[x][0]),'${:,.2f}'.format(generatedTable[x][1]),'${:,.2f}'.format(abs(generatedTable[x][2])))
            print(outputString)

#generate all rows for the table for every month for the duration of the loan
def generateTable(startBalance,payments,interest,periods):
    result=[]
    balance=startBalance
    for x in range(periods):
        row=generateRow(balance,payments,interest)
        result.append(row)
        balance=row[2]
    return result
        
#generate a month row of monthly interest, principal, and balance
def generateRow(balance,montlyPaymenet,interest):
    result=[]
    rowInterest=montlyInterest(balance,interest)
    result.append(rowInterest)
    rowPrincipal=calculatePrincipal(montlyPaymenet,rowInterest)
    result.append(rowPrincipal)
    rowEndBalance=calculateEndingBalance(balance,rowPrincipal)
    result.append(rowEndBalance)
    return result

#calculate the montly payment for a specific month
def calculateMonthlyPayments(loan,interest,periods):
    part1=loan*interest
    part2=1-(1+interest)**-periods
    result=part1/part2
    return result

#calculate monthly interest for a specific month
def montlyInterest(balance,interest):
    result=balance*interest
    return result

#calculate principal of a specific month
def calculatePrincipal(monthPayment,interest):
    result=monthPayment-interest
    return result

#calculate a monthly balance
def calculateEndingBalance(balance,principal):
    result=balance-principal
    return result


main()
