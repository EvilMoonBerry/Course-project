#Start and menu taken from course material 6 python homewrok template
from bokeh.io import output_file, show
from bokeh.plotting import figure
from venv import create
import sqlite3
from tkinter import INSERT
from math import pi
from tkinter.tix import Select
db = sqlite3.connect('bookdatabase1.db')
cur = db.cursor()
def initializeDB():
    try:
        f = open("queries.sql", "r")
        commandstring = ""
        for line in f.readlines():
            commandstring+=line
        cur.executescript(commandstring)
    except sqlite3.OperationalError:
        print("Database exists, skip initialization")
    except:
        print("No SQL file to be used for initialization")
 
 
def main():
    initializeDB()
    userInput = -1
    while(userInput != "0"):
        print("\nMenu options:")
        print("1: Print users bought books")
        print("2: Print Books that users have bought and reviewed")
        print("3: Change password")
        print("4: Delete a review")
        print("5: Print user info")
        print("6: Add new user")
        print("0: Quit")
        userInput = input("What do you want to do? ")
        print(userInput)
        if userInput == "1":
            printboughtbooks()
        if userInput == "2":
            printReviews()
        if userInput == "3":
            changepassword()
        if userInput == "4":
            deleteReview()
        if userInput == "5":
            printuserinfo()
        if userInput =="6":
            addNewUser()
        if userInput == "0":
            print("Ending software...")
    db.close()        
    return
 
def printboughtbooks():
    username = input("Give username:")
    cur.execute("SELECT UserID FROM User where Username='%s'"%username)
    id = cur.fetchone ()
    cur.execute("SELECT FK_BookID FROM Bought_books where FK_UserID='%s'"%id)
    row = cur.fetchall ()
    for piece in row:
        cur.execute("SELECT * FROM Books where BookID ='%s'"%piece)
        bookn= cur.fetchone()
        print("Book name: "+str(bookn[1]))
   
    return
 
def printReviews():
    points=[]
    names=[]
    cur.execute("""SELECT User.Username, Bought_books.FK_BookID, Reviewed_books.FK_BookID,Reviewed_books.score FROM User
        INNER JOIN Bought_books ON User.UserID=Bought_books.FK_UserID
        INNER JOIN Reviewed_books ON Bought_books.FK_UserID = Reviewed_books.FK_UserID
        WHERE Reviewed_books.FK_BookID=Bought_books.FK_BookID """);
    row = cur.fetchall()
    for i in row:
 
        print("Username: "+i[0])
        for x in cur.execute("SELECT Book_name FROM Books WHERE BookID='%s'"%i[1]):
            names.append((x[0]))
            print("Bought Book: "+str(x[0]))
        print("Score: "+str(i[3]))
        points.append((i[3]))
        print("")

    
    output_file("bars.html")


    p = figure(x_range=names, height=250, title="Book reviws",
        toolbar_location=None, tools="")

    p.vbar(x=names, top=points, width=0.9)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    show(p)
    return
 
def changepassword():
    username =input("Give username: ")
    passw = input("Give new password: ")
    newp = ("UPDATE User SET Password = ? where Username =?")
    cur.execute(newp,[passw,username])
    db.commit()
    print(cur.rowcount, "record(s) affected")
    return
 
def deleteReview():
    BookN = input("Which books review you want to delete?: ")
    cur.execute("SELECT books.Book_name, Reviews.text FROM Reviews INNER JOIN Reviewed_books ON Reviewed_books.ReviewID=Reviews.FK_ReviewID INNER JOIN Books on Reviewed_books.FK_BookID=Books.BookID")
    row = cur.fetchall()
    print(row)
    
    cur.execute("SELECT BookID FROM Books WHERE Book_name ='%s'"%BookN);
    nameID = cur.fetchone()
    cur.execute("SELECT ReviewID FROM Reviewed_books WHERE FK_BookID ='%s'"%nameID);
    rID = cur.fetchone()
    remove = ("DELETE FROM Reviews Where FK_ReviewID = '%s'"%rID)
    cur.execute(remove)
    db.commit
    print(cur.rowcount, "record(s) deleted")

    cur.execute("SELECT books.Book_name, Reviews.text FROM Reviews INNER JOIN Reviewed_books ON Reviewed_books.ReviewID=Reviews.FK_ReviewID INNER JOIN Books on Reviewed_books.FK_BookID=Books.BookID")
    line = cur.fetchall()
    print(line)
    return
 
def printuserinfo():
    username = input("Give username: ")
    cur.execute("SELECT * FROM User WHERE Username ='%s'"%username);
    row = cur.fetchone()
 
    print("ID: "+str(row[0]))
    print("Username: "+row[1])
    print("Password: "+row[2])
    print("Email: "+row[3])
    return
 
def addNewUser():
    userid=input("Give user ID")
    username = input("Give username: ")
    password=input("Give password: ")
    email = input("Give email:")
    nUser=("INSERT INTO User (UserID,Username,Password,Email) VALUES (?,?,?,?)")
    cur.execute(nUser,[userid,username,password,email])
    db.commit
    
    print("New user added!")
    return
 
 
main()

