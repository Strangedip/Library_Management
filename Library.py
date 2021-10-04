# the library and management

# for book renting function

def rentBook():

    b = input("Enter the name of the Book you need : ")

 # read library.txt for the name user entered

    with open('library.txt', 'r') as f:
        books = f.read()

    with open('rented.txt', 'r') as g:
        rbooks=g.read()

 # if name is present in txt file remove that name from library and add it to rented.txt file

        if b in books :
            print(f"you have rented the '{b}' book\nDo return within 15 days")

            nl = books.replace(b, "")

            with open('library.txt', 'w') as g:
                g.write(nl)

            with open('rented.txt', 'a') as g:
                g.write(b+"\n")

        elif b in rbooks:
            print(f"'{b}' book is already rented by someone")

        else:
            print(f"'{b}' is not present in library")

            ans = input(
                f"Do you want to add '{b}' book in the library\nYes(y) or No(n)? :")

            if ans == "y":
                with open('library.txt', 'a') as g:
                    g.write(b)

                print(f"'{b}' book is added in the library")

            elif ans == "n":
                print("Do visit again, have a great day !")

            else:
                print("choose correct option")


# for new book adding function
def addBook():
    b = input("Enter the name of the new book you want to add : ")

 # read rented and library file for the presence of name of new book
    with open('library.txt', 'r') as f:
        books = f.read()
    with open('rented.txt', 'r') as g:
        rbooks = g.read()

 # if new book name is present in wither of file dont add
    if (b in books) or (b in rbooks):
        print(f"'{b}' book already exists in the library")

 # else add new book in the library
    else:
        with open('library.txt', 'a') as f:
            books = f.write(b+"\n")
        print(f"'{b}' book has been added to the library")


# for book returning function

def returnBook():
    b = input("Enter the name of the book you want to return back : ")

 # read rented and library file for the presence of name of new book
    with open('rented.txt', 'r') as g:
        rbooks = g.read()

    with open('library.txt', 'r') as f:
        books = f.read()

 # if book name is present in library show book already is in library
    if (b in books):

        print(f"'{b}' book already exist in library Check the list!")

 # if book is present in rented file. remove book name from rented file add it to library file again
    elif b in rbooks:

        with open('library.txt', 'a') as f:
            f.write(b)

        with open('rented.txt', 'w') as f:
            nl=rbooks.replace(b, "")
            f.write(nl)
        print(f"'{b}' is returned, Do visit again!")




print("Enter your choice")

user = input(
    "1.Rent a book\n2.Add a new book\n3.Return the book\n4.Show Book list\n-> ")

if user == "1":
    rentBook()

elif user == "2":
    addBook()

elif user == "3":
    returnBook()

elif user == "4":

    with open('library.txt', 'r') as f:
        books = f.read()

    with open('rented.txt', 'r') as f:
        rbooks = f.read()
    u = input("which book list you want Rented(r) or Library (l) : ")

    if u == "l":
        print(f"Books present in library:\n{books}")

    elif u == "r":
        print(f"Rented Books:\n{rbooks}")

    else:
        print("please choose the correct option")


else:
    print("please choose the correct option")
