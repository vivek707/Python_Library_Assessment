# Existing Books in Library
list_of_books = ['Harry Potter','Madhushala','Nirmala']
book_info = {'Harry Potter':[1,'Harry Potter','JK Rowling','unassigned'],
'Madhushala':[2,'Madhushala','Harivansh Rai Bachan','unassigned'],
'Nirmala':[3,'Nirmala','Premchand','unassigned']
}

#Student class to request and return books from library
class Student:
    def requestBook(self):
        print("Enter the name of the book you'd like to borrow>>")
        self.book=input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book you'd like to return>>")
        self.book=input()
        return self.book


#Library class which helps students lend book, return book and display available books
class Library:
    assign_period = '2 Weeks'
    def __init__(self,listofbooks,book_info):#this init method is the first method to be invoked when you create an object
        #what attributes does a library in general have? - for now, let's abstract and just say it has listofbooks (we're not going to program the shelves, and walls in!)
        self.listofbooks=listofbooks
        self.book_info = book_info

    def display_allbooks(self):
        # print each data item.
        print('\nBelow are the books available in the library: ')
        for book in list_of_books:
            print(book)
        
    def lend_book(self,requestedBook):
        if requestedBook in self.listofbooks:
            self.listofbooks.remove(requestedBook)
            self.book_info[requestedBook][3] = 'assigned'
            print(f"The requested book has been assigned to you successfully for {self.assign_period}.")
        else:
            print("Sorry this book is not available in the library at present")

    def return_book(self,returnedBook):
        if returnedBook not in self.listofbooks:
            self.listofbooks.append(returnedBook)
            self.book_info[returnedBook][3] = 'unassigned'
            print("Thanks for returning your borrowed book")
        else:
            print(f"You don't own {returnedBook} so can't return it")


#Librarian class for admin actions such as adding, removing, updating status of books available in library
class Librarian:
    def __init__(self,listofbooks,book_info):#this init method is the first method to be invoked when you create an object
        #what attributes does a library in general have? - for now, let's abstract and just say it has listofbooks (we're not going to program the shelves, and walls in!)
        self.listofbooks=listofbooks
        self.book_info = book_info

    def add_book(self):
        self.book=input("Enter the name of the book you'd like to add to library: ")
        self.book_id=int(input("Enter the book ID: "))
        self.author=input("Enter the name of the author of this book: ")
        self.status=input("Enter the status of the book - assigned/unassigned: ")

        self.listofbooks.append(self.book)
        self.book_info[self.book] = [self.book_id,self.book,self.author,self.status]
        print(f"The book '{self.book}' has been added successfully")

    def delete_book(self):
        self.book=input("Enter the name of the book you'd like to delete from library: ")
        if self.book in list_of_books:
            self.listofbooks.remove(self.book)
            self.book_info.pop(self.book)
            print(f"The book '{self.book}' has been deleted successfully")
        else:
            print(f"The book '{self.book}' does not exists in the library. Please check lisf of available books")
        
    def book_information(self):
        self.book=input("Enter the name of the book you'd like to see details about: ")
        if self.book in book_info.keys():
            print('\nPlease find below the requested details: ')
            print(f'Book ID: {self.book_info[self.book][0]}')
            print(f'Book Name: {self.book_info[self.book][1]}')
            print(f'Book Author: {self.book_info[self.book][2]}')
            print(f'Book Status: {self.book_info[self.book][3]}')
        else:
            print(f"The book '{self.book}' does not exists in the library. Please check lisf of available books")

    def change_staus(self):
        self.book=input("Enter the name of the book you'd like to change status of: ")
        if self.book in book_info.keys():
            self.newstatus=input("Enter the new status - assigned/unassigned: ")
            if self.newstatus == self.book_info[self.book][3]:
                print(f'The status of the book is already {self.newstatus}')
            else:
                self.book_info[self.book][3] = self.newstatus
                print(f'The status of the book {self.book} has been changed successfully')
        else:
            print(f"The book '{self.book}' does not exists in the library")

def main():            
    
    library= Library(list_of_books,book_info)
    librarian = Librarian(list_of_books,book_info)
    student=Student()

    print("Welcome to the library management system")

    while True:
        print("-------------------------------------------")
        print("Enter 1. Enter as Student")
        print("Enter 2. Enter as Librarian")
        print("Enter 3. Exit from Program\n")
        main_choice = input("Enter Choice: ")
        
        if main_choice=='1':
            while True:
                print("-------------------------------------------")
                print("\nEnter 1. List of All Books")            
                print("Enter 2. To Borrow a Book")
                print("Enter 3. Return a Book")
                print("Enter 4. Exit to Main Menu\n")
                choice=input("Enter Choice: ")

                if choice=='1':
                    library.display_allbooks()
                elif choice=='2':
                    library.lend_book(student.requestBook())
                elif choice=='3':
                    library.return_book(student.returnBook())
                elif choice=='4':
                    break
                else:
                    print('Please choose wisely')
        elif main_choice=='2':
            while True:
                print("-------------------------------------------")
                print("\nEnter 1. Add a New Book")            
                print("Enter 2. Delete a Book")
                print("Enter 3. Information About Book")
                print("Enter 4. Change Book Status")
                print("Enter 5. Exit to Main Menu\n")
                choice=input("Enter Choice: ")

                if choice=='1':
                    librarian.add_book()
                elif choice=='2':
                    librarian.delete_book()
                elif choice=='3':
                    librarian.book_information()
                elif choice=='4':
                    librarian.change_staus()
                elif choice=='5':
                    break
                else:
                    print('Please choose wisely')
        elif main_choice=='3':
            break
        else:
            print('Please choose wisely')

try:
    main()
except KeyError as ke:
    print(f'The Book {ke} does not exists')
except Exception as e:
    print("Something Went Wrong! Please contact your admin.")
    print(f'Error Detail: {e}')