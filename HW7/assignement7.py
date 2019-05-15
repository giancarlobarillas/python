#This program takes in a phone number that can be either a number or a capital letter and covert it to a digital phone number
def main():
    result=[]
    inputNumber=input("What is the phone number you want to enter(XXX-XXX-XXXX): ")
    if(len(inputNumber)!=12):
        print("You number needs to be in the format of XXX-XXX-XXXX")
    else:
        for x in inputNumber:
            if(x=='-'):
                result.append(getNumber(x))
            else:
                try:
                    val=int(x)
                    result.append(str(val))
                except ValueError:
                    val=x.upper()
                    result.append(getNumber(val))
    print("".join(result))

#get the number from a given letter or number
def getNumber(x):
    if(x=='A' or x=='B' or x=='C' or x=='2'):
        return('2')
    elif(x=='D' or x=='E' or x=='F' or x=='3'):
        return('3')
    elif(x=='G' or x=='H' or x=='I' or x=='4'):
        return('4')
    elif(x=='J' or x=='K' or x=='L' or x=='5'):
        return('5')
    elif(x=='M' or x=='N' or x=='O' or x=='6'):
        return('6')
    elif(x=='P' or x=='Q' or x=='R' or x=='7'):
        return('7')
    elif(x=='T' or x=='U' or x=='V' or x=='8'):
        return('8')
    elif(x=='W' or x=='X' or x=='Y' or x=='Z' or x=='9'):
        return('9')
    else:
        return(x)

main()
