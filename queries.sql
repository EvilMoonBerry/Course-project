CREATE TABLE User (

    UserID INT NOT NULL PRIMARY KEY,
    Username VARCHAR (60),
    Password VARCHAR (70),
    Email VARCHAR (60)
);
CREATE TABLE Book_store (
    StoreID INT NOT NULL PRIMARY KEY,
    Store_name VARCHAR (60),
    Address VARCHAR (60)
);
CREATE TABLE Books(
    BookID INT NOT NULL PRIMARY KEY,
    Book_name VARCHAR (60),
    Genre VARCHAR (60),
    Author VARCHAR, 
    Store_name VARCHAR (60),
    FOREIGN KEY (Store_name) REFERENCES Book_store (Store_name)
        ON DELETE CASCADE
);

CREATE TABLE Reviewed_books (
    ReviewID INT NOT NULL PRIMARY KEY,
    FK_UserID INT NOT NULL,
    FK_BookID INT NOT NULL,
    Score INT,
    FOREIGN KEY (FK_UserID) REFERENCES UserID (UserID)
        ON DELETE CASCADE,
    FOREIGN KEY (FK_BookID) REFERENCES Books (BookID)
        ON DELETE CASCADE
);

CREATE TABLE Bought_books (
    FK_UserID INT NOT NULL,
    FK_BookID INT NOT NULL,
    FK_Store_name VARCHAR (60),
    Username VARCHAR (60),
    FOREIGN KEY (FK_UserID) REFERENCES UserID (UserID)
        ON DELETE CASCADE,
    FOREIGN KEY (FK_BookID) REFERENCES Books (BookID)
        ON DELETE CASCADE,
    FOREIGN KEY (FK_Store_name) REFERENCES Books (Store_name)
        ON DELETE CASCADE,
    FOREIGN KEY (Username) REFERENCES UserID (Username)
        ON DELETE CASCADE
);

CREATE TABLE Reviews (
    FK_ReviewID int not null,
    Text VARCHAR (200),
    FOREIGN KEY (FK_ReviewID) REFERENCES Reviewed_books (ReviewID)
        ON DELETE CASCADE
);


INSERT INTO User VALUES
    (10001,"Bookworm","PaGe","Bookworm321@gmail.com"),
    (10002,"BookFairy","Twinkle","FairyDust@hotmail.com"),
    (10003,"BookGeek","1234","IHaveGoodPassword1234@gmail.com");
    
INSERT INTO Book_store VALUES
    (20001,"Suomalainen Kirjakauppa","Brahenkatu 5"),
    (20002,"Akateeminen kirjakauppa","Pohjoisesplanadi 39"),
    (20003,"Adlibris","Verkkokauppa");

INSERT INTO Books VALUES
    (30001,"Tänään olen Elossa","Biography","Oskari Saari","Akateeminen kijakauppa"),
    (30002,"Harry Potter: All About the Hogwarts Houses","Young adults","Vanessa Moody","Akateeminen kirjakauppa"),
    (30003,"Tiitiäisen satupuu","Kirsi Kunnas","Childern books","Suomalinen Kirjakauppa"),
    (30004,"Onnelliset Villasukat","Otava","Hobby books","Suomalainen Kirjakauppa"),
    (30005,"Ennen lintuja","Merj Mäki","Historic romance novels","Adlibris");

INSERT INTO Bought_books VALUES
    (10001,30002,"Akateeminen kirjakauppa","Bookworm"),
	(10001,30004,"Akateeminen kirjakauppa","Bookworm"),
    (10002,30002,"Akateeminen kirjakauppa","BookFairy"),
    (10003,30003,"Suomalainen Kirjakauppa","BookGeek");
    
INSERT INTO Reviewed_books VALUES
    (0001,10001,30002,10),
    (0002,10002,30003,8),
    (0003,10003,30003,7);
    
    
INSERT INTO Reviews VALUES
    (0001,"Was great"),
    (0002,"Would read again"),
    (0003,"So nice");
  

