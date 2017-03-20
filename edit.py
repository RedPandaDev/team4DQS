import csv


def listReader(tuteeFile,tutorFile):
    with open(tuteeFile) as csvfile:   #read list of tutees
        tutees = csv.reader(csvfile) 
        csvfile.readline()
        tuteeList = list(tutees)

    with open(tutorFile) as csvfile:   #read list of tutors
        tutors = csv.reader(csvfile) 
        csvfile.readline()
        tutorList = list(tutors)

    return tuteeList,tutorList



def match(tutorList,tuteeList,quota):       #matches tutees with tutor groups

    for student in tuteeList:
        tuteeID = student[0]
        courseType = courseConvert(student[5])      #convert courseID to base type
        gradType = student[6]           #tutee grad type
        tutorGroup = student[4]         #group tutee assigned to
        print(courseType)
        if tutorGroup == "":
            
            for tutor in tutorList:
                researchType = tutor[4]     #base research type of tutor
                tuteeGroup = tutor[6]       #ID of tutor group
                tutees = tutor[7]           #list of tutees in group
                currentTutees = tutor[7].split(",")
                numTutees = len(currentTutees)
                if (student[4]=="" and courseType == researchType and numTutees<quota):
                    student[4] = tutor[6]   #assign student to tutor groupID
                    tutor[7] = tutor[7]+","+student[0]

            for tutor in tutorList:
                tuteeGroup = tutor[6]       #ID of tutor group
                tutees = tutor[7]           #list of tutees in group
                currentTutees = tutor[7].split(",")
                numTutees = len(currentTutees)
                if (student[4]=="" and numTutees<quota):  #might need to remove grad type.
                    student[4] = tutor[6]
                    tutor[7]= tutor[7]+","+student[0]
                if tutor[7][:1] == ",":
                    tutor[7]=tutor[7][1:]       #remove first comma
                
    return tuteeList,tutorList


def courseConvert(course):                  #converts tutee course into a base type for comparison with tutor research type
    if course == "UFBSCMSA" or course =="UFBSCMSB":
        cType = "pure"
    elif course =="UFBSCSFA" or course =="UFBSCSFB":
        cType = "s&f"
    elif course =="UFBSCSHA" or course =="UFBSCSHB":
        cType = "hpc"
    elif course =="UFBSCVCA" or course =="UFBSCVCB":
        cType = "cv&cg"
    else:
        cType = "apSof"
    return cType




                
tuteeList,tutorList = listReader("Tutee.csv","Tutor.csv")
quota = 15
print (tuteeList)
tuteeList,tutorList=match(tutorList,tuteeList,quota)
print(tuteeList)
print(tutorList)




def reassignment(tuteeList,tutorList):
     choice = input('Select studentID for re-assignment ')
     counter = 0
     groupCounter = 0 
     for tutee in tuteeList:
        print(tutee)
        tuteeID = tutee[0]
        if choice == tuteeID:
            for tutor in tutorList:
                print(tutor)
                tuteesIn = tutor[7].split(',')
                counter = 0
                for Assigned in tuteesIn:
                    
                    if Assigned == choice:
 #                       print("Counter = " + tuteesIn[counter])
                        del tuteesIn[counter]
                        tutor[7] = tuteesIn
                        print(tutor)
                        tutee[4] = ""
                        print(tuteeList)
                       # print(tuteesIn[counter-1])
                    else:
                        counter = counter+1
          
                


                

reassignment(tuteeList,tutorList)

