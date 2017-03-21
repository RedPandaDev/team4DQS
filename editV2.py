

#Needs desperately Sam's code
                


def reassignmentDel(tuteeList,tutorList):
    

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

     reassignmentAdd(choice,tuteeList,tutorList)



def reassignmentAdd(Add,tuteeList,tutorList):
     newTutor = input('Enter a tutor ID ')
     counter = 0
     groupCounter = 0 
     for tutee in tuteeList:
        tuteeID = tutee[0]
        tutee[4] += newTutor
        print(tutee)
        if Add == tuteeID:
            # add to tutee list too
            for tutor in tutorList:
                print(tutor)
                counter = 0
                if newTutor == tutor[0]:
                    tutor[7] += "," + Add
                    print(tutor)
                    return

              # merge both so you enter student ID and the tutor to reassign it to
              # and it removes the tutor from student and student from tutor list
              # and reassigns it to the new tutor in both

