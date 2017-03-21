#To Run Code:
#>>> from DisplayListsTutees import *
#>>> tuteeList("tutor6","tutor6","tutor6","Tutor.csv","Tutee.csv")
#-----------------------------------------------------------------
#Austen Wells Code for "Displaying Lists Of Tutees For A Particular Personal Tutor" Test Case
#This imports the CSV file
import csv
#TutorList is a function used to extract the student Numbers from each Tutor
#Query is used to compare the User Input with the expected input
def tutorList (querySN, queryFN1, queryFN2, tutorCSV, header=True):
#This allows the tutorList to access the tutorCSV file
	with open(tutorCSV) as csvfile:
#This reads the CSV file
		rdr = csv.reader(csvfile)
#This skips the header and reads the lines below the header
		if header==True:
			csvfile.readline()
#For loop to iterate over the rows 1,2,3 in the CSV file to find the Specific Personal Tutor
		for rows in list(rdr):
			nameSN = rows[1]
			nameFN1 = rows[2]
			nameFN2 = rows[3]
#If statement to check that inputs are correct
			if (nameSN == querySN and nameFN1 == queryFN1 and nameFN2 == queryFN2):
#If the values are valid then the program will display a list of student numbers
				tutee = [int(x) for x in rows[7].split(",")]
				return tutee
#This returns blank if an incorrect tutor is entered
		return ""
#The tuteeList function is used to display a list of all student details for each tutor
def tuteeList (querySN, queryFN1, queryFN2, tutorCSV, tuteeCSV, header=True):
#reads in the information from the tutorList function
	tutee = tutorList(querySN, queryFN1, queryFN2, tutorCSV, header=True)
#This prints a list of students numbers from a specific tutor group
	print(tutee)
#If statement checks if the tutees return blank then it will output the error "Invalid Tutor Entered"
	if (tutee != ""):
		studentlist = []
#This allows the tuteeList to access the tuteeCSV file
		with open(tuteeCSV) as csvfile:
#This reads the CSV file
			rdr = csv.reader(csvfile)
			csvfile.readline()
#For loop to iterate and display the individual rows of students from the Tutors Tutee List
			for students in rdr:
				name = int(students[0])
				if (name in tutee):
					print (students)
					studentlist.append(students)
#Else statement throws the error if an invalid tutor is entered
	else:
		print("Invalid Tutor Entered")
