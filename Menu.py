from tkinter import *
from tkinter.filedialog import askopenfilename as aofn
from tkinter.filedialog import asksaveasfile as asfn
from DisplayListsTutees import tuteeList
from initialMatching import mainMatching, setQuota, resetMatching
from indvStudent import indvTutee
from editV2 import reassignmentDel


tuteeLink = "NA"
tutorLink = "NA"


def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()

#------------ Open files ------------#

def OpenTuteeFile():
    name = aofn(initialdir="H:",
                defaultextension='.csv',
                filetypes=(("All Excel Files", "*.xls;*.csv"), ("All Files", "*.*")),
                title="Choose a file.")
    global tuteeLink
    tuteeLink = name;
    print(tuteeLink)

    try:
        with open(name, 'r') as UseFile:
            print(UseFile.read())
    except:
        print("No file exists")

    return tuteeLink


def OpenTutorFile():
    name = aofn(initialdir="H:",
                defaultextension='.csv',
                filetypes=(("All Excel Files", "*.xls;*.csv" ), ("All Files", "*.*")),
                title="Choose a file.")
    global tutorLink
    tutorLink = name;
    print(tutorLink)
    try:
        with open(name, 'r') as UseFile:
            print(UseFile.read())
    except:
        print("No file exists")
        
    return tutorLink

#------------ Save file? ------------#

def file_save():
    save = asfn(initialdir="C:/",
                filetypes=(("Excel File(.xls)", "*.xls"),("CSV File(.csv)", "*.csv"), ("All Files", "*.*")),
                title="Choose a file.")
    if save is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(text.get(1.0, END)) # This saves the text?
    save.write(text2save)
    save.close() # `()` was missing.

#------------ Clear Matching ------------#

def clearMatching():
    clear = Toplevel(root)
    clear.grid()
    clear.grab_set()
    label = Label(clear, text="Are you sure you want to clear student assignment?", font=("Calibri", 14))
    label.grid(row=1, column=1, columnspan=3, sticky=W, padx=5, pady=5)

    def clearIt():
        global tuteeLink
        global tutorLink
        resetMatching(tuteeLink, tutorLink)
        clear.destroy()

        cleared = Toplevel(root)
        cleared.grid()
        cleared.grab_set()
        label = Label(cleared, text="Assignment successfully cleared.", font=("Calibri", 14))
        label.grid(row=1, column=1, sticky='', padx=20, pady=10)

        def closeCleared():
            cleared.destroy()

        button = Button(cleared, text="Okay", command=closeCleared)
        button.grid(row = 2, column=1, sticky='', padx=20, pady=10)


    def closeClearing():
        clear.destroy()

    button = Button(clear, text="Okay", command=clearIt)
    button.grid(row = 3, column=2, sticky=W, padx=15, pady=5)
    button = Button(clear, text="Cancel", command=closeClearing)
    button.grid(row = 3, column=3, sticky=W, padx=15, pady=5)

    
#------------ First Matching ------------#

def FirstMatching():
    matching = Toplevel(root)
    matching.grid()
    matching.grab_set()
    label = Label(matching, text="Make sure you are matching the correct files.", font=("Calibri", 14))
    label.grid(row=1, column=1, columnspan=3, sticky=W, padx=5, pady=5)
    label = Label(matching, text="Enter a quota for each tutor:")
    label.grid(row=2, column=1, columnspan=2, sticky=W, padx=5, pady=5)

    textQuota = Entry(matching)
    textQuota.grid(row=2, column=3, sticky='', padx=5, pady=5)

    def enterQuota():
        global tuteeLink
        global tutorLink
        quota = int(textQuota.get())
        checkQuota = setQuota(quota)
        if (checkQuota == False):
            error = Toplevel(root)
            error.grid()
            error.grab_set()

            def closeError():
                error.destroy()
            label = Label(error, text="Make sure you enter an integer number, 5 or higher!", font=("Calibri", 14))
            label.grid(row=1, column=1, columnspan=3, sticky=W, padx=5, pady=5)
            button = Button(error, text="Okay", command=closeError)
            button.grid(row = 3, column=2, sticky=W, padx=15, pady=5)
        else:
            matching.destroy()
            leftovers, text = mainMatching(quota, tuteeLink, tutorLink)

            successMatch = Toplevel(root)
            successMatch.grid()
            successMatch.grab_set()

            def closeSuccessMatch():
                successMatch.destroy()

            label = Label(successMatch, text="Students assigned to Tutors succesfully!", font=("Calibri", 14))
            label.grid(row=1, column=1,  sticky='', padx=5, pady=5)
            
            if (leftovers >0):
                label = Label(successMatch, text=text, font=("Calibri", 12))
                label.grid(row=2, column=1,  sticky='', padx=5, pady=5)

            button = Button(successMatch, text="Okay", command=closeSuccessMatch)
            button.grid(row = 3, column=1, sticky='', padx=15, pady=5)




    def closeMatching():
        matching.destroy()

    button = Button(matching, text="Okay", command=enterQuota)
    button.grid(row = 3, column=2, sticky=W, padx=15, pady=5)
    button = Button(matching, text="Cancel", command=closeMatching)
    button.grid(row = 3, column=3, sticky=W, padx=15, pady=5)

