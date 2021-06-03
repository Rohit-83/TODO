import dbhelper
import os

os.system('clear')
choice = int(input("choose what you want ?\n\t1. View Task\n\t2. Add a Task\n\t3. Delete a Task\n\t4. Quit\n\t>"))

while choice != 4:
    if choice ==1:#view task
        os.system('clear')
        print("ID" , "\t" "TASK\n")
        for rows in dbhelper.show():
            print(str(rows[0]) + "\t" + rows[1])
        choice = int(
            input("choose what you want ?\n\t1. View Task\n\t2. Add a Task\n\t3. Delete a Task\n\t4. Quit\n\t>"))

    elif choice==2:#add a task
        task = input("Enter a task: ")
        if len(task)!=0:
            dbhelper.insertdata(task)
        choice = int(
            input("choose what you want ?\n\t1. View Task\n\t2. Add a Task\n\t3. Delete a Task\n\t4. Quit\n\t>"))

    elif choice==3:#delete a task
        #first we show the availabe option from which we have to delete
        os.system('clear')
        print("ID", "\t" "TASK\n")
        for rows in dbhelper.show():
            print(str(rows[0]) + "\t" + rows[1])
        id = int(input("Choose a task ID to delete : "))
        dbhelper.deletedata(id)
        choice = int(
            input("choose what you want ?\n\t1. View Task\n\t2. Add a Task\n\t3. Delete a Task\n\t4. Quit\n\t>"))

    else:
        print("You have to choose the correct option...")
        choice = int(
            input("choose what you want ?\n\t1. View Task\n\t2. Add a Task\n\t3. Delete a Task\n\t4. Quit\n\t>"))

else:
    print("Thank you for using the application....")