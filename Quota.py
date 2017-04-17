#Matthew Jones Code for 'Display information on the quota of tutees staff member has been assigned per year or degree group'
import csv


def CountYear(Year,Staff,filename,filename2, header = True):
#The counter begins at 0
    count = 0

    with open(filename) as csvfile: #Opens the tutee csv file
        with open(filename2) as csvfile2: # Opens the tutor csv file
 
            tutee = csv.reader(csvfile)
            tutor = csv.reader(csvfile2)

            if header==True: #Skips the header in both csv files
                csvfile.readline()
                csvfile2.readline()
                

                for tut in tutee:
                    if tut[6] == Year and tut[4] == Staff:
                        count += 1 #Adds 1 to the counter
                        
                for row in tutor:
                    if row[0] == Staff:
                        print(row[0],row[1],row[2],row[3],row[4],count)#Prints out specific rows from the tutor csv file + the counter
                        


def CountCode(Code,Staff,filename,filename2, header = True):
#Counter begins at 0
    count = 0
   
    with open(filename) as csvfile: #Opens the tutee csv file
        with open(filename2) as csvfile2: #Opens the tutor csv file
 
            tutee = csv.reader(csvfile)
            tutor = csv.reader(csvfile2)

            if header==True: #This skips the header in both csv files
                csvfile.readline()
                csvfile2.readline()
                

                for tut in tutee:
                    if tut[5] == Code and tut[4] == Staff:
                        count += 1 #Adds 1 to the counter
                        
                for row in tutor:
                    if row[0] == Staff:
                        print(row[0],row[1],row[2],row[3],row[4],count) #Prints out specific rows from the tutor csv file + the counter






