class Library:
    User=[]
    Book=[]
    IssuedBook=[]
    Fund=0
    def seebooks():
        print(Library.Book)
    
class Reader(Library):
    
    def __init__(self, name):
        self.Name= name
        super().User.append(self.Name)
        print("Thank you for using our service! Happy reading:)")
      
    def issuebook(bookname):
        if bookname in Library.Book:
            Library.IssuedBook.append(bookname)
            Library.Book.remove(bookname)
            print("Here is your book!!")
        else:
            print("Sorry the book is not available:')")
    
    def returnbook(bookname):
        if bookname in Library.IssuedBook:
            a= Library.IssuedBook.pop(bookname)
            Library.Book.append(a)
            print("Thanks for taking our service! Visit again:)")

                    
        
class Admin(Reader):
    def addbook(name):
        Library.Book.append(name)
        
    def removebook(name):
        Library.Book.pop(name)

    def seeuser():
        print(Reader.__dict__)

i=1
while i>0:
    print("Welcome to the Library")
    a= int(input("Are you a (1)reader or the (2)admin or a (3)Visitor?  "))
    if (a==1):
        b= int(input("What do you want? (1). Register your self (2). Issue Book (3). Return Book"))
        if b==1:
            name= input("Enter your name: ")
            name= Reader(name)
        if b==2:
            bn1= input("Enter book name: ")
            bn1= Reader.issuebook(bn1)
        if b==3:
            bn2= input("Enter book name: ")
            Reader.returnbook(bn2)
    if (a==2):
        c= int(input("What do you want? (1). Add Book? (2). Remove book?"))
        if c==1:
            bn3= input("Enter the book name: ")
            Admin.addbook(bn3)
        if c==2:
            bn4= input("Enter the book name: ")
            Admin.removebook(bn4)
    if (a==3):
        Library.seebooks()
    p= int(input("Enter 1 to exit: "))
    if p==1:
        break
    else:
        pass


