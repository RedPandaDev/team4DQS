from tkinter import *
from tkinter.filedialog import askopenfilename as aofn
from tkinter.filedialog import asksaveasfile as asfn
from DisplayListsTutees import tuteeList

tuteeLink = "Tutee.csv"
tutorLink = "Tutor.csv"

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()


def OpenTuteeFile():
    name = aofn(initialdir="H:",
                defaultextension='.csv',
                filetypes=(("All Excel Files", "*.xls;*.csv" ), ("All Files", "*.*")),
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

def file_save():
    save = asfn(initialdir="C:/",
                filetypes=(("Excel File(.xls)", "*.xls"),("CSV File(.csv)", "*.csv"), ("All Files", "*.*")),
                title="Choose a file.")
    if save is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(text.get(1.0, END)) # This saves the text?
    save.write(text2save)
    save.close() # `()` was missing.

def listTutees():
    listingTutees = Toplevel(root)
    listingTutees.grid()
    listingTutees.grab_set()

    labelName = Label(listingTutees, text="Enter Tutor Forename: ")
    labelName.grid(row=1, column=1, sticky=W, padx=5, pady=5)
    textName = Entry(listingTutees)
    textName.grid(row=1, column=2, sticky=W, padx=5, pady=5)
    textName.delete(0, END)

    labelMidName = Label(listingTutees, text="Enter Tutor Middle Name: ")
    labelMidName.grid(row=2, column=1, sticky=W, padx=5, pady=5)
    textMidName = Entry(listingTutees)
    textMidName.grid(row=2, column=2, sticky=W, padx=5, pady=5)
    textMidName.delete(0, END)

    labelSurame = Label(listingTutees, text="Enter Tutor Surname: ")
    labelSurame.grid(row=3, column=1, sticky=W, padx=5, pady=5)
    textSurame = Entry(listingTutees)
    textSurame.grid(row=3, column=2, sticky=W, padx=5, pady=5)
    textSurame.delete(0, END)

    def displayTutees():
        global tuteeLink
        global tutorLink
        tutorName1 = textName.get()
        tutorName2 = textMidName.get()
        tutorName3 = textSurame.get()
        listingTutees.destroy()
        tutees = tuteeList(tutorName1,tutorName2,tutorName3,tutorLink,tuteeLink)

        listingofTutees = Toplevel(root)
        listingofTutees.grid()
        listingofTutees.grab_set()
        title = tutorName1, tutorName2, tutorName3
        label = Label(listingofTutees, text='Tutees assigned to:', font=("Helvetica", 16))
        label.grid(row=1, column=1, sticky=E, padx=5, pady=5)
        label = Label(listingofTutees, text=title, font=("Helvetica", 16))
        label.grid(row=1, column=2, sticky=W, padx=5, pady=5)

        def close():
            listingofTutees.destroy()
            
        i = 1
        for lists in tutees:
            a = ', '.join(map(str, lists))
            i += 1
            label = Label(listingofTutees, text=a)
            label.grid(row=i, column=1, columnspan=2, sticky=W, padx=5, pady=5)

        button = Button(listingofTutees, text="Okay", command=close)
        button.grid(row = i+1, column=1, columnspan=2, sticky=N, padx=5, pady=5)


    button = Button(listingTutees, text="List Tutees", command=displayTutees)
    button.grid(row=4, column=1, columnspan=2, sticky=N, padx=5, pady=5)

    


def create_layout(frame):
    frame = Frame(frame)
    frame.pack(side = LEFT, fill=BOTH)
    w = Label(frame, text="Assign Students", font=("Helvetica", 16))
    w.pack()

    b = Button(frame, text='Open Student File', command=OpenTuteeFile, width = 40)
    b.pack(pady = 5, padx = 30)
    c = Button(frame, text='Open Tutor File', command=OpenTutorFile, width = 40)
    c.pack(pady = 5, padx = 30)
    d = Button(frame, text='Assign All Students', command=donothing,  width = 40)
    d.pack(pady = 5, padx = 20)
    e = Button(frame, text='Find a Student', command=donothing,  width = 40)
    e.pack(pady = 5, padx = 20)
    f = Button(frame, text='Re-assign a Student', command=donothing,  width = 40)
    f.pack(pady = 5, padx = 20)
    g = Button(frame, text='Quota', command=donothing,  width = 40)
    g.pack(pady = 5, padx = 20)
    h = Button(frame, text='List Tutees', command=listTutees,  width = 40)
    h.pack(pady = 5, padx = 20)
    i = Button(frame, text='Exit', command=root.quit,  width = 40)
    i.pack(pady = 40, padx = 20)


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
