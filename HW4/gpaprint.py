import csv

def main():
    data = []
    courseCode = []
    courseCredit = []
    courseGrade = []
    with open("dataIO.txt") as f:
        reader = csv.reader(f,delimiter=",")
        for row in reader:
            data.append(row)
            courseCode.append(row[2])
            courseCredit.append(row[3])
            courseGrade.append(row[4])
    length=len(data)
    counter = 0
    #student1
    courseCodeGroup=[]
    courseCreditGroup = []
    courseGradeGroup=[]
    # student2
    courseCodeGroup2 = []
    courseCreditGroup2 = []
    courseGradeGroup2 = []
    # student3
    courseCodeGroup3 = []
    courseCreditGroup3 = []
    courseGradeGroup3 = []
    for row in data:
        if(counter<3):
            courseCodeGroup.append(courseCode[counter])
            courseCreditGroup.append(courseCredit[counter])
            courseGradeGroup.append(courseGrade[counter])
        elif(counter<7):
            courseCodeGroup2.append(courseCode[counter])
            courseCreditGroup2.append(courseCredit[counter])
            courseGradeGroup2.append(courseGrade[counter])
        else:
            courseCodeGroup3.append(courseCode[counter])
            courseCreditGroup3.append(courseCredit[counter])
            courseGradeGroup3.append(courseGrade[counter])

        counter=counter+1

    printReport("BOKOW, R.", "2333021", courseCodeGroup, courseCreditGroup, courseGradeGroup)
    printReport("FALLIN, D.", "2574063", courseCodeGroup2, courseCreditGroup2, courseGradeGroup2)
    printReport("KINGSLEY, M.", "2663628", courseCodeGroup3, courseCreditGroup3, courseGradeGroup3)


def getGradeNumber(grade,strCredit):
    credit=int(strCredit)
    if grade=='A':
        return 4*credit
    elif grade=='B':
        return 3*credit
    elif grade == 'C':
        return 2*credit
    elif grade == 'D':
        return 1*credit
    else:
        return 0

def printReport(name,id,courseArray,creditArray,gradeArray):
    report = open(name+".txt", "w")
    report.write("Student Name:" + name+"\n")
    report.write("Student ID Number: "+id+"\n")
    report.write("Course Code \t Course Credits \t Course Grade\n")
    counter=0
    creditArrayINT=[]
    gradeArrayINT=[]
    for x in courseArray:
        report.write(x+" \t\t\t "+creditArray[counter]+" \t\t\t\t\t "+gradeArray[counter]+"\n")
        creditArrayINT.append(int(creditArray[counter]))
        gradeArrayINT.append(getGradeNumber(gradeArray[counter],creditArray[counter]))
        counter=counter+1
    #print("Total Semester course credits completed: "+str(sum(creditArrayINT)))
    gpa=str(round(sum(gradeArrayINT)/sum(creditArrayINT),1))
    report.write("Total Semester Course Credits Compled: "+ str(sum(creditArrayINT))+"\n")
    report.write("Semester GPA:"+ gpa+"\n")

main()
