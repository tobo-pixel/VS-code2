import time
import random
from datetime import date,timedelta
import tkinter as tk
class Book:
    def __init__(self,title,author,isbn,copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = int(copies)


class Member:
    def __init__(self,first_name,last_name,member_id):
        self.first_name = first_name
        self.last_name = last_name
        self.member_id = member_id
        self.borrowed_books = {}
        self.borrowedbooks_history = {}
        self.fine = []
    def borrow_time(self,borrowedbook):
        # To keep track of when a book was borrowed and when it is to be returned
        time_borrowed = date.today()
        due_date = time_borrowed + timedelta(weeks=2)
        self.borrowed_books[borrowedbook] = [time_borrowed,due_date]

# ==== Library Data Storage ====
library_books = []  # To store all library books
members = []  # To store all members of the library
bank_accounts = {}  # Storage of account details for Tobo bank used to pay fines


def new_member(first_name,last_name):
    # Register new members
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    # Generate 6 digit membership id
    member_id = random.randint(100000,999999)
    used_id = True
    # Loops until a unique id is generated
    while used_id:
        for member in members:
            if member_id == member.member_id:
                member_id = random.randint(100000,999999)
                break
        else:
            used_id = False
    member1 = Member(first_name,last_name,member_id)
    members.append(member1)  # Adds the member object to the members list
    print(f"Congratulations {last_name.upper()} {first_name.upper()} you are now a member of Tobo library services\nYour membership id is {member_id}")


def is_member(memberid,function,title,author,isbn):
    # Confirms if someone is a member of the library or not
    for member in members:
        if member.member_id == memberid:
            print(f"Login successful for {member.last_name} {member.first_name}")
            function(title,author,isbn,memberid)
            break
    else:
        print("No Match")


def search_member(firstname,lastname):
    # Checking for a member using first name and last name
    for member in members:
        if member.first_name.lower() == firstname.lower() and member.last_name.lower() == lastname.lower():
            print(f"{member.last_name} {member.first_name} with member id {member.member_id}")
            print("Borrowed books:\n")
            is_book = 0
            for book,date in member.borrowed_books.items():
                print(f"{book.title} by {book.author} with ISBN {book.isbn} borrowed on {date[0]} due {date[1]}")
                is_book += 1
            for book,date in member.borrowedbooks_history.items():
                print(f"{book.title} by {book.author} with ISBN {book.isbn} borrowed on {date[0]} due {date[1]} and returned {date[2]}")
            if is_book == 0:
                print("No books borrowed")
                break
    else:
        print("No match")


def delete_member(first_name,last_name,member_id):
    # Removing members from the library
    for member in members:
        if member.first_name.lower() == first_name.lower() and member.last_name.lower() == last_name.lower() and member.member_id == member_id:
            # Checks if all borrowed books have been returned
            if member.borrowed_books != {}:
                print("You have to return all books to be able to delete membership")
                print("Return the following books:\n")
                for borrowedbook,date in member.borrowed_books.items():
                    print(f"{borrowedbook.title} by {borrowedbook.author} with ISBN {borrowedbook.isbn} due {date[1]}")
                break
            # Checks if there are unpaid fines for the member
            elif member.fine != []:
                print("You have to pay all fines to be able to delete membership")
                break
            else:
                members.remove(member)
                print("Membership successfully deleted")
                break
    else:
        print("Member not found")


def add_book(title,author,isbn,):
    # For adding a new book to the library
    input_copies = input("How many copies: ")
    book1 = Book(title,author,isbn,input_copies)
    for book in library_books:
        if book.title.lower() == title.lower() and book.author.lower() == author.lower() and book.isbn == isbn:
            print("This book is already in the library")
            break
    else:
        library_books.append(book1)
        print(f"{input_copies} copy(s) of {title} by {author} with isbn {isbn} has been successfully added to the library archives")


def show_books():
    # Displays all books in the library 
    for book in library_books:
        print(f"{book.copies} copy(s) of {book.title} by {book.author} with ISBN {book.isbn}")
        for member in members:
            for borrowedbook,date in member.borrowed_books.items():
                if borrowedbook == book:
                    print(f"{member.last_name} {member.first_name} borrowed a copy of {book.title} by {book.author} with ISBN {book.isbn} due {date[1]}")


def search(title,author,isbn):
    # To search for a book with at least one criteria(name,author or isbn)
    is_book = False
    for book in library_books:
        if book.title.lower() == title.lower() or book.author.lower() == author.lower() or book.isbn == isbn:
            is_book = True
            print(f"{book.copies} copy(s) of {book.title} by {book.author} with ISBN {book.isbn}")
            for member in members:
                for borrowedbook,date in member.borrowed_books.items():
                    if borrowedbook == book:
                        print(f"{member.last_name} {member.first_name} borrowed a copy of {book.title} by {book.author} with ISBN {book.isbn} due {date[1]}")
    if is_book == False:
        print("Book not found")


def borrow(title,author,isbn,memberid):
    # For borrowing books from the library
    book_found = False
    count = 0
    for book in library_books:
        if book.title.lower() == title.lower() and book.author.lower() == author.lower() and book.isbn == isbn:
            book_found = True
            for member in members:
                if memberid == member.member_id:
                    for borrowedbook in member.borrowed_books:
                        count += 1  # Checks number of unreturned books the member has borrowed
                    total_fine = sum(member.fine)
                    # Once fines has reached 3000 naira, borrowing of books isn`t allowed again
                    if total_fine >= 3000:
                        print("You cannot borrow a book because your fines has reached the 3000 naira limit")
                    # A member can only borrow 5 books at a time
                    elif count >= 5:
                        print("You cannot borrow more than 5 books at a time")
                    else:
                        if book.copies > 0:
                            print(f"You have successfully borrowed {book.title} by {book.author} with ISBN {book.isbn}\nYou are to return it in 2 weeks")
                            book.copies -= 1
                            member.borrow_time(book)
                        else:
                            print(f"All copies of {book.title} are currently borrowed")
                    break
            break
    if book_found == False:
        print("Book not found")


def return_book(title,author,isbn,memberid):
    # For returning borrowed books
    book_found = False
    for book in library_books:
        if book.title.lower() == title.lower() and book.author.lower() == author.lower() and book.isbn == isbn:
            book_found = True
            for member in members:
                if member.member_id == memberid:
                    if book in member.borrowed_books:
                        today_date = date.today()
                        book.copies += 1
                        member.borrowed_books[book].append(today_date)
                        if today_date < member.borrowed_books[book][1]:
                            print(f"You have successfully returned {book.title} by {book.author} with isbn {isbn}")
                        else:
                            days_difference = today_date - member.borrowed_books[book][1]
                            days_difference = days_difference.days
                            fine = 500 * days_difference  # 500 naira fine per day
                            print(f"This book was due on {member.borrowed_books[book][1]}\nYou are {days_difference} days late\nYour fine is {fine} naira")
                            member.fine.append(fine)
                        member.borrowedbooks_history[book] = member.borrowed_books.pop(book)
                    else:
                        print("You did not borrow this book")
                    break
            break
    if book_found == False:
        print("Book not found")


def check_ISBN(title,author,isbn,function):
    # ISBN is a unique 10 digit or 13 digit number for a book
    # This function checks if the ISBN is valid or not
    problems = True
    while problems:
        duplicate = 0
        for book in library_books:
            if book.isbn == isbn:
                duplicate += 1  # Checks if any other book in the library has the same ISBN
        value_error = 0
        try:
            int(isbn)  # Checks if the ISBN is a number
        except ValueError:
            value_error += 1 
        if len(isbn) != 10 and len(isbn) != 13:
            # Checks if the ISBN is 10 or 13 digits or not
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

# ==== THE MAIN PROGRAM LOOP ====
# while True:
#     print("Welcome to Tobo Library Services")
#     choice = input("What would you like to do\n1. Search a book\t2. Borrow a book\n3. Return a book\t4. Add a book(For admin only)\n5. Show all books\t6. Become a member\n7. Delete membership\t8. Search Member\n9. Payment of fine\n")
#     if choice == "1":
#         input_title = input("Name of book(If you can`t remember, you can leave it blank): ")
#         input_author = input(f"Author of {input_title}(If you can`t remember, you can leave it blank): ")
#         input_isbn = input(f"ISBN of {input_title}(If you can`t remember, you can leave it blank): ")
#         # CLEAN ISBN INPUT
#         # ISBN sometimes include dashes and spaces, so this removes them
#         isbn_nodashes = input_isbn.replace("-","") 
#         isbn_nospace = isbn_nodashes.replace(" ","") 
#         if input_title or input_author or isbn_nospace:
#             search(input_title,input_author,isbn_nospace)
#             time.sleep(5)
#         else:
#             print("Please enter at least one search criteria(name or author or isbn)")
#     elif choice == "2":
#         input_title = input("Name of book: ")
#         input_author = input(f"Author of {input_title}: ")
#         input_isbn = input(f"ISBN of {input_title}: ")
#         isbn_nodashes = input_isbn.replace("-","")
#         isbn_nospace = isbn_nodashes.replace(" ","")
#         try:
#             input_memberid = int(input("Member ID: "))
#         except ValueError:
#             print("Invalid input")
#             continue
#         is_member(input_memberid,borrow,input_title,input_author,isbn_nospace)
#         time.sleep(5)
#     elif choice == "3":
#         input_title = input("Name of book: ")
#         input_author = input(f"Author of {input_title}: ")
#         input_isbn = input(f"ISBN of {input_title}: ")
#         isbn_nodashes = input_isbn.replace("-","")
#         isbn_nospace = isbn_nodashes.replace(" ","")
#         try:
#             input_memberid = int(input("Member ID: "))
#         except ValueError:
#             print("Invalid input")
#             continue
#         is_member(input_memberid,return_book,input_title,input_author,isbn_nospace)
#         time.sleep(5)
#     elif choice == "4":
#         password = "AS13qYuP0"
#         input_password = input("What is the password: ")
#         if input_password == password:
#             input_title = input("Name of book: ")
#             input_author = input(f"Author of {input_title}: ")
#             input_isbn = input(f"ISBN of {input_title}: ")
#             isbn_nodashes = input_isbn.replace("-","")
#             isbn_nospace = isbn_nodashes.replace(" ","")
#             check_ISBN(input_title,input_author,isbn_nospace,add_book)
#             time.sleep(5)
#         else:
#             print("Incorrect password")
#     elif choice == "5":
#         show_books()
#         time.sleep(5)
#     elif choice == "6":
#         lastname = input("Your last name: ")
#         firstname = input("Your first name: ")
#         new_member(firstname,lastname)
#         time.sleep(7)
#     elif choice == "7":
#         lastname = input("Your last name: ")
#         firstname = input("Your first name: ")
#         try:
#             memberid = int(input("Your membership id: "))
#         except ValueError:
#             print("Invalid input")
#             continue
#         delete_member(firstname,lastname,memberid)
#         time.sleep(5)
#     elif choice == "8":
#         input_firstname = input("First Name: ")
#         input_lastname = input("Last name: ")
#         search_member(input_firstname,input_lastname)
#         time.sleep(7)
#     elif choice == "9":
#         print("Your payment would have to be done using Tobo bank")
#         try:
#             from Bank_app import bankapp
#             bankapp(bank_accounts)
#         except ImportError:
#             print("Bank app temporarily unavailable")
#     else:
#         print("Choose between the options below")
#         time.sleep(3)
