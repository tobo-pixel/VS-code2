def withdraw(balance,amount):
    if amount <= balance:
        new_balance = balance - amount
        print(new_balance)
    else:
        print("Insufficient balance")

withdraw(1200,300)
import time
import random
class Book:
    def __init__(self,title,author,isbn,copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
class Member:
    def __init__(self,first_name,last_name,member_id):
        self.first_name = first_name
        self.last_name = last_name
        self.member_id = member_id
        self.borrowed_books = []
library_books = []
members = []
def new_member(first_name,last_name):
    first_name = first_name.upper()
    last_name = last_name.upper()
    member_id = random.randint(100000,999999)
    used_id = True
    while used_id:
        count = 0
        for member in members:
            if member.member_id == member_id:
                member_id = random.randint(100000,999999)
                count += 1
        if count == 0:
            used_id = False
    member1 = Member(first_name,last_name,member_id)
    members.append(member1)
    print(f"Congratulations {last_name.upper()} {first_name.upper()} you are now a member of Tobo library servie\nYour membership id id {member_id}")
def delete_member(first_name,last_name,member_id):
    is_member = False
    for member in members:
        if member.first_name == first_name.upper() and member.last_name == last_name.upper() and member.member_id == member_id:
            members.remove(member)
            is_member = True
            print("Membership successfully deleted")
    if is_member == False:
        print("Member not found")
def add_book(title,author,isbn,copies):
    book1 = Book(title,author,isbn,copies)
    count = 0
    for book in library_books:
        if book.title.lower() == title.lower() and book.author.lower() == author.lower() and book.isbn == isbn:
            print("This book is already in the library")
            count += 1
    if count == 0:
        library_books.append(book1)
        print(f"{title} by {author} with isbn {isbn} has been successfully added to the library archives")
def show_books():
    for book in library_books:
        print(f"{book.title} by {book.author} with ISBN {book.isbn} and availability status {book.is_available}")
def search(title,author,isbn):
    for book in library_books:
        if book.title.lower() == title.lower() or book.author.lower() == author.lower() or book.isbn == isbn:
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"ISBN: {book.isbn}")
            print(f"Availability status: {book.is_available}")
        else:
            print("Book not found")
def borrow(title,author,isbn):
    for book in library_books:
        if book.title.lower() == title.lower() and book.author.lower() == author.lower() and book.isbn == isbn:
            if book.is_available == True:
                print(f"You have successfully borrowed {book.title} by {book.author} with ISBN {book.isbn}")
                book.is_available = False
            else:
                print("This book is currently borrowed")
        else:
            print("Book not found")
def return_book(title,author,isbn):
    for book in library_books:
        if book.title.lower() == title.lower() and book.author.lower() == author.lower() and book.isbn == isbn and book.is_available == False:
            print(f"You have successfully returned {book.title} by {book.author} with isbn {isbn}")
        elif book.title.lower() == title.lower() and book.author.lower() == author.lower() and book.isbn == isbn and book.is_available == True:
            print("This book was not borrowed")
        else:
            print("This book does not belong to the library")
def check_ISBN(title,author,isbn,function):
    problems = True
    while problems:
        duplicate = 0
        for book in library_books:
            if book.isbn == isbn:
                duplicate += 1
        value_error = 0
        try:
            int(isbn)
        except ValueError:
            value_error += 1
        if len(isbn) != 10 and len(isbn) != 13:
            print("Invalid ISBN\nISBN should have 10 or 13 digits")
            isbn = input(f"Input a valid isbn for {title}: ")
        elif value_error != 0:
            print("Invalid ISBN\nISBN should only have numbers")
            isbn = input(f"Input a valid isbn for {title}: ")
        elif duplicate != 0:
            print("Invalid ISBN\nDuplicate ISBN")
            isbn = input(f"Input a valid isbn for {title}: ")
        else:
            problems = False
    else:
            function(title,author,isbn)
            time.sleep(5)
while True:
    print("Welcome to Tobo Library Services")
    choice = input("What would you like to do\n1. Search a book\n2. Borrow a book\n3. Return a book\n4. Add a book\n5. Show all books\n6. Become a member\n7. Delete membership\n")
    if choice == "1":
        input_title = input("Name of book(If you can`t remember, you can leave it blank): ")
        input_author = input(f"Author of {input_title}(If you can`t remember, you can leave it blank): ")
        input_isbn = input(f"ISBN of {input_title}(If you can`t remember, you can leave it blank): ")
        isbn_nodashes = input_isbn.replace("-","")
        isbn_nospace = isbn_nodashes.replace(" ","")
        search(input_title,input_author,isbn_nospace)
        time.sleep(5)
    elif choice == "2":
        input_title = input("Name of book: ")
        input_author = input(f"Author of {input_title}: ")
        input_isbn = input(f"ISBN of {input_title}: ")
        isbn_nodashes = input_isbn.replace("-","")
        isbn_nospace = isbn_nodashes.replace(" ","")
        check_ISBN(input_title,input_author,isbn_nospace,borrow)
        time.sleep(5)
    elif choice == "3":
        input_title = input("Name of book: ")
        input_author = input(f"Author of {input_title}: ")
        input_isbn = input(f"ISBN of {input_title}: ")
        isbn_nodashes = input_isbn.replace("-","")
        isbn_nospace = isbn_nodashes.replace(" ","")
        check_ISBN(input_title,input_author,isbn_nospace,return_book)
        time.sleep(5)
    elif choice == "4":
        input_title = input("Name of book: ")
        input_author = input(f"Author of {input_title}: ")
        input_isbn = input(f"ISBN of {input_title}: ")
        input_copies = input(f"How many copies of {input_title}")
        isbn_nodashes = input_isbn.replace("-","")
        isbn_nospace = isbn_nodashes.replace(" ","")
        check_ISBN(input_title,input_author,isbn_nospace,add_book)
    elif choice == "5":
        show_books()
        time.sleep(5)
    elif choice == "6":
        lastname = input("Your last name: ")
        firstname = input("Your first name: ")
        new_member(firstname,lastname)
        time.sleep(5)
    elif choice == "7":
        lastname = input("Your last name: ")
        firstname = input("Your first name: ")
        memberid = input("Your membership id: ")
        delete_member(firstname,lastname,memberid)
        time.sleep(5)
    else:
        print("Choose between the 5 options below")
        time.sleep(3)