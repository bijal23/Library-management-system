class Library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print("we have following books in our library:"+ self.name)
        for book in self.bookList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            if book in self.bookList:
                self.lendDict.update({book:user})
                print("lender book has been updated.you can take the book now")
            else:
               print("Book is not in the List")
        else:
            print("Book is already being used by"+ self.lendDict[book])

    def addBook(self, book):
        self.bookList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)
        print("returned")

lib = Library(['PYTHON','PHP','C','CPP'],'Nirma')

while True:
    print("welcome to the library. Enter your choice to continue")
    print("1. Display Books")
    print("2. Issue a Book")
    print("3. add a Book")
    print("4. return a Book")
    user_choice = int(input('Enter Your choice : '))

    if user_choice == 1:
        lib.displayBooks()

    elif user_choice == 2:
        book = input("Enter the name of the book you want to lend : ")
        user = input("enter your name : ")
        lib.lendBook(user, book)

    elif user_choice == 3:
        book = input("Enter the name of the book you want to add : ")
        lib.addBook(book)

    elif user_choice == 4:
        book = input("Enter the name of the book you want to return : ")
        lib.returnBook(book)

    else:
        print("Not a valid option")

        print("Press q to quit and c to continue")

        user_choice2 = ""

        while user_choice2!= "c" and user_choice2!= "q":
            user_choice2 = input()

            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue