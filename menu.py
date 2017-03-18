from tkinter import *
from tkinter.filedialog import askopenfilename as aofn
from tkinter.filedialog import asksaveasfile as asfn

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()


def OpenFile():
    name = aofn(initialdir="C:/",
                defaultextension='.csv',
                filetypes=(("All Excel Files", "*.xls;*.csv" ), ("All Files", "*.*")),
                title="Choose a file.")
    print(name)

    try:
        with open(name, 'r') as UseFile:
            print(UseFile.read())
    except:
        print("No file exists")

def file_save():
    save = asfn(initialdir="C:/",
                filetypes=(("Excel File(.xls)", "*.xls"),("CSV File(.csv)", "*.csv"), ("All Files", "*.*")),
                title="Choose a file.")
    if save is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(text.get(1.0, END)) # This saves the text?
    save.write(text2save)
    save.close() # `()` was missing.

def create_layout(frame):
    frame = Frame(frame)
    frame.pack(side = LEFT, fill=BOTH)
    w = Label(frame, text="Assign Students", font=("Helvetica", 16))
    w.pack()

    b = Button(frame, text='Open File', command=OpenFile, width = 40)
    b.pack(pady = 5, padx = 30)
    c = Button(frame, text='Assign All Students', command=donothing,  width = 40)
    c.pack(pady = 5, padx = 20)
    d = Button(frame, text='Find a Student', command=donothing,  width = 40)
    d.pack(pady = 5, padx = 20)
    e = Button(frame, text='Assign One Student', command=donothing,  width = 40)
    e.pack(pady = 5, padx = 20)
    f = Button(frame, text='Remove Student', command=donothing,  width = 40)
    f.pack(pady = 5, padx = 20)
    g = Button(frame, text='Quota', command=donothing,  width = 40)
    g.pack(pady = 5, padx = 20)
    h = Button(frame, text='List Tutees', command=donothing,  width = 40)
    h.pack(pady = 5, padx = 20)
    i = Button(frame, text='Exit', command=root.quit,  width = 40)
    i.pack(pady = 40, padx = 20)


root = Tk()
root.title("Student Assignment")
root.minsize(width=350, height=400)
menubar = Menu(root)
create_layout(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=OpenFile)
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