#------------ Find Individual Student ------------#

def findIndStu(): 
    findingIndStu = Toplevel(root)
    findingIndStu.grid()
    findingIndStu.grab_set()
    
    label = Label(findingIndStu, text='Enter Tutor name you want to know about:', font=("Calibri", 16))
    label.grid(row=1, column=1, columnspan=2, sticky=E, padx=5, pady=5)

    labelName = Label(findingIndStu, text="Enter Tutor Forename: ")
    labelName.grid(row=2, column=1, sticky=E, padx=5, pady=5)
    textName = Entry(findingIndStu)
    textName.grid(row=2, column=2, sticky=W, padx=5, pady=5)
    textName.delete(0, END)

    labelMidName = Label(findingIndStu, text="Enter Tutor Middle Name: ")
    labelMidName.grid(row=3, column=1, sticky=E, padx=5, pady=5)
    textMidName = Entry(findingIndStu)
    textMidName.grid(row=3, column=2, sticky=W, padx=5, pady=5)
    textMidName.delete(0, END)

    labelSurame = Label(findingIndStu, text="Enter Tutor Surname: ")
    labelSurame.grid(row=4, column=1, sticky=E, padx=5, pady=5)
    textSurame = Entry(findingIndStu)
    textSurame.grid(row=4, column=2, sticky=W, padx=5, pady=5)
    textSurame.delete(0, END)

    def displayTuteesSmall():
        global tuteeLink
        global tutorLink
        tutorName1 = textName.get()
        tutorName2 = textMidName.get()
        tutorName3 = textSurame.get()
        findingIndStu.destroy()
        tutees = tuteeList(tutorName3, tutorName1, tutorName2,  tutorLink, tuteeLink)

        listingofTuteesSmall = Toplevel(root)
        listingofTuteesSmall.grid()
        listingofTuteesSmall.grab_set()
        title = tutorName1, tutorName2, tutorName3
        label = Label(listingofTuteesSmall, text='Tutees assigned to:', font=("Calibri", 16))
        label.grid(row=1, column=1, columnspan=2, sticky=E, padx=5, pady=5)
        label = Label(listingofTuteesSmall, text=title, font=("Calibri", 16))
        label.grid(row=1, column=3,columnspan=2, sticky=W, padx=5, pady=5)

        label = Label(listingofTuteesSmall, text='Student No')
        label.grid(row=2, column=1, sticky=W, padx=5, pady=5)
        label = Label(listingofTuteesSmall, text='Surname')
        label.grid(row=2, column=2, sticky=W, padx=5, pady=5)
        label = Label(listingofTuteesSmall, text='Forename1')
        label.grid(row=2, column=3, sticky=W, padx=5, pady=5)
        label = Label(listingofTuteesSmall, text='Forename2')
        label.grid(row=2, column=4, sticky=W, padx=5, pady=5)
        label = Label(listingofTuteesSmall, text='Tutor')


        def showIndStudent():
            listingofTuteesSmall.destroy()

            indStudent = Toplevel(root)
            indStudent.grid()
            indStudent.grab_set()
            labelName = Label(indStudent, text="Search for Student information:", font=("Calibri", 16))
            labelName.grid(row=1, column=1, columnspan=2, sticky='', padx=5, pady=5)
            labelName = Label(indStudent, text="Enter Student Number: ")
            labelName.grid(row=2, column=1, sticky=E, padx=5, pady=5)
            textStuNo = Entry(indStudent)
            textStuNo.grid(row=2, column=2, sticky=W, padx=5, pady=5)
            textStuNo.delete(0, END)

            def closeindStudent():
                indStudent.destroy()

            def displayStudent():
                global tuteeLink
                studentID = int(textStuNo.get())
                rows1,rows2,rows3,rows4,rows5,rows6,rows7,rows8 = indvTutee(studentID,tuteeLink)

                indStudent.destroy()
                studentDisplay = Toplevel(root)
                studentDisplay.grid()
                studentDisplay.grab_set()

                label = Label(studentDisplay, text='Student Information', font=("Calibri", 16))
                label.grid(row=1, column=1,columnspan=8, sticky='', padx=5, pady=5)

                label = Label(studentDisplay, text='Student No')
                label.grid(row=2, column=1, sticky=W, padx=5, pady=5)
                label = Label(studentDisplay, text='Surname')
                label.grid(row=2, column=2, sticky=W, padx=5, pady=5)
                label = Label(studentDisplay, text='Forename1')
                label.grid(row=2, column=3, sticky=W, padx=5, pady=5)
                label = Label(studentDisplay, text='Forename2')
                label.grid(row=2, column=4, sticky=W, padx=5, pady=5)
                label = Label(studentDisplay, text='Tutor')
                label.grid(row=2, column=5, sticky=W, padx=5, pady=5)
                label = Label(studentDisplay, text='Course')
                label.grid(row=2, column=6, sticky=W, padx=5, pady=5)
                label = Label(studentDisplay, text='Grad Level')
                label.grid(row=2, column=7, sticky=W, padx=5, pady=5)
                label = Label(studentDisplay, text='Univ Email')
                label.grid(row=2, column=8, sticky=W, padx=5, pady=5)

                label = Label(studentDisplay, text=rows1)
                label.grid(row=3, column=1, sticky=W, padx=5, pady=5)
                label = Label(studentDisplay, text=rows2)
                label.grid(row=3, column=2, sticky=W, padx=5, pady=5)
                label = Label(studentDisplay, text=rows3)
                label.grid(row=3, column=3, sticky=W, padx=5, pady=5)
                label = Label(studentDisplay, text=rows4)
                label.grid(row=3, column=4, sticky=W, padx=5, pady=5)
                label = Label(studentDisplay, text=rows5)
                label.grid(row=3, column=5, sticky=W, padx=5, pady=5)
                label = Label(studentDisplay, text=rows6)
                label.grid(row=3, column=6, sticky=W, padx=5, pady=5)
                label = Label(studentDisplay, text=rows7)
                label.grid(row=3, column=7, sticky=W, padx=5, pady=5)
                label = Label(studentDisplay, text=rows8)
                label.grid(row=3, column=8, sticky=W, padx=5, pady=5)

                def closeDisplay():
                    studentDisplay.destroy()

                button = Button(studentDisplay, text="Close", command=closeDisplay)
                button.grid(row=4, column=1, columnspan=8,  sticky='', padx=5, pady=10)




            button = Button(indStudent, text="Show information", command=displayStudent)
            button.grid(row=5, column=1,  sticky=N, padx=5, pady=5)
            button = Button(indStudent, text="Cancel", command=closeindStudent)
            button.grid(row=5, column=2, sticky=N, padx=5, pady=5)



        i = 2
        for lists in tutees:
            
            i += 1
            label = Label(listingofTuteesSmall, text=lists[0])
            label.grid(row=i, column=1, sticky=W, padx=5, pady=5)
            label = Label(listingofTuteesSmall, text=lists[1])
            label.grid(row=i, column=2, sticky=W, padx=5, pady=5)
            label = Label(listingofTuteesSmall, text=lists[2])
            label.grid(row=i, column=3, sticky=W, padx=5, pady=5)
            label = Label(listingofTuteesSmall, text=lists[3])
            label.grid(row=i, column=4, sticky=W, padx=5, pady=5)
            label = Label(listingofTuteesSmall, text=lists[4])

        label = Label(listingofTuteesSmall, text='Make sure to note down the student number for the wanted student.', font=("Calibri", 12))
        label.grid(row=i+1, column=1, columnspan=5, sticky='', padx=5, pady=5)

        button = Button(listingofTuteesSmall, text="Continue", command=showIndStudent)
        button.grid(row = i+2, column=1, columnspan=5, sticky=N, padx=5, pady=5)

    def closefindingIndStu():
        findingIndStu.destroy()

    button = Button(findingIndStu, text="List Tutees", command=displayTuteesSmall)
    button.grid(row=5, column=1,  sticky=N, padx=5, pady=5)
    button = Button(findingIndStu, text="Cancel", command=closefindingIndStu)
    button.grid(row=5, column=2, sticky=N, padx=5, pady=5)
