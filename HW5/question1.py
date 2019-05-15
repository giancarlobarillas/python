#this function verifies if a string of values is sorted
def main():
    userInputList=input("Please enter your list.(Have a space in between each value)")
    isSorted(getArrayOfNumbers(userInputList))

#convert string onto a array
def getArrayOfNumbers(stringList):
    strlist=stringList.split(" ")
    removedList=filter(None,strlist) #remove all spaces
    list=[float(x) for x in removedList]
    return list

#verify if the list is sorted
def isSorted(lst):
    flag=0#flag to confirm if list is sorted
    i=1
    while i < len(lst):
        if(lst[i]<lst[i-1]):
            flag=1
        i+=1
    if(flag):
        print("The list is not sorted")
    else:
        print("The list is already sorted")

main()
