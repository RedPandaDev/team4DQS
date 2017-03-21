#2.	Searching the personal tutor list for individual students 
import csv
#don't worry about this oporation. input stage 1 uses this.
#searches through tutors to find the tutors related to them
def tutorList (querySN, queryFN1, queryFN2, filename, header=True):

	with open(filename) as csvfile:
		rdr = csv.reader(csvfile)
		if header==True:
			csvfile.readline()
		for rows in rdr:
			nameSN = rows[1]
			nameFN1 = rows[2]
			nameFN2 = rows[3]
			
			
			if (nameSN == querySN and nameFN1 == queryFN1 and nameFN2 == queryFN2):
				tutees = [int(x) for x in rows[7].split(",")]
				return tutees
		return ""
#INPUT STAGE1: give this oporation the Surname, Forname1, Forname2, Tutor CSV file locaton, Tutee CSV file location and if there is a header(optional)
#OUTPUT: you get 4 Arrays: Array 1 gives you the ID, array 2 gives you the surname, array 3 gives you forname1 array 4 gives you forname2. 
#take these and use the index to deisplay them in the correct order with the right names and ID'd.
def basicgroupstudent (querySN, queryFN1, queryFN2, tutfilename, tuteefilename, header=True):
	tutees = tutorList(querySN, queryFN1, queryFN2, tutfilename, header=True)
	ID = []
	namesSN = []
	namesFN1 = []
	namesFN2 = []
	with open(tuteefilename) as csvfile:
		rdr = csv.reader(csvfile)
		csvfile.readline()
		for rows in rdr:
			idx = int(rows[0])
			if (idx in tutees):
				ID.append(rows[0])

				namesSN.append(rows[1])
				namesFN1.append(rows[2])
				namesFN2.append(rows[3])
		return ID,namesSN,namesFN1,namesFN2

#INPUT STAGE2: give the oporation the studentID and the file location of the tutee CSV file
#OUTPUT: you get 8 strings, ID, Surname, Forname1, Forname2, Tutor, Course, Grad Level and University Email.
#this is the final output. either return to start or exit out of the oporation after.
def indvTute(studentID,tuteefilename):
	with open(tuteefilename) as csvfile:
		rdr = csv.reader(csvfile)
		csvfile.readline()
		for rows in rdr:
			if (int(rows[0])==studentID):
				return rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7]
	