#------------ Re-Assign Students ------------#
def reAssign():
    reassignTutees = Toplevel(root)
    reassignTutees.grid()
    reassignTutees.grab_set()

    labelName = Label(reassignTutees, text="Re-Assign a Student", font=("Calibri", 16))
    labelName.grid(row=1, column=1, columnspan=2, sticky='', padx=5, pady=5)
    labelName = Label(reassignTutees, text="Enter Student Number for Student to be Re-Assigned: ")
    labelName.grid(row=2, column=1, sticky=E, padx=5, pady=5)
    textStuNo = Entry(reassignTutees)
    textStuNo.grid(row=2, column=2, sticky=W, padx=5, pady=5)
    textStuNo.delete(0, END)

    labelName = Label(reassignTutees, text="Enter Tutor Number to Assign the Student to: ")
    labelName.grid(row=3, column=1, sticky=E, padx=5, pady=5)
    textTutNo = Entry(reassignTutees)
    textTutNo.grid(row=3, column=2, sticky=W, padx=5, pady=5)
    textTutNo.delete(0, END)

    def assign():
        global tuteeLink
        global tutorLink
        studID = textStuNo.get()
        tutorID = textTutNo.get()
        reassignmentDel(studID, tutorID, tuteeLink, tutorLink)
        reassignTutees.destroy()

        reAssigned = Toplevel(root)
        reAssigned.grid()
        reAssigned.grab_set()
        label = Label(reAssigned, text="Student was re-assigned.", font=("Calibri", 14))
        label.grid(row=1, column=1, sticky='', padx=20, pady=10)
        def closeReAssigned():
            reAssigned.destroy()

        button = Button(reAssigned, text="Okay", command=closeReAssigned)
        button.grid(row=2, column=1, sticky='', padx=5, pady=5)

    def closeReassignTutees():
        reassignTutees.destroy()

    button = Button(reassignTutees, text="Re-Assign Student", command=assign)
    button.grid(row=5, column=1,  sticky=N, padx=5, pady=5)
    button = Button(reassignTutees, text="Cancel", command=closeReassignTutees)
    button.grid(row=5, column=2, sticky=N, padx=5, pady=5)


