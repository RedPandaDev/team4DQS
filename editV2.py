from initialMatching import listReader, rewrite


def reassignmentDel(studentID, tutorID, tuteeLink, tutorLink):
     tuteeList, tutorList = listReader(tuteeLink,tutorLink)

     choice = studentID
     counter = 0
     groupCounter = 0 
     for tutee in tuteeList:
        
        tuteeID = tutee[0]
        if choice == tuteeID:

            for tutor in tutorList:
                
                tuteesIn = tutor[7].split(',') 
                
                counter = 0

                for Assigned in tuteesIn:
                    
                    if Assigned == choice:
 #                       print("Counter = " + tuteesIn[counter])
                        del tuteesIn[counter]
                        print(tuteesIn)
                        print(tutor[7])
                        tutor[7] = ','.join(map(str, tuteesIn)) 
                        print(tutor[7])
                      
                        tutee[4] = ""

                       # print(tuteesIn[counter-1])
                    else:
                        counter = counter+1
            
     reassignmentAdd(tutorID, choice,tuteeList,tutorList)


def remove_punct(text):
    text_strip = ""
    for b in text:
        if b in "[']":
            b = ''
        text_strip += b
    return text_strip

def reassignmentAdd(tutorID, Add,tuteeList,tutorList):
     newTutor = tutorID
     counter = 0
     groupCounter = 0 
     for tutee in tuteeList:
        tuteeID = tutee[0]

        if Add == tuteeID:
            # add to tutee list too
            for tutor in tutorList:
                counter = 0
                if newTutor == tutor[0]:
                    
                    tutor[7] += "," + Add
                    
                    tutee[4] += newTutor


                    rewrite(tutorList, tuteeList)
                    return



              # merge both so you enter student ID and the tutor to reassign it to
              # and it removes the tutor from student and student from tutor list
              # and reassigns it to the new tutor in both

