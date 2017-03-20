#2.	Searching the personal tutor list for individual students 
import csv

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

def indvTute(studentID,tuteefilename):
	with open(tuteefilename) as csvfile:
		rdr = csv.reader(csvfile)
		csvfile.readline()
		for rows in rdr:
			if (int(rows[0])==studentID):
				return rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7]
	
def indvTutMain():
	#get tutor surname
	#get tutor forname1
	#get tutor forname2
	#get tutor csv file name

	#show basic list of tutees in group

	#get student ID
	#get tutee csv file name
	#show individual tutee full information

	