#------------ List Tutees ------------#

def listTutees():
    listingTutees = Toplevel(root)
    listingTutees.grid()
    listingTutees.grab_set()
    
    label = Label(listingTutees, text='Enter Tutor name you want to know about:', font=("Calibri", 16))
    label.grid(row=1, column=1, columnspan=2, sticky=E, padx=5, pady=5)

    labelName = Label(listingTutees, text="Enter Tutor Forename: ")
    labelName.grid(row=2, column=1, sticky=E, padx=5, pady=5)
    textName = Entry(listingTutees)
    textName.grid(row=2, column=2, sticky=W, padx=5, pady=5)
    textName.delete(0, END)

    labelMidName = Label(listingTutees, text="Enter Tutor Middle Name: ")
    labelMidName.grid(row=3, column=1, sticky=E, padx=5, pady=5)
    textMidName = Entry(listingTutees)
    textMidName.grid(row=3, column=2, sticky=W, padx=5, pady=5)
    textMidName.delete(0, END)

    labelSurame = Label(listingTutees, text="Enter Tutor Surname: ")
    labelSurame.grid(row=4, column=1, sticky=E, padx=5, pady=5)
    textSurame = Entry(listingTutees)
    textSurame.grid(row=4, column=2, sticky=W, padx=5, pady=5)
    textSurame.delete(0, END)

    def displayTutees():
        global tuteeLink
        global tutorLink
        tutorName1 = textName.get()
        tutorName2 = textMidName.get()
        tutorName3 = textSurame.get()
        listingTutees.destroy()
        tutees = tuteeList(tutorName3, tutorName1, tutorName2,  tutorLink, tuteeLink)

        listingofTutees = Toplevel(root)
        listingofTutees.grid()
        listingofTutees.grab_set()
        title = tutorName1, tutorName2, tutorName3
        label = Label(listingofTutees, text='Tutees assigned to:', font=("Calibri", 16))
        label.grid(row=1, column=1, columnspan=4, sticky=E, padx=5, pady=5)
        label = Label(listingofTutees, text=title, font=("Calibri", 16))
        label.grid(row=1, column=5,columnspan=4, sticky=W, padx=5, pady=5)

        label = Label(listingofTutees, text='Student No')
        label.grid(row=2, column=1, sticky=W, padx=5, pady=5)
        label = Label(listingofTutees, text='Surname')
        label.grid(row=2, column=2, sticky=W, padx=5, pady=5)
        label = Label(listingofTutees, text='Forename1')
        label.grid(row=2, column=3, sticky=W, padx=5, pady=5)
        label = Label(listingofTutees, text='Forename2')
        label.grid(row=2, column=4, sticky=W, padx=5, pady=5)
        label = Label(listingofTutees, text='Tutor')
        label.grid(row=2, column=5, sticky=W, padx=5, pady=5)
        label = Label(listingofTutees, text='Course')
        label.grid(row=2, column=6, sticky=W, padx=5, pady=5)
        label = Label(listingofTutees, text='Grad Level')
        label.grid(row=2, column=7, sticky=W, padx=5, pady=5)
        label = Label(listingofTutees, text='Univ Email')
        label.grid(row=2, column=8, sticky=W, padx=5, pady=5)

        def closeListingofTutees():
            listingofTutees.destroy()

        i = 2
        for lists in tutees:
            
            i += 1
            label = Label(listingofTutees, text=lists[0])
            label.grid(row=i, column=1, sticky=W, padx=5, pady=5)
            label = Label(listingofTutees, text=lists[1])
            label.grid(row=i, column=2, sticky=W, padx=5, pady=5)
            label = Label(listingofTutees, text=lists[2])
            label.grid(row=i, column=3, sticky=W, padx=5, pady=5)
            label = Label(listingofTutees, text=lists[3])
            label.grid(row=i, column=4, sticky=W, padx=5, pady=5)
            label = Label(listingofTutees, text=lists[4])
            label.grid(row=i, column=5, sticky=W, padx=5, pady=5)
            label = Label(listingofTutees, text=lists[5])
            label.grid(row=i, column=6, sticky=W, padx=5, pady=5)
            label = Label(listingofTutees, text=lists[6])
            label.grid(row=i, column=7, sticky=W, padx=5, pady=5)
            label = Label(listingofTutees, text=lists[7])
            label.grid(row=i, column=8, sticky=W, padx=5, pady=5)

        button = Button(listingofTutees, text="Okay", command=closeListingofTutees)
        button.grid(row = i+1, column=1, columnspan=8, sticky=N, padx=5, pady=5)

    def closeListingTutees():
        listingTutees.destroy()

    button = Button(listingTutees, text="List Tutees", command=displayTutees)
    button.grid(row=5, column=1,  sticky=N, padx=5, pady=5)
    button = Button(listingTutees, text="Cancel", command=closeListingTutees)
    button.grid(row=5, column=2, sticky=N, padx=5, pady=5)

