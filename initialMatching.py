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




def resetMatching(tuteeFile, tutorFile):    #empties all relevant values for reassignment
    tuteeList, tutorList = listReader(tuteeFile,tutorFile)

    for student in tuteeList:
        student[4]=""
    for tutor in tutorList:
        tutor[7] =""

    rewrite(tutorList, tuteeList)





def match(tutorList,tuteeList,quota):       #matches tutees with tutor groups
    tuteesLeft = len(tuteeList)
    for student in tuteeList:
        tuteeID = student[0]
        courseType = courseConvert(student[5])      #convert courseID to base type
        gradType = student[6]           #tutee grad type
        tutorGroup = student[4]         #group tutee assigned to
        if student[4] == "":    #if tutee is unassigned
            
            for tutor in tutorList:
                
                researchType = tutor[4]     #base research type of tutor
                
                tutees = tutor[7]           #list of tutees in group
                
                currentTutees = tutor[7].split(",")
                
                numTutees = len(currentTutees)

                if (student[4]=="" and courseType == researchType and numTutees<quota):
                    student[4] = tutor[6]   #assign student to tutor groupID
                    tutor[7] = tutor[7]+","+student[0]
                    tuteesLeft = tuteesLeft-1
            rewrite(tutorList,tuteeList)

            for tutor in tutorList:
                tutees = tutor[7]           #list of tutees in group
                currentTutees = tutor[7].split(",")
                numTutees = len(currentTutees)
                if (student[4]=="" and numTutees<quota): 
                    student[4] = tutor[6]   #assign tutee to tutor group
                    tutor[7]= tutor[7]+","+student[0]
                    tuteesLeft = tuteesLeft-1
                if tutor[7][:1] == ",":
                    tutor[7]=tutor[7][1:]       #remove first comma
            rewrite(tutorList,tuteeList)
    return tuteesLeft
    #print(tuteesLeft, "unassigned. You may want to increase your quota.")


def rewrite(tutorList, tuteeList):

    with open("Tutor.csv",'w', newline = '') as csvfile:    #overwrite tutor file with new info
        writeTo = csv.writer(csvfile, dialect='excel')
        writeTo.writerow(["Staff ID","Surname","Forename1","Forename2","Research Area","Grad Level","Tutor Group","Tutees"])    #header row
        for item in tutorList:
            writeTo.writerow(item)  #data rows


    with open("Tutee.csv",'w', newline = '') as csvfile2:   #overwrite tutee file with new info
        writeTo = csv.writer(csvfile2, dialect='excel')
        writeTo.writerow(["Student No","Surname","Forename1","Forename2","Tutor","Course","Grad Level","Univ Email"])   #same as above
        for item in tuteeList:
            writeTo.writerow(item)



            
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


def setQuota(UserQuota):                     #Allows user to set a quota for students
    try:
        if UserQuota >= 5:
            return True
        else:
            return False
    except ValueError:
        print("Please enter an integer value greater than 5.")
                


def mainMatching(quota, tuteeFile, tutorFile):
    tuteeList, tutorList = listReader(tuteeFile, tutorFile)       #example runthrough with quota of 10
    leftovers = match(tutorList, tuteeList, quota)
    print("Matching complete")
    message = str(leftovers) + " students left unassigned. You may want to increase your quota."
    print(message)
    return leftovers, str(message)
