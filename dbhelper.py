import sqlite3
#for creation of data base
conn = sqlite3.connect('test.db')

#creation of table if not exists
conn.execute(''' CREATE TABLE IF NOT EXISTS todo(
id INTEGER PRIMARY KEY,
task TEXT NOT NULL
)
''')

#DATA INSERTION
#query = "INSERT INTO todo(task) VALUES('Reecord');"
#conn.execute(query)
#conn.commit()

def insertdata(newtask):
    query = "INSERT INTO todo(task) VALUES(?);"
    conn.execute(query,(newtask,))
    conn.commit()

#now we will make a function which delete task by id
def deletedata(newid):
    query = "DELETE FROM todo WHERE id = ?;"
    conn.execute(query,(newid,))
    conn.commit()

def deletedatatask(newtask):
    query = "DELETE FROM todo WHERE task = ?;"
    conn.execute(query,(newtask,))
    conn.commit()

#now we will make a function which update the data by id and task
def updatedata(newtask,newid):
    query = "UPDATE todo SET task =? WHERE id =?;"
    conn.execute(query,(newtask,newid))
    conn.commit()

def show():
    query = "SELECT * FROM todo;"
    return  conn.execute(query)


#insertdata("Sleeping")
#deletedata(3)
#updatedata("Eatiing",2)

#query = "SELECT * FROM todo;"
#for rows in conn.execute(query):
    #print(rows)
#print("database connected")
#conn.close()
#always close the data base