#------------ Main Layout ------------#

def create_layout(frame):
    frame = Frame(frame)
    frame.grid()

    w = Label(frame, text="Assign Students", font=("Helvetica", 16))
    w.grid(row=1, column=1, columnspan=3, sticky='', padx=5, pady=5)

    w = Label(frame, text="")
    w.grid(row=1, column=1, sticky='', padx=5, pady=5)
    w = Label(frame, text="")
    w.grid(row=1, column=3, sticky='', padx=5, pady=5)

    b = Button(frame, text='Open Student File', command=OpenTuteeFile, width=40)
    b.grid(row=2, column=2, sticky=E, padx=15, pady=5)

    c = Button(frame, text='Open Tutor File', command=OpenTutorFile, width=40)
    c.grid(row=3, column=2, sticky='', padx=15, pady=5)

    w = Label(frame, text="")
    w.grid(row=4, column=2, sticky='', padx=5, pady=5)

    d = Button(frame, text='Assign All Students', command=FirstMatching, width=40)
    d.grid(row=5, column=2, sticky='', padx=15, pady=5)

    e = Button(frame, text='Find a Student', command=findIndStu, width=40)
    e.grid(row=6, column=2, sticky='', padx=15, pady=5)

    f = Button(frame, text='Re-assign a Student', command=reAssign, width=40)
    f.grid(row=7, column=2, sticky='', padx=15, pady=5)

    g = Button(frame, text='Quota', command=donothing, width=40)
    g.grid(row=8, column=2, sticky='', padx=15, pady=5)

    h = Button(frame, text='List Tutees', command=listTutees, width=40)
    h.grid(row=9, column=2, sticky='', padx=15, pady=5)

    w = Label(frame, text="")
    w.grid(row=10, column=3, sticky='', padx=5, pady=5)

    d = Button(frame, text='Clear Tutor Student Assignments', command=clearMatching, width=40)
    d.grid(row=11, column=2, sticky='', padx=15, pady=5)

    w = Label(frame, text="")
    w.grid(row=12, column=3, sticky='', padx=5, pady=0)

    i = Button(frame, text='Exit', command=root.quit, width=40)
    i.grid(row=13, column=2, sticky='', padx=15, pady=10)


root = Tk()
root.title("Student Assignment")
root.minsize(width=350, height=400)
menubar = Menu(root)
create_layout(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=file_save)

filemenu.add_separator()


filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()
