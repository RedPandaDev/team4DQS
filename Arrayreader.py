import csv

 
def arrayreader(filename,lists,items,header):
	with open(filename) as csvfile:
		rdr = csv.reader(csvfile)
		matix = [[0 for x in range(items)] for y in range(lists)]
		if header==True:
			csvfile.readline()
		for rows in rdr:
			for i in range(0,items):
				matrix[rows][i]=rows[i]
		
		return matrix
print(arrayreader("csvfile.csv",2,8,False))