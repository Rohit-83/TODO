import tkinter
from tkinter import *
from tkinter import messagebox as msg
import dbhelper


main = tkinter.Tk()
main.title("TODO")
main.geometry("500x600+300+300")
main.resizable(False,False)

def add():
    if (len(addtask.get())==0):
        msg.showinfo("ERROR","NO Task is Availabe\n Please Enter some Task first..")
    else:
        dbhelper.insertdata(addtask.get())
        #now if we want to see what we add in real time then
        addtask.delete(0, END)
        addvalue()

def addvalue():
    listbox.delete(0, END)
    for rows in dbhelper.show():
        listbox.insert(END, rows[1])

def deletetask(event):
    dbhelper.deletedatatask(listbox.get(ANCHOR))
    addvalue()


main.configure(
    background="#1d1d1d"
)
tkinter.Label(
    main,
    text="Task Manager",
    background = "#1d1d1d",
    foreground = "#eeeeee",
    font = ("Verdana 20")
).pack(pady=10)

addframe = tkinter.Frame(
    main,
    background="#eeeeee"
).pack()

addtask = tkinter.Entry(
    addframe,
    font = ("Verdana"),
    background = "#eeeeee"
)
addtask.pack(ipadx=20,ipady=4,pady=5)

addbtn = tkinter.Button(
    addframe,
    text = "ADD TASK ",
    command = add,
    background = "#e6d8d8",
    foreground = "red",
    relief = "flat",
    font = ("Verdana "),
    highlightcolor = "#000000",
    activebackground = "#1d1d1d",
    border = 0,
    activeforeground = "#eeeeee",
)
addbtn.pack(padx=20,ipadx=15,ipady=15,pady=3)

tkinter.Label(
    main,
    text="Your Task",
    background = "#1d1d1d",
    foreground = "#eeeeee",
    font = ("Calibri",17,"bold"),
).pack(pady=10)

taskframe = tkinter.Frame(
    main,
    bg= "#e6d8d8"
)
taskframe.pack(fill = BOTH , expand = 300)
scrollbar = Scrollbar(taskframe)
scrollbar.pack(side = RIGHT,fill = Y)
listbox = Listbox(
    taskframe,
    font = ("Verdana 18 bold"),
    bg = "#f7e9f7",
    fg = "#b0dce8",
    selectbackground = "white",
    selectforeground = "#1d1d1d"
)
listbox.pack(fill = BOTH, expand = 300)
listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listbox.yview)

listbox.bind("<Double-Button-1>",deletetask)
listbox.bind("<Delete>",deletetask)

tkinter.Label(
    main,
    text = "Help : Double Click On A Task to Delete ",
    background = "#1d1d1d",
    foreground = "#ffb24d",
    font = ("Calibri 18"),
).pack(side = BOTTOM,pady=10)
addvalue()

main.mainloop()