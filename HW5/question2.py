#this program multiplies two matrixes
def main():
    strFirstMatrix=input("Enter matrix1: ")
    strSecondMatrix=input("Enter matrix2: ")
    FirstMatrix=getArrayOfNumbers(strFirstMatrix)
    SecondMatrix=getArrayOfNumbers(strSecondMatrix)
    matrix1Length=len(FirstMatrix)
    matrix2Length=len(SecondMatrix)
    formatM1=formatMatrix(FirstMatrix)
    formatM2=formatMatrix(SecondMatrix)
    if(matrix1Length==9 and matrix2Length==9):
        print("The multiplcation of the matrix is: ")
        cMatrix=multMatrix(formatM1,formatM2)
        displayMatrix(FirstMatrix,SecondMatrix,cMatrix)
    else:
        print("Please input a 3 * 3 matrix")

'''
#brute force method
def multiplyMatrix(a,b):
    resultMatrix=[]
    c11=a[0]*b[0]+a[1]*b[3]+a[2]*b[6]
    c12=a[0]*b[1]+a[1]*b[4]+a[2]*b[7]
    c13=a[0]*b[2]+a[1]*b[5]+a[2]*b[8]
    c21=a[3]*b[0]+a[4]*b[3]+a[5]*b[6]
    c22=a[3]*b[1]+a[4]*b[4]+a[5]*b[7]
    c23=a[3]*b[2]+a[4]*b[5]+a[5]*b[8]
    c31=a[6]*b[0]+a[7]*b[3]+a[8]*b[6]
    c32=a[6]*b[1]+a[7]*b[4]+a[8]*b[7]
    c33=a[6]*b[2]+a[7]*b[5]+a[8]*b[8]
    resultMatrix.append(c11)
    resultMatrix.append(c12)
    resultMatrix.append(c13)
    resultMatrix.append(c21)
    resultMatrix.append(c22)
    resultMatrix.append(c23)
    resultMatrix.append(c31)
    resultMatrix.append(c32)
    resultMatrix.append(c33)
    #print("%0.1f" % (resultMatrix[5],))
    return resultMatrix

'''

#multply matrix given two formated matrixes
def multMatrix(a,b):
    resultMatrix=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                resultMatrix[i][j] += a[i][k] * b[k][j]
    return resultMatrix

#format matrix to usable multiplcations
def formatMatrix(a):
    newMatrix=[[a[0],a[1],a[2]],[a[3],a[4],a[5]],[a[6],a[7],a[8]]]
    return newMatrix


#display matrix in the given format
def displayMatrix(a,b,c):
    print(str(a[0])+" "+str(a[1])+" "+str(a[2])+
    "\t"+str(b[0])+" "+str(b[1])+" "+str(b[2])+
    "\t"+"%0.1f" % (c[0][0],)+" "+"%0.1f" % (c[0][1],)+" "+"%0.1f" % (c[0][2],))

    print(str(a[3])+" "+str(a[4])+" "+str(a[5])+
    "  *  "+str(b[3])+" "+str(b[4])+" "+str(b[5])+
    "  =  "+"%0.1f" % (c[1][0],)+" "+"%0.1f" % (c[1][1],)+" "+"%0.1f" % (c[1][2],))

    print(str(a[6])+" "+str(a[7])+" "+str(a[8])+
    "\t"+str(b[6])+" "+str(b[7])+" "+str(b[8])+
    "\t"+"%0.1f" % (c[2][0],)+" "+"%0.1f" % (c[2][1],)+" "+"%0.1f" % (c[2][2],))


#convert the string into a array
def getArrayOfNumbers(stringList):
    strlist=stringList.split(" ")
    removedList=filter(None,strlist) #remove all spaces
    list=[float(x) for x in removedList]
    return list

main()
