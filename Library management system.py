import time
import random
from datetime import date,timedelta,datetime
import tkinter as tk
from tkinter import messagebox
import csv
import os
class Book:
    def __init__(self,title,author,isbn,copies):
        self.title = title.strip().capitalize()
        self.author = author.strip().capitalize()
        self.isbn = isbn.strip()
        self.copies = int(copies)
        # Checks if the file already exists
        file_exists = os.path.exists("library_books.csv")
        with open("library_books.csv","a",newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Title","Author","ISBN","Copies"])
            writer.writerow([self.title,self.author,self.isbn,self.copies])


class Member:
    def __init__(self,first_name,last_name,member_id):
        self.first_name = first_name.strip().capitalize()
        self.last_name = last_name.strip().capitalize()
        self.member_id = member_id
        file_exists = os.path.exists("library_members.csv")
        with open("library_members.csv","a",newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Firstname","Lastname","Member ID"])
            writer.writerow([self.first_name,self.last_name,self.member_id])

def fines(memberid,fine):
    file_exists = os.path.exists("member_fines.csv")
    with open("member_fines.csv","a",newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Member ID","Fine"])
        writer.writerow([memberid,fine])

def borrow_time(memberid,book_title,book_author,book_isbn):
    # To keep track of when a book was borrowed and when it is to be returned
    time_borrowed = date.today()
    due_date = time_borrowed + timedelta(weeks=2)
    file_exists = os.path.exists("borrowed_books.csv")
    with open("borrowed_books.csv","a",newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Member ID","Book Title","Book Author","Book ISBN","Date Borrowed","Due Date","Date Returned"])
        writer.writerow([memberid,book_title,book_author,book_isbn,str(time_borrowed),due_date,"Not Returned"])


def backbutton_function():
    for widget in content_frame.winfo_children():
        widget.destroy()
    content_frame.pack_forget()
    button_frame.pack()


def new_member(first_name,last_name):
    # Register new members
    # Generate 6 digit membership id
    member_id = random.randint(100000,999999)
    used_id = True
    # Loops until a unique id is generated
    while used_id:
        used_id = False
        file_exists = os.path.exists("library_members.csv")
        if not file_exists:
            text1 = tk.Text(content_frame,height=2,width=30)
            text1.insert("end","No Library Members yet\nWould you like to be the first")
            text1.grid(row=0,column=0)
            used_id =  False
            break
        with open("library_members.csv","r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if member_id == int(row[2]):
                    used_id = True
            if used_id == True:
                member_id = random.randint(100000,999999)
            else:
                used_id = False
    member1 = Member(first_name,last_name,member_id)
    text = tk.Text(content_frame,height=2,width=100)
    text.insert("1.0",f"Congratulations {last_name.upper()} {first_name.upper()} you are now a member of Tobo library services\nYour membership id is {member_id}")
    text.grid(row=0,column=0)


def is_member(memberid,function,title,author,isbn):
    # Confirms if someone is a member of the library or not
    file_exists = os.path.exists("library_members.csv")
    if not file_exists:
        text1 = tk.Text(content_frame,height=2,width=30)
        text1.insert("end","No Library Members yet\nWould you like to be the first")
        text1.grid(row=0,column=0)
        return
    with open("library_members.csv","r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if int(row[2]) == memberid:
                function(title,author,isbn,memberid)
                break
        else:
            text = tk.Text(content_frame)
            text.insert("1.0","No Match for this ID")
            text.grid(row=0,column=0)


def search_member(firstname,lastname):
    # Checking for a member using first name and last name
    firstname = firstname.strip()
    lastname = lastname.strip()
    file_exists = os.path.exists("library_members.csv")
    if not file_exists:
        text1 = tk.Text(content_frame,height=2,width=30)
        text1.insert("end","No Library Members yet\nWould you like to be the first")
        text1.grid(row=0,column=0)
        return
    with open("library_members.csv","r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0].lower() == firstname.lower() and row[1].lower() == lastname.lower():
                text = tk.Text(content_frame)
                text.insert("end",f"{row[1]} {row[0]} with member id {row[2]}\n")
                text.insert("end","Borrowed books:\n")
                text.grid(row=0,column=0)
                v_scroll = tk.Scrollbar(content_frame,orient="vertical",command=text.yview)
                v_scroll.grid(row=0,column=1,sticky="ns")
                h_scroll = tk.Scrollbar(content_frame,orient="horizontal",command=text.xview)
                h_scroll.grid(row=1,column=0,sticky="ew")
                text.config(yscrollcommand=v_scroll.set,xscrollcommand=h_scroll.set)
                is_book = 0
                file_exists = os.path.exists("borrowed_books.csv")
                if not file_exists:
                    text1 = tk.Text(content_frame,height=1,width=30)
                    text1.insert("end","No Books have been borrowed yet")
                    text1.grid(row=0,column=0)
                    return
                with open("borrowed_books.csv","r") as f:
                    borrowedbook_reader = csv.reader(f)
                    next(borrowedbook_reader)
                    for borrowedbook_row in borrowedbook_reader:
                        if borrowedbook_row[0] == row[2]:
                            text.insert("end",f"{borrowedbook_row[1]} by {borrowedbook_row[2]} with ISBN {borrowedbook_row[3]} borrowed on {borrowedbook_row[4]} due {borrowedbook_row[5]}\nRETURN STATUS:{borrowedbook_row[6]}\n")
                            is_book += 1
                    if is_book == 0:
                        text.insert("end","No books borrowed")
                        break
                    else:
                        break
        else:
            text2 = tk.Text(content_frame,height=1,width=10)
            text2.insert("end","No match")
            text2.grid(row=0,column=0)


def delete_member(first_name,last_name,member_id):
    problem = False
    match = False
    # Removing members from the library
    first_name = first_name.strip()
    last_name = last_name.strip()
    file_exists = os.path.exists("library_members.csv")
    if not file_exists:
        text1 = tk.Text(content_frame,height=2,width=30)
        text1.insert("end","No Library Members yet\nWould you like to be the first")
        text1.grid(row=0,column=0)
        return
    with open("library_members.csv","r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0].lower() == first_name.lower() and row[1].lower() == last_name.lower() and row[2] == str(member_id):
                match = True
                # Checks if all borrowed books have been returned
                file_exists = os.path.exists("borrowed_books.csv")
                if not file_exists:
                    pass
                else:
                    text = tk.Text(content_frame)
                    text.insert("end","You have to return all books to be able to delete membership\n")
                    text.insert("end","Return the following books:\n")
                    text.grid(row=0,column=0)
                    with open("borrowed_books.csv","r") as f:
                        borrowedbook_reader = csv.reader(f)
                        next(borrowedbook_reader)
                        for borrowedbook_row in borrowedbook_reader:
                            if row[2] == borrowedbook_row[0] and borrowedbook_row[6] == "Not Returned":
                                text.insert("end",f"{borrowedbook_row[1]} by {borrowedbook_row[2]} with ISBN {borrowedbook_row[3]} due {borrowedbook_row[5]}\n")
                                problem = True
                    # Checks if there are unpaid fines for the member
                if not problem:
                        print("here")
                        file_exists2 = os.path.exists("member_fines.csv")
                        if not file_exists2:
                            pass
                        else:
                            with open("member_fines.csv","r") as f:
                                fine_reader = csv.reader(f)
                                next(fine_reader)
                                for fine_row in fine_reader:
                                    if fine_row[0] == row[2]:
                                        text = tk.Text(content_frame,height=1,width=55)
                                        text.insert("1.0","You have to pay all fines to be able to delete membership")
                                        text.grid(row=0,column=0)
                                        return
                        with open("library_members.csv","r") as f:
                            reader2 = csv.reader(f)
                            rows = list(reader2)  # Convert to list
                        wanted_rows = []  # List to store all the rows we don't want to delete
                        found = False
                        for row in rows:
                            if row[2] != str(member_id):
                                wanted_rows.append(row)  # Adds rows that don't match to the list
                            else:
                                found = True  # Don't add the row to the list
                        if not found:
                            text1 = tk.Text(content_frame,height=1,width=20)
                            text1.insert("end","1.0","Member not found")
                            text1.grid(row=0,column=0)
                            return
                        with open("library_members.csv","w",newline="") as f:
                            writer = csv.writer(f)
                            writer.writerows(wanted_rows)
                        text = tk.Text(content_frame,height=1,width=55)
                        text.insert("1.0","Membership successfully deleted")
                        text.grid(row=0,column=0)
                        break
        if not match:
            text1 = tk.Text(content_frame,height=1,width=20)
            text1.insert("end","Member not found")
            text1.grid(row=0,column=0)
                
def edit_book(title,author,isbn,widget1_function,widget2_function,button_function):
    title = title.strip()
    author = author.strip()
    isbn = isbn.strip()
    book_found = False
    with open("library_books.csv","r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0].lower() == title.lower() and row[1].lower() == author.lower() and row[2] == isbn:
                book_found = True
                def edittile_function():
                    for widget in content_frame.winfo_children():
                        widget.destroy()
                    back_button3 = tk.Button(content_frame,text="<- BACK TO EDIT OPTIONS MENU",command=backbutton3_function)
                    back_button3.grid(row=5,column=0)
                    back_button2 = tk.Button(content_frame,text="<- BACK TO EDIT BOOK MENU",command=widget2_function)
                    back_button2.grid(row=6,column=0)
                    back_button4 = tk.Button(content_frame,text="<-BACK TO ADMIN OPTIONS",command=button_function)
                    back_button4.grid(row=6,column=2)
                    back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
                    back_button.grid(row=7,column=0)

                    title_label = tk.Label(content_frame,text="The new title:")
                    title_label.grid(row=0,column=0)
                    inputtitle = tk.Entry(content_frame)
                    inputtitle.grid(row=0,column=1)
                    function_button1 = tk.Button(content_frame,text="SUBMIT",command=lambda:edit_title(inputtitle,title_label,function_button1))
                    function_button1.grid(row=1,column=1)
                def edit_title(input_title,widget1,widget2):
                    nonlocal title
                    input_title.grid_forget()
                    widget1.grid_forget()
                    widget2.grid_forget()
                    input_title = input_title.get().strip()
                    file_exists = os.path.exists("borrowed_books.csv")
                    if file_exists:
                        with open("borrowed_books.csv","r") as f:
                            borrowedbook_reader = csv.reader(f)
                            borrowedbook_rows = list(borrowedbook_reader)
                            for borrowedbook_row in borrowedbook_rows:
                                if borrowedbook_row[3] == isbn:
                                    borrowedbook_row[1] = input_title.capitalize()
                        with open("borrowed_books.csv","w",newline="") as f:
                            writer = csv.writer(f)
                            writer.writerows(borrowedbook_rows)
                    match = False
                    with open("library_books.csv","r") as f:
                        title_reader = csv.reader(f)
                        title_rows = list(title_reader)
                    for title_row in title_rows:
                        if title_row[0].lower() == title.lower() and title_row[1].lower() == author.lower() and title_row[2] == isbn:
                            match = True
                            title_row[0] = input_title.capitalize()
                            title = input_title.capitalize()
                            text = tk.Text(content_frame)
                            text.insert("end",f"Successfully changed the Title to {input_title.capitalize()}")
                            text.grid(row=0,column=0)
                    if not match:
                        text = tk.Text(content_frame,height=1)
                        text.insert("1.0","Book not found")
                        text.grid(row=0,column=0)
                    with open("library_books.csv","w",newline="") as f:
                        writer = csv.writer(f)
                        writer.writerows(title_rows)
                    return
                def editauthor_function():
                    for widget in content_frame.winfo_children():
                        widget.destroy()
                    back_button3 = tk.Button(content_frame,text="<- BACK TO EDIT OPTIONS MENU",command=backbutton3_function)
                    back_button3.grid(row=5,column=0)
                    back_button2 = tk.Button(content_frame,text="<- BACK TO EDIT BOOK MENU",command=widget2_function)
                    back_button2.grid(row=6,column=0)
                    back_button4 = tk.Button(content_frame,text="<-BACK TO ADMIN OPTIONS",command=button_function)
                    back_button4.grid(row=6,column=2)
                    back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
                    back_button.grid(row=7,column=0)

                    author_label = tk.Label(content_frame,text="The new author:")
                    author_label.grid(row=0,column=0)
                    inputauthor = tk.Entry(content_frame)
                    inputauthor.grid(row=0,column=1)
                    function_button2 = tk.Button(content_frame,text="SUBMIT",command=lambda:edit_author(inputauthor,author_label,function_button2))
                    function_button2.grid(row=1,column=1)
                def edit_author(input_author,widget1,widget2):
                    nonlocal author
                    input_author.grid_forget()
                    widget1.grid_forget()
                    widget2.grid_forget()
                    input_author = input_author.get().strip()
                    file_exists = os.path.exists("borrowed_books.csv")
                    if file_exists:
                        with open("borrowed_books.csv","r") as f:
                            borrowedbook_reader = csv.reader(f)
                            borrowedbook_rows = list(borrowedbook_reader)
                            for borrowedbook_row in borrowedbook_rows:
                                if borrowedbook_row[3] == isbn:
                                    borrowedbook_row[2] = input_author.capitalize()
                        with open("borrowed_books.csv","w",newline="") as f:
                            writer = csv.writer(f)
                            writer.writerows(borrowedbook_rows)
                    match = False
                    with open("library_books.csv","r") as f:
                        author_reader = csv.reader(f)
                        author_rows = list(author_reader)
                    for author_row in author_rows:
                        if author_row[0].lower() == title.lower() and author_row[1].lower() == author.lower() and author_row[2] == isbn:
                            match = True
                            author_row[1] = input_author.capitalize()
                            author = input_author.capitalize()
                            text = tk.Text(content_frame)
                            text.insert("end",f"Successfully changed the Author to {input_author.capitalize()}")
                            text.grid(row=0,column=0)
                    if not match:
                        text = tk.Text(content_frame,height=1)
                        text.insert("1.0","Book not found")
                        text.grid(row=0,column=0)
                    with open("library_books.csv","w",newline="") as f:
                        writer = csv.writer(f)
                        writer.writerows(author_rows)
                    return
                def editisbn_function():
                    for widget in content_frame.winfo_children():
                        widget.destroy()
                    back_button3 = tk.Button(content_frame,text="<- BACK TO EDIT OPTIONS MENU",command=backbutton3_function)
                    back_button3.grid(row=5,column=0)
                    back_button2 = tk.Button(content_frame,text="<- BACK TO EDIT BOOK MENU",command=widget2_function)
                    back_button2.grid(row=6,column=0)
                    back_button4 = tk.Button(content_frame,text="<-BACK TO ADMIN OPTIONS",command=button_function)
                    back_button4.grid(row=6,column=2)
                    back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
                    back_button.grid(row=7,column=0)

                    isbn_label = tk.Label(content_frame,text="The new ISBN:")
                    isbn_label.grid(row=0,column=0)
                    inputisbn = tk.Entry(content_frame)
                    inputisbn.grid(row=0,column=1)
                    function_button3 = tk.Button(content_frame,text="SUBMIT",command=lambda:edit_isbn(inputisbn,isbn_label,function_button3,function_button3))
                    function_button3.grid(row=1,column=1)
                def edit_isbn(input_isbn,widget1,widget2,widget3):
                    nonlocal isbn
                    input_isbn.grid_forget()
                    widget1.grid_forget()
                    widget2.grid_forget()
                    widget3.grid_forget()
                    input_isbn = input_isbn.get().strip()
                    problems = True
                    duplicate = 0
                    file_exists = os.path.exists("library_books.csv")
                    if file_exists:
                        with open("library_books.csv","r") as f:
                            book_reader = csv.reader(f)
                            for book_row in book_reader:
                                if book_row[2] == input_isbn:
                                    duplicate += 1  # Checks if any other book in the library has the same ISBN
                    value_error = 0
                    try:
                        int(input_isbn)  # Checks if the ISBN is a number
                    except ValueError:
                        value_error += 1 
                    text1 = tk.Text(content_frame,height=2,width=34)
                    text2 = tk.Text(content_frame,height=1,width=25)
                    isbn_entry = tk.Entry(content_frame)
                    button = tk.Button(content_frame,text="SUBMIT",command=lambda:edit_isbn(isbn_entry,text1,text2,button))
                    if len(input_isbn) != 10 and len(input_isbn) != 13:
                        # Checks if the ISBN is 10 or 13 digits or not
                        text1.delete("1.0","end")
                        text1.insert("1.0","Invalid ISBN\nISBN should have 10 or 13 digits")
                        text1.grid(row=0,column=0)
                        text2.delete("1.0","end")
                        text2.insert("1.0",f"Input a valid isbn for {title}:")
                        text2.grid(row=1,column=0)
                        isbn_entry.grid(row=1,column=1)
                        button.grid(row=3,column=1)
                    elif value_error != 0:
                        text1.delete("1.0","end")
                        text1.insert("1.0","Invalid ISBN\nISBN should only have numbers")
                        text1.grid(row=0,column=0)
                        text2.delete("1.0","end")
                        text2.insert("1.0",f"Input a valid isbn for {title}:")
                        text2.grid(row=1,column=0)
                        isbn_entry.grid(row=1,column=1)
                        button.grid(row=3,column=1)
                    elif duplicate != 0:
                        text1.delete("1.0","end")
                        text1.insert("1.0","Invalid ISBN\nDuplicate ISBN")
                        text1.grid(row=0,column=0)
                        text2.delete("1.0","end")
                        text2.insert("1.0",f"Input a valid isbn for {title}:")
                        text2.grid(row=1,column=0)
                        isbn_entry.grid(row=1,column=1)
                        button.grid(row=3,column=1)
                    else:
                        file_exists = os.path.exists("borrowed_books.csv")
                        if file_exists:
                            with open("borrowed_books.csv","r") as f:
                                borrowedbook_reader = csv.reader(f)
                                borrowedbook_rows = list(borrowedbook_reader)
                                for borrowedbook_row in borrowedbook_rows:
                                    if borrowedbook_row[3] == isbn:
                                        borrowedbook_row[3] = input_isbn.capitalize()
                            with open("borrowed_books.csv","w",newline="") as f:
                                writer = csv.writer(f)
                                writer.writerows(borrowedbook_rows)
                        match = False
                        with open("library_books.csv","r") as f:
                            isbn_reader = csv.reader(f)
                            isbn_rows = list(isbn_reader)
                        for isbn_row in isbn_rows:
                            if isbn_row[0].lower() == title.lower() and isbn_row[1].lower() == author.lower() and isbn_row[2] == isbn:
                                match = True
                                isbn_row[2] = input_isbn
                                isbn = input_isbn
                                text = tk.Text(content_frame)
                                text.insert("end",f"Successfully changed the ISBN to {input_isbn}")
                                text.grid(row=0,column=0)
                        if not match:
                            text = tk.Text(content_frame,height=1)
                            text.insert("1.0","Book not found")
                            text.grid(row=0,column=0)
                        with open("library_books.csv","w",newline="") as f:
                            writer = csv.writer(f)
                            writer.writerows(isbn_rows)
                        return
                def addcopy_function():
                    for widget in content_frame.winfo_children():
                        widget.destroy()
                    back_button3 = tk.Button(content_frame,text="<- BACK TO EDIT OPTIONS MENU",command=backbutton3_function)
                    back_button3.grid(row=5,column=0)
                    back_button2 = tk.Button(content_frame,text="<- BACK TO EDIT BOOK MENU",command=widget2_function)
                    back_button2.grid(row=6,column=0)
                    back_button4 = tk.Button(content_frame,text="<-BACK TO ADMIN OPTIONS",command=button_function)
                    back_button4.grid(row=6,column=2)
                    back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
                    back_button.grid(row=7,column=0)

                    addcopy_label = tk.Label(content_frame,text="How many copies:")
                    addcopy_label.grid(row=0,column=0)
                    inputcopy = tk.Entry(content_frame)
                    inputcopy.grid(row=0,column=1)
                    function_button4 = tk.Button(content_frame,text="SUBMIT",command=lambda:add_copies(inputcopy,addcopy_label,function_button4))
                    function_button4.grid(row=1,column=1)
                def add_copies(input_copies,widget1,widget2):
                    input_copies.grid_forget()
                    widget1.grid_forget()
                    widget2.grid_forget()
                    try:
                        input_copies = int(input_copies.get().strip())
                    except ValueError:
                        text = tk.Text(content_frame)
                        text.insert("end","Invalid Input")
                        text.grid(row=0,column=0)
                        return
                    match = False
                    with open("library_books.csv","r") as f:
                        addcopy_reader = csv.reader(f)
                        addcopy_rows = list(addcopy_reader)
                    for addcopy_row in addcopy_rows:
                        if addcopy_row[0].lower() == title.lower() and addcopy_row[1].lower() == author.lower() and addcopy_row[2] == isbn:
                            match = True
                            addcopy_row[3] = int(addcopy_row[3]) + input_copies
                            text = tk.Text(content_frame)
                            text.insert("end",f"Successfully added {input_copies} copies of {title.capitalize()}")
                            text.grid(row=0,column=0)
                    if not match:
                        text = tk.Text(content_frame,height=1)
                        text.insert("1.0","Book not found")
                        text.grid(row=0,column=0)
                    with open("library_books.csv","w",newline="") as f:
                        writer = csv.writer(f)
                        writer.writerows(addcopy_rows)
                    return
                def deletecopy_function():
                    for widget in content_frame.winfo_children():
                        widget.destroy()
                    back_button3 = tk.Button(content_frame,text="<- BACK TO EDIT OPTIONS MENU",command=backbutton3_function)
                    back_button3.grid(row=5,column=0)
                    back_button2 = tk.Button(content_frame,text="<- BACK TO EDIT BOOK MENU",command=widget2_function)
                    back_button2.grid(row=6,column=0)
                    back_button4 = tk.Button(content_frame,text="<-BACK TO ADMIN OPTIONS",command=button_function)
                    back_button4.grid(row=6,column=2)
                    back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
                    back_button.grid(row=7,column=0)

                    delcopy_label = tk.Label(content_frame,text="How many copies:")
                    delcopy_label.grid(row=0,column=0)
                    inputcopy = tk.Entry(content_frame)
                    inputcopy.grid(row=0,column=1)
                    function_button5 = tk.Button(content_frame,text="SUBMIT",command=lambda:delete_copies(inputcopy,delcopy_label,function_button5))
                    function_button5.grid(row=1,column=1)
                def delete_copies(input_copies,widget1,widget2):
                    input_copies.grid_forget()
                    widget1.grid_forget()
                    widget2.grid_forget()
                    try:
                        input_copies = int(input_copies.get().strip())
                    except ValueError:
                        text = tk.Text(content_frame)
                        text.insert("end","Invalid Input")
                        text.grid(row=0,column=0)
                        return
                    match = False
                    with open("library_books.csv","r") as f:
                        delcopy_reader = csv.reader(f)
                        delcopy_rows = list(delcopy_reader)
                    for delcopy_row in delcopy_rows:
                        if delcopy_row[0].lower() == title.lower() and delcopy_row[1].lower() == author.lower() and delcopy_row[2] == isbn:
                            match = True
                            if int(delcopy_row[3]) >= input_copies:
                                delcopy_row[3] = int(delcopy_row[3]) - input_copies
                                text = tk.Text(content_frame)
                                text.insert("end",f"Sucessfully removed {input_copies} copies of {title.capitalize()}")
                                text.grid(row=0,column=0)
                            else:
                                text = tk.Text(content_frame)
                                text.insert("end",f"You can't delete more than the available copies of the book")
                                text.grid(row=0,column=0)
                    if not match:
                        text = tk.Text(content_frame,height=1)
                        text.insert("1.0","Book not found")
                        text.grid(row=0,column=0)
                    with open("library_books.csv","w",newline="") as f:
                        writer = csv.writer(f)
                        writer.writerows(delcopy_rows)
                    return
                def delete_book():
                    for widget in content_frame.winfo_children():
                        widget.destroy()
                    back_button3 = tk.Button(content_frame,text="<- BACK TO EDIT OPTIONS MENU",command=backbutton3_function)
                    back_button3.grid(row=5,column=0)
                    back_button2 = tk.Button(content_frame,text="<- BACK TO EDIT BOOK MENU",command=widget2_function)
                    back_button2.grid(row=6,column=0)
                    back_button4 = tk.Button(content_frame,text="<-BACK TO ADMIN OPTIONS",command=button_function)
                    back_button4.grid(row=6,column=2)
                    back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
                    back_button.grid(row=7,column=0)

                    borrowed = False
                    with open("borrowed_books.csv","r") as f:
                        borrowedbook_reader = csv.reader(f)
                        next(borrowedbook_reader)
                        for borrowedbook_row in borrowedbook_reader:
                            if borrowedbook_row[3] == isbn and borrowedbook_row[6] == "Not Returned":
                                text = tk.Text(content_frame)
                                text.insert("end","You can't delete this book because all copies haven't been returned yet")
                                text.grid(row=0,column=0)
                                borrowed = True
                    match = False
                    if not borrowed:
                        wanted_rows = []
                        with open("library_books.csv","r") as f:
                            delbook_reader = csv.reader(f)
                            delbook_rows = list(delbook_reader)
                        for delbook_row in delbook_rows:
                            if delbook_row[0].lower() == title.lower() and delbook_row[1].lower() == author.lower() and delbook_row[2] == isbn:
                                match = True
                                text = tk.Text(content_frame)
                                text.insert("end",f"Successfully deleted {title.capitalize()}")
                                text.grid(row=0,column=0)
                                pass
                            else:
                                wanted_rows.append(delbook_row)
                        if not match:
                            text = tk.Text(content_frame,height=1)
                            text.insert("1.0","Book not found")
                            text.grid(row=0,column=0)
                        with open("library_books.csv","w",newline="") as f:
                            writer = csv.writer(f)
                            writer.writerows(wanted_rows)
                        return
                question_label = tk.Label(content_frame,text="What would you like to do?")
                question_label.grid(row=0,column=0)
                edittitle_button = tk.Button(content_frame,text="1. EDIT TITLE",command=edittile_function)
                edittitle_button.grid(row=1,column=0,pady=5,padx=10)
                editauthor_button = tk.Button(content_frame,text="2. EDIT AUTHOR",command=editauthor_function)
                editauthor_button.grid(row=1,column=1,pady=5)
                editisbn_button = tk.Button(content_frame,text="3. EDIT ISBN",command=editisbn_function)
                editisbn_button.grid(row=2,column=0,pady=5,padx=10)
                addcopy_button = tk.Button(content_frame,text="4. ADD COPY(IES)",command=addcopy_function)
                addcopy_button.grid(row=2,column=1,pady=5)
                deletecopy_button = tk.Button(content_frame,text="5. DELETE COPY(IES)",command=deletecopy_function)
                deletecopy_button.grid(row=3,column=0,pady=5,padx=10)
                deletebook_button = tk.Button(content_frame,text="6. DELETE THE BOOK",command=delete_book)
                deletebook_button.grid(row=3,column=1,pady=5)

                def backbutton3_function():
                    for widget in content_frame.winfo_children():
                        widget.destroy()
                    question_label = tk.Label(content_frame,text="What would you like to do?")
                    question_label.grid(row=0,column=0)
                    edittitle_button = tk.Button(content_frame,text="1. EDIT TITLE",command=edittile_function)
                    edittitle_button.grid(row=1,column=0,pady=5,padx=10)
                    editauthor_button = tk.Button(content_frame,text="2. EDIT AUTHOR",command=editauthor_function)
                    editauthor_button.grid(row=1,column=1,pady=5)
                    editisbn_button = tk.Button(content_frame,text="3. EDIT ISBN",command=editisbn_function)
                    editisbn_button.grid(row=2,column=0,pady=5,padx=10)
                    addcopy_button = tk.Button(content_frame,text="4. ADD COPY(IES)",command=addcopy_function)
                    addcopy_button.grid(row=2,column=1,pady=5)
                    deletecopy_button = tk.Button(content_frame,text="5. DELETE COPY(IES)",command=deletecopy_function)
                    deletecopy_button.grid(row=3,column=0,pady=5,padx=10)
                    deletebook_button = tk.Button(content_frame,text="6. DELETE THE BOOK",command=delete_book)
                    deletebook_button.grid(row=3,column=1,pady=5)
                    back_button2 = tk.Button(content_frame,text="<- BACK TO EDIT BOOK MENU",command=widget2_function)
                    back_button2.grid(row=6,column=0)
                    back_button4 = tk.Button(content_frame,text="<-BACK TO ADMIN OPTIONS",command=button_function)
                    back_button4.grid(row=6,column=2)

                    back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
                    back_button.grid(row=7,column=0)




        if not book_found:
            text = tk.Text(content_frame)
            text.insert("end","Book not found")
            text.grid(row=0,column=0)

def add_book(title,author,isbn,):
    # For adding a new book to the library
    label = tk.Label(content_frame,text="How many copies:")
    label.grid(row=0,column=0)
    input_copies = tk.Entry(content_frame)
    input_copies.grid(row=0,column=1)
    def collected_inputs():
        label.grid_forget()
        button.grid_forget()
        try:
            copies = int(input_copies.get().strip())
        except ValueError:
            error_text = tk.Text(content_frame,height=1,width=25)
            error_text.insert("1.0","Invalid input")
            error_text.grid(row=0,column=0)
            return
        input_copies.grid_forget()
        duplicate = False
        file_exists = os.path.exists("library_books.csv")
        if file_exists:
            with open("library_books.csv","r") as f:
                reader = csv.reader(f)
                next(reader)  # Skips header
                for row in reader:
                    if row[0].lower() == title.strip().lower() and row[1].lower() == author.strip().lower() and row[2] == isbn.strip():
                        text = tk.Text(content_frame,height=1,width=34)
                        text.insert("1.0","This book is already in the library")
                        text.grid(row=0,column=0)
                        duplicate = True
                        break
        if not duplicate:
            book1 = Book(title,author,isbn,copies)
            text = tk.Text(content_frame,height=1,width=130)
            text.insert("1.0",f"{copies} copy(s) of {title.capitalize()} by {author.capitalize()} with isbn {isbn} has been successfully added to the library archives")
            text.grid(row=0,column=0)
    button = tk.Button(content_frame,text="SUBMIT",command=collected_inputs)
    button.grid(row=1,column=1)


def show_books():
    # Displays all books in the library
    text1 = tk.Text(content_frame) 
    text1.grid(row=0,column=0)
    v_scroll = tk.Scrollbar(content_frame,orient="vertical",command=text1.yview)
    v_scroll.grid(row=0,column=1,sticky="ns")
    h_scroll = tk.Scrollbar(content_frame,orient="horizontal",command=text1.xview)
    h_scroll.grid(row=1,column=0,sticky="ew")
    text1.config(yscrollcommand=v_scroll.set,xscrollcommand=h_scroll.set)
    file_exists = os.path.exists("library_books.csv")
    if not file_exists:
        text1.insert("end","No Books in Library yet")
        return
    with open("library_books.csv","r") as f:
        reader = csv.reader(f)
        next(reader)  # Skips header
        for row in reader:
            text1.insert("end",f"{row[3]} copy(s) of {row[0]} by {row[1]} with ISBN {row[2]}\n")
            file_exists = os.path.exists("library_members.csv")
            if not file_exists:
                continue
            with open("library_members.csv","r") as f:
                member_reader = csv.reader(f)
                next(member_reader)
                for member_row in member_reader:
                    file_exists = os.path.exists("borrowed_books.csv")
                    if not file_exists:
                        break
                    with open("borrowed_books.csv","r") as f:
                        borrowedbook_reader = csv.reader(f)
                        next(borrowedbook_reader)
                        for borrowedbook_row in borrowedbook_reader:
                            if borrowedbook_row[0] == member_row[2] and borrowedbook_row[3] == row[2] and borrowedbook_row[6] == "Not Returned" :
                                text1.insert("end",f"{member_row[1]} {member_row[0]} borrowed a copy of {row[0]} by {row[1]} with ISBN {row[2]} on {borrowedbook_row[4]} due {borrowedbook_row[5]}\n")
                    text1.insert("end","\n")  # Adds a blank line between books



def search(title,author,isbn):
    # To search for a book with at least one criteria(name,author or isbn)
    title = title.strip()
    author = author.strip()
    isbn = isbn.strip()
    is_book = False
    text1 = tk.Text(content_frame)
    text1.grid(row=0,column=0)
    v_scroll = tk.Scrollbar(content_frame,orient="vertical",command=text1.yview)
    v_scroll.grid(row=0,column=1,sticky="ns")
    h_scroll = tk.Scrollbar(content_frame,orient="horizontal",command=text1.xview)
    h_scroll.grid(row=1,column=0,sticky="ew")
    text1.config(yscrollcommand=v_scroll.set,xscrollcommand=h_scroll.set)
    file_exists = os.path.exists("library_books.csv")
    if not file_exists:
        text1.insert("end","No Books in Library yet")
        return
    with open("library_books.csv","r") as f:
        reader = csv.reader(f)
        next(reader)  # Skips header
        if (title or author) and (not isbn) and (not(title and author)):
            for row in reader:
                if row[0].lower() == title.lower() or row[1].lower() == author.lower() or row[2] == isbn:
                    is_book = True
                    text1.insert("end",f"{row[3]} copy(s) of {row[0]} by {row[1]} with ISBN {row[2]}\n")
                    with open("library_members.csv","r") as f:
                        member_reader = csv.reader(f)
                        next(member_reader)
                        for member_row in member_reader:
                            with open("borrowed_books.csv","r") as f:
                                borrowedbook_reader = csv.reader(f)
                                next(borrowedbook_reader)
                                for borrowedbook_row in borrowedbook_reader:
                                    if borrowedbook_row[3] == row[2] and borrowedbook_row[6] == "Not Returned" and borrowedbook_row[0] == member_row[2]:
                                        text1.insert("end",f"{member_row[1]} {member_row[0]} borrowed a copy of {row[0]} by {row[1]} with ISBN {row[2]} due {borrowedbook_row[5]}\n")
        elif isbn :
            for row in reader:
                if row[2] == isbn:
                    is_book = True
                    text1.insert("end",f"{row[3]} copy(s) of {row[0]} by {row[1]} with ISBN {row[2]}\n")
                    with open("library_members.csv","r") as f:
                        member_reader = csv.reader(f)
                        next(member_reader)
                        for member_row in member_reader:
                            with open("borrowed_books.csv","r") as f:
                                borrowedbook_reader = csv.reader(f)
                                next(borrowedbook_reader)
                                for borrowedbook_row in borrowedbook_reader:
                                    if borrowedbook_row[3] == row[2] and borrowedbook_row[6] == "Not Returned" and borrowedbook_row[0] == member_row[2]:
                                        text1.insert("end",f"{member_row[1]} {member_row[0]} borrowed a copy of {row[0]} by {row[1]} with ISBN {row[2]} due {borrowedbook_row[5]}\n")
        elif author and title and (not isbn):
            for row in reader:
                if row[0].lower() == title.lower() and row[1].lower() == author.lower():
                    is_book = True
                    text1.insert("end",f"{row[3]} copy(s) of {row[0]} by {row[1]} with ISBN {row[2]}\n")
                    with open("library_members.csv","r") as f:
                        member_reader = csv.reader(f)
                        next(member_reader)
                        for member_row in member_reader:
                            with open("borrowed_books.csv","r") as f:
                                borrowedbook_reader = csv.reader(f)
                                next(borrowedbook_reader)
                                for borrowedbook_row in borrowedbook_reader:
                                    if borrowedbook_row[3] == row[2] and borrowedbook_row[6] == "Not Returned" and borrowedbook_row[0] == member_row[2]:
                                        text1.insert("end",f"{member_row[1]} {member_row[0]} borrowed a copy of {row[0]} by {row[1]} with ISBN {row[2]} due {borrowedbook_row[5]}\n")
        else:
            text = tk.Text(content_frame,height=1)
            text.insert("1.0","Input at least one search criteria")
    if is_book == False:
        text3 = tk.Text(content_frame,height=1,width=15)
        text3.insert("1.0","Book not found")
        text3.grid(row=0,column=0)


def borrow(title,author,isbn,memberid):
    # For borrowing books from the library
    title = title.strip()
    author = author.strip()
    isbn = isbn.strip()
    book_found = False
    count = 0
    file_exists = os.path.exists("library_books.csv")
    if not file_exists:
        text1 = tk.Text(content_frame,height=1,width=30)
        text1.insert("end","No Books in Library yet")
        text1.grid(row=0,column=0)
        return
    with open("library_books.csv","r") as f:
        reader = csv.reader(f)
        next(reader)  # Skips header
        for row in reader:
            if row[0].lower() == title.lower() and row[1].lower() == author.lower() and row[2] == isbn:
                book_found = True
                with open("library_members.csv","r") as f:
                    member_reader = csv.reader(f)
                    next(member_reader)
                    for member_row in member_reader:
                        if memberid == int(member_row[2]):
                            file_exists = os.path.exists("borrowed_books.csv")
                            count = 0
                            member_exist = True
                            if not file_exists:
                                member_exist = False
                            if member_exist:
                                with open("borrowed_books.csv","r") as f:
                                    borrowedbook_reader = csv.reader(f)
                                    next(borrowedbook_reader)
                                    for borrowedbook_row in borrowedbook_reader:
                                        if borrowedbook_row[0] == str(memberid) and borrowedbook_row[6] == "Not Returned":
                                            count += 1  # Checks number of unreturned books the member has borrowed
                                            if borrowedbook_row[1].lower() == title.lower() and borrowedbook_row[2].lower() == author.lower() and borrowedbook_row[3] == isbn:
                                                error_text = tk.Text(content_frame,height=2,width=50)
                                                error_text.insert("end","You have borrowed this book already\nYou are only allowed to borrow 1 copy per book")
                                                error_text.grid(row=0,column=0)
                                                return
                            file_exists = os.path.exists("member_fines.csv")
                            fine_exist = True
                            total_fine = 0
                            if not file_exists:
                                fine_exist = False
                            if fine_exist:
                                total_fine = 0
                                with open("member_fines.csv","r") as f:
                                    fine_reader = csv.reader(f)
                                    next(fine_reader)
                                    for fine_row in fine_reader:
                                        if fine_row[0] == member_row[2]:
                                            total_fine = int(fine_row[1])
                            # Once fines has reached 3000 naira, borrowing of books isn`t allowed again
                            if total_fine >= 3000:
                                text = tk.Text(content_frame)
                                text.insert("1.0","You cannot borrow a book because your fines has reached the 3000 naira limit")
                                text.grid(row=0,column=0)
                            # A member can only borrow 5 books at a time
                            elif count >= 5:
                                text = tk.Text(content_frame)
                                text.insert("1.0","You cannot borrow more than 5 books at a time")
                                text.grid(row=0,column=0)
                            else:
                                if int(row[3]) > 0:
                                    text = tk.Text(content_frame)
                                    text.insert("1.0",f"You have successfully borrowed {row[0]} by {row[1]} with ISBN {row[2]}\nYou are to return it in 2 weeks")
                                    text.grid(row=0,column=0)
                                    with open("library_books.csv","r") as f:
                                        reader2 = csv.reader(f)
                                        rows = list(reader2)  # Convert to list
                                    for i in range(1,len(rows)):
                                        if rows[i][2] == row[2]:
                                            rows[i][3] = int(rows[i][3]) - 1
                                            break
                                    with open("library_books.csv","w",newline="") as f:
                                        writer = csv.writer(f)
                                        writer.writerows(rows)
                                    borrow_time(member_row[2],row[0],row[1],row[2])
                                else:
                                    text = tk.Text(content_frame)
                                    text.insert("1.0",f"No available copies of {row[0]}")
                                    text.grid(row=0,column=0)
                            break
                    break
    if book_found == False:
        text = tk.Text(content_frame)
        text.insert("1.0","Book not found")
        text.grid(row=0,column=0)


def return_book(title,author,isbn,memberid):
    # For returning borrowed books
    title = title.strip()
    author = author.strip()
    isbn = isbn.strip()
    file_exists = os.path.exists("library_books.csv")
    if not file_exists:
        text1 = tk.Text(content_frame,height=1,width=30)
        text1.insert("end","No Books in Library yet")
        text1.grid(row=0,column=0)
        return
    book_found = False
    with open("library_books.csv","r") as f:
        reader = csv.reader(f)
        next(reader)  # Skips header
        for row in reader:
            if row[0].lower() == title.lower() and row[1].lower() == author.lower() and row[2] == isbn:
                book_found = True
                file_exists = os.path.exists("library_members.csv")
                if not file_exists:
                    text1 = tk.Text(content_frame,height=1,width=30)
                    text1.insert("end","There are no library members\nYou could be the first")
                    text1.grid(row=0,column=0)
                    return
                with open("library_members.csv","r") as f:
                    member_reader = csv.reader(f)
                    next(member_reader)
                    for member_row in member_reader:
                        if int(member_row[2]) == memberid:
                            file_exists = os.path.exists("borrowed_books.csv")
                            if not file_exists:
                                text1 = tk.Text(content_frame,height=1,width=30)
                                text1.insert("end","No Books have been borrowed yet")
                                text1.grid(row=0,column=0)
                                return
                            with open("borrowed_books.csv","r") as f:
                                borrowedbook_reader = csv.reader(f)
                                next(borrowedbook_reader)
                                for borrowedbook_row in borrowedbook_reader:
                                    if (isbn == borrowedbook_row[3]) and (borrowedbook_row[6] == "Not Returned") and (memberid == int(borrowedbook_row[0])):
                                        today_date = date.today()
                                        with open("library_books.csv","r") as f:
                                                reader2 = csv.reader(f)
                                                rows = list(reader2)  # Convert to list
                                        for i in range(1,len(rows)):
                                            if rows[i][2] == row[2]:
                                                rows[i][3] = int(rows[i][3]) + 1
                                        with open("library_books.csv","w",newline="") as f:
                                            book_writer = csv.writer(f)
                                            book_writer.writerows(rows)
                                        with open("borrowed_books.csv","r") as f:
                                            reader3 = csv.reader(f)
                                            borrowedbook_row1 = list(reader3)
                                        for i in range(1,len(borrowedbook_row1)):
                                            if borrowedbook_row1[i][3] == row[2] and borrowedbook_row1[i][0] == str(memberid):
                                                borrowedbook_row1[i][6] = f"Returned on {str(date.today())}"
                                        with open("borrowed_books.csv","w",newline="") as f:
                                            borrowedbook_writer = csv.writer(f)
                                            borrowedbook_writer.writerows(borrowedbook_row1)
                                        due_date = datetime.strptime(borrowedbook_row[5],"%Y-%m-%d")
                                        due_date = due_date.date()
                                        if today_date < due_date:
                                            text = tk.Text(content_frame,height=1)
                                            text.insert("1.0",f"You have successfully returned {row[0]} by {row[1]} with isbn {row[2]}")
                                            text.grid(row=0,column=0)
                                        else:
                                            days_difference = today_date - due_date
                                            days_difference = days_difference.days
                                            fine = 500 * days_difference  # 500 naira fine per day
                                            text = tk.Text(content_frame,height=3)
                                            text.insert("1.0",f"This book was due on {borrowedbook_row[4]}\nYou are {days_difference} days late\nYour fine is {fine} naira")
                                            text.grid(row=0,column=0)
                                            fines(member_row[2],fine)
                                        break
                                else:
                                    text = tk.Text(content_frame,height=1,width=30)
                                    text.insert("1.0","You did not borrow this book")
                                    text.grid(row=0,column=0)
                        
    if book_found == False:
        text1 = tk.Text(content_frame,height=1,width=17)
        text1.insert("1.0","Book not found")
        text1.grid(row=0,column=0)


def check_ISBN(title,author,isbn,function,text1,text2,input_isbn,button):
    title = title.strip()
    author = author.strip()
    # If isbn is an entry widget, get the value. Otherwise use as it is
    if hasattr(isbn,"get"):
        isbn = isbn.get().strip()
    else:
        isbn = isbn.strip()
        pass
    # ISBN is a unique 10 digit or 13 digit number for a book
    # This function checks if the ISBN is valid or not
    problems = True
    duplicate = 0
    file_exists = os.path.exists("library_books.csv")
    if file_exists:
        with open("library_books.csv","r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[2] == isbn:
                    duplicate += 1  # Checks if any other book in the library has the same ISBN
    value_error = 0
    try:
        int(isbn)  # Checks if the ISBN is a number
    except ValueError:
        value_error += 1 
    if len(isbn) != 10 and len(isbn) != 13:
        # Checks if the ISBN is 10 or 13 digits or not
        text1.delete("1.0","end")
        text1.insert("1.0","Invalid ISBN\nISBN should have 10 or 13 digits")
        text1.grid(row=0,column=0)
        text2.delete("1.0","end")
        text2.insert("1.0",f"Input a valid isbn for {title}:")
        text2.grid(row=1,column=0)
        input_isbn.grid(row=1,column=1)
        button.grid(row=3,column=1)
    elif value_error != 0:
        text1.delete("1.0","end")
        text1.insert("1.0","Invalid ISBN\nISBN should only have numbers")
        text1.grid(row=0,column=0)
        text2.delete("1.0","end")
        text2.insert("1.0",f"Input a valid isbn for {title}:")
        text2.grid(row=1,column=0)
        input_isbn.grid(row=1,column=1)
        button.grid(row=3,column=1)
    elif duplicate != 0:
        text1.delete("1.0","end")
        text1.insert("1.0","Invalid ISBN\nDuplicate ISBN")
        text1.grid(row=0,column=0)
        text2.delete("1.0","end")
        text2.insert("1.0",f"Input a valid isbn for {title}:")
        text2.grid(row=1,column=0)
        input_isbn.grid(row=1,column=1)
        button.grid(row=3,column=1)
    else:
        text1.grid_forget()
        text2.grid_forget()
        input_isbn.grid_forget()
        button.grid_forget()
        function(title,author,isbn)


def searchbutton_function():  
    back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
    back_button.grid(row=6,column=0)
    button_frame.pack_forget()
    content_frame.pack()
    label1 = tk.Label(content_frame,text="Name of the book(If you can`t remember, you can leave it blank):",font=("arial",12))
    label1.grid(row=0,column=0)
    input_title = tk.Entry(content_frame)
    input_title.grid(row=0,column=1)

    label2 = tk.Label(content_frame,text="Author of the book(If you can`t remember, you can leave it blank):",font=("arial",12))
    label2.grid(row=1,column=0)
    input_author = tk.Entry(content_frame)
    input_author.grid(row=1,column=1)
    
    label3 = tk.Label(content_frame,text="ISBN of the book(If you can`t remember, you can leave it blank):",font=("arial",12))
    label3.grid(row=2,column=0)
    input_isbn = tk.Entry(content_frame)
    input_isbn.grid(row=2,column=1)
    
    def collected_inputs():
        # CLEAN ISBN INPUT
        # ISBN sometimes include dashes and spaces, so this removes them
        title = input_title.get()
        author = input_author.get()
        isbn = input_isbn.get()
        isbn_nodashes = isbn.replace("-","") 
        isbn_nospace = isbn_nodashes.replace(" ","")
        if title or author or isbn_nospace:
            input_author.grid_forget()
            input_title.grid_forget()
            input_isbn.grid_forget()
            label1.grid_forget()
            label2.grid_forget()
            label3.grid_forget()
            button_sb.grid_forget()

            def backbutton2_function():
                for widget in content_frame.winfo_children():
                    if widget == label1 or widget == label2 or widget == back_button or widget == input_title or widget == button_sb or widget == input_author or widget == label3 or widget == input_isbn :
                        pass
                    else:
                        widget.destroy()
                label1.grid(row=0,column=0)
                label2.grid(row=1,column=0)
                label3.grid(row=2,column=0)
                input_title.grid(row=0,column=1)
                input_author.grid(row=1,column=1)
                input_isbn.grid(row=2,column=1)
                button_sb.grid(row=3,column=2)
                back_button.grid(row=6,column=0)
            back_button2 = tk.Button(content_frame,text="<- BACK TO SEARCH BOOK MENU",command=backbutton2_function)
            back_button2.grid(row=5,column=0)

            search(title,author,isbn_nospace)
        else:
            text = tk.Text(content_frame,height=1,width=65)
            text.insert("1.0","Please enter at least one search criteria(name or author or isbn)")
            text.grid(row=0,column=0)
    button_sb = tk.Button(content_frame,text="SUBMIT",command=collected_inputs)
    button_sb.grid(row=3,column=2)
def borrowbutton_function():
    back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
    back_button.grid(row=6,column=0)
    button_frame.pack_forget()
    content_frame.pack()
    label1 = tk.Label(content_frame,text="Name of the book:",font=("arial",12))
    label1.grid(row=0,column=0)
    input_title = tk.Entry(content_frame)
    input_title.grid(row=0,column=1)

    label2 = tk.Label(content_frame,text="Author of the book:",font=("arial",12))
    label2.grid(row=1,column=0)
    input_author = tk.Entry(content_frame)
    input_author.grid(row=1,column=1)
    
    label3 = tk.Label(content_frame,text="ISBN of the book:",font=("arial",12))
    label3.grid(row=2,column=0)
    input_isbn = tk.Entry(content_frame)
    input_isbn.grid(row=2,column=1)
    label4 = tk.Label(content_frame,text="MEMBER ID:")
    label4.grid(row=3,column=0)
    input_memberid = tk.Entry(content_frame)
    input_memberid.grid(row=3,column=1)
    def collected_inputs():
        title = input_title.get()
        author = input_author.get()
        isbn = input_isbn.get()
        try:
            memberid = int(input_memberid.get())
        except ValueError:
            text = tk.Text(content_frame,height=1,width=16)
            text.insert("1.0","Invalid input")
            return
        isbn_nodashes = isbn.replace("-","") 
        isbn_nospace = isbn_nodashes.replace(" ","")
        input_author.grid_forget()
        input_title.grid_forget()
        input_isbn.grid_forget()
        input_memberid.grid_forget()
        label1.grid_forget()
        label2.grid_forget()
        label3.grid_forget()
        label4.grid_forget()
        button_bb.grid_forget()

        def backbutton2_function():
            for widget in content_frame.winfo_children():
                if widget == label1 or widget == label2 or widget == back_button or widget == input_title or widget == button_bb or widget == input_author or widget == label3 or widget == label4 or widget == input_isbn or widget == input_memberid :
                    pass
                else:
                    widget.destroy()
            label1.grid(row=0,column=0)
            label2.grid(row=1,column=0)
            label3.grid(row=2,column=0)
            label4.grid(row=3,column=0)
            input_title.grid(row=0,column=1)
            input_author.grid(row=1,column=1)
            input_isbn.grid(row=2,column=1)
            input_memberid.grid(row=3,column=1)
            button_bb.grid(row=3,column=2)
            back_button.grid(row=6,column=0)
        back_button2 = tk.Button(content_frame,text="<- BACK TO BORROW BOOK MENU",command=backbutton2_function)
        back_button2.grid(row=5,column=0)

        is_member(memberid,borrow,title,author,isbn_nospace)
    button_bb = tk.Button(content_frame,text="SUBMIT",command=collected_inputs)
    button_bb.grid(row=3,column=2)
def returnbook_function():
    back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
    back_button.grid(row=6,column=0)
    button_frame.pack_forget()
    content_frame.pack()
    label1 = tk.Label(content_frame,text="Name of the book:",font=("arial",12))
    label1.grid(row=0,column=0)
    input_title = tk.Entry(content_frame)
    input_title.grid(row=0,column=1)

    label2 = tk.Label(content_frame,text="Author of the book:",font=("arial",12))
    label2.grid(row=1,column=0)
    input_author = tk.Entry(content_frame)
    input_author.grid(row=1,column=1)
    
    label3 = tk.Label(content_frame,text="ISBN of the book:",font=("arial",12))
    label3.grid(row=2,column=0)
    input_isbn = tk.Entry(content_frame)
    input_isbn.grid(row=2,column=1)
    label4 = tk.Label(content_frame,text="MEMBER ID:")
    label4.grid(row=3,column=0)
    input_memberid = tk.Entry(content_frame)
    input_memberid.grid(row=3,column=1)
    def collected_inputs():
        title = input_title.get()
        author = input_author.get()
        isbn = input_isbn.get()
        try:
            memberid = int(input_memberid.get())
        except ValueError:
            text = tk.Text(content_frame,height=1,width=16)
            text.insert("1.0","Invalid input")
            return
        isbn_nodashes = isbn.replace("-","") 
        isbn_nospace = isbn_nodashes.replace(" ","")
        input_author.grid_forget()
        input_title.grid_forget()
        input_isbn.grid_forget()
        input_memberid.grid_forget()
        label1.grid_forget()
        label2.grid_forget()
        label3.grid_forget()
        label4.grid_forget()
        button_rb.grid_forget()

        def backbutton2_function():
            for widget in content_frame.winfo_children():
                if widget == label1 or widget == label2 or widget == back_button or widget == input_title or widget == input_author or widget == button_rb or widget == label3 or widget == label4 or widget == input_isbn or widget == input_memberid :
                    pass
                else:
                    widget.destroy()
            label1.grid(row=0,column=0)
            label2.grid(row=1,column=0)
            label3.grid(row=2,column=0)
            label4.grid(row=3,column=0)
            input_title.grid(row=0,column=1)
            input_author.grid(row=1,column=1)
            input_isbn.grid(row=2,column=1)
            input_memberid.grid(row=3,column=1)
            button_rb.grid(row=3,column=2)
            back_button.grid(row=6,column=0)
        back_button2 = tk.Button(content_frame,text="<- BACK TO RETURN BOOK MENU",command=backbutton2_function)
        back_button2.grid(row=5,column=0)
        
        is_member(memberid,return_book,title,author,isbn_nospace)
    button_rb = tk.Button(content_frame,text="SUBMIT",command=collected_inputs)
    button_rb.grid(row=3,column=2)

def editbook_function(widget1,widget2,widget3,widget4,collected_password,button_function):
    back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
    back_button.grid(row=7,column=0)
    widget1.grid_forget()
    widget2.grid_forget()
    widget3.grid_forget()
    widget4.grid_forget()
    title_label = tk.Label(content_frame,text="Title of Book:")
    title_label.grid(row=0,column=0)
    booktitle = tk.Entry(content_frame)
    booktitle.grid(row=0,column=1)
    author_label = tk.Label(content_frame,text="Author of Book:")
    author_label.grid(row=1,column=0)
    bookauthor = tk.Entry(content_frame)
    bookauthor.grid(row=1,column=1)
    isbn_label = tk.Label(content_frame,text="ISBN of Book:")
    isbn_label.grid(row=2,column=0)
    bookisbn = tk.Entry(content_frame)
    bookisbn.grid(row=2,column=1)

    def collected_inputs(booktitle,bookauthor,bookisbn,button_ed,title_label,author_label,isbn_label):
        book_title = booktitle.get()
        book_author = bookauthor.get()
        book_isbn = bookisbn.get()
        button_ed.grid_forget()
        title_label.grid_forget()
        booktitle.grid_forget()
        author_label.grid_forget()
        bookauthor.grid_forget()
        isbn_label.grid_forget()
        bookisbn.grid_forget()

        def backbutton2_function():
            for widget in content_frame.winfo_children():
                widget.destroy()
            title_label = tk.Label(content_frame,text="Title of Book:")
            title_label.grid(row=0,column=0)
            booktitle = tk.Entry(content_frame)
            booktitle.grid(row=0,column=1)
            author_label = tk.Label(content_frame,text="Author of Book:")
            author_label.grid(row=1,column=0)
            bookauthor = tk.Entry(content_frame)
            bookauthor.grid(row=1,column=1)
            isbn_label = tk.Label(content_frame,text="ISBN of Book:")
            isbn_label.grid(row=2,column=0)
            bookisbn = tk.Entry(content_frame)
            bookisbn.grid(row=2,column=1)
            back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
            back_button.grid(row=7,column=0)
            button_ed = tk.Button(content_frame,text="SUBMIT",command=lambda:collected_inputs(booktitle,bookauthor,bookisbn,button_ed,title_label,author_label,isbn_label))
            button_ed.grid(row=3,column=1)
            back_button4 = tk.Button(content_frame,text="<- BACK TO ADMIN MENU",command=lambda:backbutton2admin_function(collected_password))
            back_button4.grid(row=6,column=0)
            back_button5 = tk.Button(content_frame,text="<-BACK TO ADMIN OPTIONS",command=button_function)
            back_button5.grid(row=6,column=2)

        back_button2 = tk.Button(content_frame,text="<- BACK TO EDIT BOOK MENU",command=backbutton2_function)
        back_button2.grid(row=6,column=0)


        edit_book(book_title,book_author,book_isbn,backbutton_function,backbutton2_function,button_function)
    button_ed = tk.Button(content_frame,text="SUBMIT",command=lambda:collected_inputs(booktitle,bookauthor,bookisbn,button_ed,title_label,author_label,isbn_label))
    button_ed.grid(row=3,column=1)

def addbook_function(widget1,widget2,widget3,widget4,collected_password,button_function):
    back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
    back_button.grid(row=7,column=0)
    widget1.grid_forget()
    widget2.grid_forget()
    widget3.grid_forget()
    widget4.grid_forget()
    label1 = tk.Label(content_frame,text="Name of the book:",font=("arial",12))
    label1.grid(row=0,column=0)
    input_title = tk.Entry(content_frame)
    input_title.grid(row=0,column=1)

    label2 = tk.Label(content_frame,text="Author of the book:",font=("arial",12))
    label2.grid(row=1,column=0)
    input_author = tk.Entry(content_frame)
    input_author.grid(row=1,column=1)
    
    label3 = tk.Label(content_frame,text="ISBN of the book:",font=("arial",12))
    label3.grid(row=2,column=0)
    input_isbn1 = tk.Entry(content_frame)
    input_isbn1.grid(row=2,column=1)

    def collected_inputs(input_title,input_author,input_isbn1,label1,label2,label3,button_ad):
        title = input_title.get()
        author = input_author.get()
        isbn = input_isbn1.get()
        input_author.grid_forget()
        input_title.grid_forget()
        input_isbn1.grid_forget()
        label1.grid_forget()
        label2.grid_forget()
        label3.grid_forget()
        button_ad.grid_forget()
        isbn_nodashes = isbn.replace("-","")
        isbn_nospace = isbn_nodashes.replace(" ","")
        text1 = tk.Text(content_frame,height=2,width=34)
        text2 = tk.Text(content_frame,height=1,width=25)
        input_isbn = tk.Entry(content_frame)
        button2 = tk.Button(content_frame,text="SUBMIT",command=lambda:check_ISBN(title,author,input_isbn,add_book,text1,text2,input_isbn,button2))
        
        def backbutton2_function():
            for widget in content_frame.winfo_children():
              widget.destroy()
            label1 = tk.Label(content_frame,text="Name of the book:",font=("arial",12))
            label1.grid(row=0,column=0)
            input_title = tk.Entry(content_frame)
            input_title.grid(row=0,column=1)

            label2 = tk.Label(content_frame,text="Author of the book:",font=("arial",12))
            label2.grid(row=1,column=0)
            input_author = tk.Entry(content_frame)
            input_author.grid(row=1,column=1)
            
            label3 = tk.Label(content_frame,text="ISBN of the book:",font=("arial",12))
            label3.grid(row=2,column=0)
            input_isbn1 = tk.Entry(content_frame)
            input_isbn1.grid(row=2,column=1)
            back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
            back_button.grid(row=7,column=0)
            button_ad = tk.Button(content_frame,text="SUBMIT",command=lambda:collected_inputs(input_title,input_author,input_isbn1,label1,label2,label3,button_ad))
            button_ad.grid(row=4,column=1)
            back_button4 = tk.Button(content_frame,text="<- BACK TO ADMIN MENU",command=lambda:backbutton2admin_function(collected_password))
            back_button4.grid(row=6,column=0)
            back_button5 = tk.Button(content_frame,text="<-BACK TO ADMIN OPTIONS",command=button_function)
            back_button5.grid(row=6,column=2)

        back_button2 = tk.Button(content_frame,text="<- BACK TO ADD BOOK MENU",command=backbutton2_function)
        back_button2.grid(row=5,column=0)

        check_ISBN(title,author,isbn_nospace,add_book,text1,text2,input_isbn,button2)
    button_ad = tk.Button(content_frame,text="SUBMIT",command=lambda:collected_inputs(input_title,input_author,input_isbn1,label1,label2,label3,button_ad))
    button_ad.grid(row=4,column=1)

def change_password(widget1,widget2,widget3,widget4,widget5):
    back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
    back_button.grid(row=7,column=0)
    widget1.grid_forget()
    widget2.grid_forget()
    widget3.grid_forget()
    widget4.grid_forget()
    widget5.grid_forget()
    label = tk.Label(content_frame,text="NEW PASSWORD:")
    label.grid(row=0,column=0)
    new_password = tk.Entry(content_frame)
    new_password.grid(row=0,column=1)
    def collected_password():
        password = new_password.get().strip()
        label.grid_forget()
        new_password.grid_forget()
        button.grid_forget()
        label2 = tk.Label(content_frame,text="CONFIRM NEW PASSWORD:")
        label2.grid(row=0,column=0)
        password2 = tk.Entry(content_frame)
        password2.grid(row=0,column=1)
        def confirm_password(inputpassword):
            password2 = inputpassword.get().strip()
            label2.grid_forget()
            inputpassword.grid_forget()
            button2.grid_forget()
            if password2 == password:
                with open("library_password.txt","w") as f:
                    f.write(password)
                text = tk.Text(content_frame,height=1,width=40)
                text.insert("1.0","Password successfully changed")
                text.grid(row=0,column=0)
            else:
                text = tk.Text(content_frame,height=1)
                text.insert("1.0","PASSWORD DOESN'T MATCH")
                text.grid(row=0,column=0)
        button2 = tk.Button(content_frame,text="SUBMIT",command=lambda:confirm_password(password2))
        button2.grid(row=1,column=1)
    button = tk.Button(content_frame,text="SUBMIT",command=collected_password)
    button.grid(row=1,column=1)

def backbutton2admin_function(collected_password):
    for widget in content_frame.winfo_children():
        widget.destroy()
    label = tk.Label(content_frame,text="What is the password:")
    label.grid(row=0,column=0)
    input_password2 = tk.Entry(content_frame)
    input_password2.grid(row=0,column=1)
    back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
    back_button.grid(row=7,column=0)
    password_button = tk.Button(content_frame,text="SUBMIT",command=lambda:collected_password(back_button,input_password2,label,password_button))
    password_button.grid(row=1,column=1)

def admin():
    back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
    back_button.grid(row=7,column=0)
    button_frame.pack_forget()
    content_frame.pack()
    admin_password = "AS13qYuP0"
    file_exists = os.path.exists("library_password.txt")
    if file_exists:
        with open("library_password.txt","r") as f:
            admin_password = f.read()
    label = tk.Label(content_frame,text="What is the password:")
    label.grid(row=0,column=0)
    input_password = tk.Entry(content_frame)
    input_password.grid(row=0,column=1)
    def collected_password(back_button,input_password,label,password_button):
        input_password.grid_forget()
        label.grid_forget()
        password_button.grid_forget()
        back_button.grid_forget()
        if input_password.get().strip() == admin_password:
            label2 = tk.Label(content_frame,text="What would you like to do?")
            label2.grid(row=0,column=0)
            button1 = tk.Button(content_frame,text="ADD A BOOK",command=lambda:addbook_function(label2,button1,button2,button3,collected_password,backbutton4_function))
            button1.grid(row=1,column=0,pady=5,padx=5)
            button2 = tk.Button(content_frame,text="EDIT A BOOK",command=lambda:editbook_function(label2,button1,button2,button3,collected_password,backbutton4_function))
            button2.grid(row=1,column=2,pady=5,padx=5)
            button3 = tk.Button(content_frame,text="CHANGE PASSWORD",command=lambda:change_password(label2,button1,button2,button3,back_button2))
            button3.grid(row=2,column=1,pady=5)

            def backbutton4_function():
                for widget in content_frame.winfo_children():
                    widget.destroy()
                label2 = tk.Label(content_frame,text="What would you like to do?")
                label2.grid(row=0,column=0)
                button1 = tk.Button(content_frame,text="ADD A BOOK",command=lambda:addbook_function(label2,button1,button2,button3,collected_password,backbutton4_function))
                button1.grid(row=1,column=0,pady=5,padx=5)
                button2 = tk.Button(content_frame,text="EDIT A BOOK",command=lambda:editbook_function(label2,button1,button2,button3,collected_password,backbutton4_function))
                button2.grid(row=1,column=2,pady=5,padx=5)
                button3 = tk.Button(content_frame,text="CHANGE PASSWORD",command=lambda:change_password(label2,button1,button2,button3,back_button2))
                button3.grid(row=2,column=1,pady=5)
                back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
                back_button.grid(row=7,column=0)
                back_button2 = tk.Button(content_frame,text="<- BACK TO ADMIN MENU",command=lambda:backbutton2admin_function(collected_password))
                back_button2.grid(row=6,column=0)
            back_button4 = tk.Button(content_frame,text="<-BACK TO ADMIN OPTIONS",command=backbutton4_function)
            back_button4.grid(row=6,column=2)

            back_button2 = tk.Button(content_frame,text="<- BACK TO ADMIN MENU",command=lambda:backbutton2admin_function(collected_password))
            back_button2.grid(row=6,column=0)


        else:
            text = tk.Text(content_frame,height=1,width=30)
            text.insert("end","Password incorrect")
            text.grid(row=0,column=0)
            back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
            back_button.grid(row=7,column=0)
    password_button = tk.Button(content_frame,text="SUBMIT",command=lambda:collected_password(back_button,input_password,label,password_button))
    password_button.grid(row=1,column=1)

def showbook_function():
    back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
    back_button.grid(row=5,column=0)
    button_frame.pack_forget()
    content_frame.pack()
    show_books()
def becomemember_function():
    back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
    back_button.grid(row=6,column=0)
    button_frame.pack_forget()
    content_frame.pack()
    label1 = tk.Label(content_frame,text="Your last name:")
    label1.grid(row=0,column=0)
    lastname = tk.Entry(content_frame)
    lastname.grid(row=0,column=1)
    label2 = tk.Label(content_frame,text="Your first name:")
    label2.grid(row=1,column=0)
    firstname = tk.Entry(content_frame)
    firstname.grid(row=1,column=1)
    def collected_inputs():
        first_name = firstname.get()
        last_name = lastname.get()
        label1.grid_forget()
        firstname.grid_forget()
        label2.grid_forget()
        lastname.grid_forget()
        button_bm.grid_forget()

        def backbutton2_function():
            for widget in content_frame.winfo_children():
                if widget == label1 or widget == label2 or widget == back_button or widget == firstname or widget == lastname or widget == button_bm:
                    pass
                else:
                    widget.destroy()
            label1.grid(row=0,column=0)
            label2.grid(row=1,column=0)
            lastname.grid(row=0,column=1)
            firstname.grid(row=1,column=1)
            button_bm.grid(row=2,column=1)
            back_button.grid(row=6,column=0)
        back_button2 = tk.Button(content_frame,text="<- BACK TO BECOME MEMBER MENU",command=backbutton2_function)
        back_button2.grid(row=5,column=0)

        new_member(first_name,last_name)
    button_bm = tk.Button(content_frame,text="SUBMIT",command=collected_inputs)
    button_bm.grid(row=2,column=1)
def deletemember_function():
    back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
    back_button.grid(row=6,column=0)
    button_frame.pack_forget()
    content_frame.pack()
    label1 = tk.Label(content_frame,text="Your last name:")
    label1.grid(row=0,column=0)
    input_lastname = tk.Entry(content_frame)
    input_lastname.grid(row=0,column=1)
    label2 = tk.Label(content_frame,text="Your first name:")
    label2.grid(row=1,column=0)
    input_firstname = tk.Entry(content_frame)
    input_firstname.grid(row=1,column=1)
    label3 = tk.Label(content_frame,text="Your membership id:")
    label3.grid(row=2,column=0)
    input_memberid = tk.Entry(content_frame)
    input_memberid.grid(row=2,column=1)
    def collected_inputs():
        firstname = input_firstname.get()
        lastname = input_lastname.get()
        try:
            memberid = int(input_memberid.get())
        except ValueError:
            text = tk.Text(content_frame,height=1,width=16)
            text.insert("1.0","Invalid input")
            return
        label1.grid_forget()
        input_firstname.grid_forget()
        label2.grid_forget()
        input_lastname.grid_forget()
        label3.grid_forget()
        input_memberid.grid_forget()
        button_dm.grid_forget()

        def backbutton2_function():
            for widget in content_frame.winfo_children():
                if widget == label1 or widget == label2 or widget == back_button or widget == input_firstname or widget == input_lastname or widget == label3 or widget == input_memberid or widget == button_dm:
                    pass
                else:
                    widget.destroy()
            label1.grid(row=0,column=0)
            label2.grid(row=1,column=0)
            label3.grid(row=2,column=0)
            input_lastname.grid(row=0,column=1)
            input_firstname.grid(row=1,column=1)
            input_memberid.grid(row=2,column=1)
            button_dm.grid(row=3,column=1)
            back_button.grid(row=6,column=0)
        back_button2 = tk.Button(content_frame,text="<- BACK TO DELETE MEMBER MENU",command=backbutton2_function)
        back_button2.grid(row=5,column=0)

        delete_member(firstname,lastname,memberid)
    button_dm = tk.Button(content_frame,text="SUBMIT",command=collected_inputs)
    button_dm.grid(row=3,column=1)
def searchmember_function():
    back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
    back_button.grid(row=6,column=0)
    button_frame.pack_forget()
    content_frame.pack()
    label1 = tk.Label(content_frame,text="Your last name:")
    label1.grid(row=0,column=0)
    input_lastname = tk.Entry(content_frame)
    input_lastname.grid(row=0,column=1)
    label2 = tk.Label(content_frame,text="Your first name:")
    label2.grid(row=1,column=0)
    input_firstname = tk.Entry(content_frame)
    input_firstname.grid(row=1,column=1)
    def collected_inputs():
        firstname = input_firstname.get()
        lastname = input_lastname.get()
        label1.grid_forget()
        input_firstname.grid_forget()
        label2.grid_forget()
        input_lastname.grid_forget()
        button_sm.grid_forget()

        def backbutton2_function():
            for widget in content_frame.winfo_children():
                if widget == label1 or widget == label2 or widget == input_firstname or widget == back_button or widget == input_lastname or widget == button_sm:
                    pass
                else:
                    widget.destroy()
            label1.grid(row=0,column=0)
            label2.grid(row=1,column=0)
            input_lastname.grid(row=0,column=1)
            input_firstname.grid(row=1,column=1)
            button_sm.grid(row=2,column=1)
            back_button.grid(row=6,column=0)
        back_button2 = tk.Button(content_frame,text="<- BACK TO SEARCH MENU",command=backbutton2_function)
        back_button2.grid(row=5,column=0)
        search_member(firstname,lastname)
    button_sm = tk.Button(content_frame,text="SUBMIT",command=collected_inputs)
    button_sm.grid(row=2,column=1)
def finepayment_function():
    back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
    back_button.grid(row=7,column=0)
    button_frame.pack_forget()
    content_frame.pack()
    attempts = 5
    finepayment_text = tk.Text(content_frame,height=1,width=50)
    finepayment_text.insert("1.0","Your payment would have to be done using Tobo bank")
    finepayment_text.grid(row=0,column=0)
    finepayment_label = tk.Label(content_frame,text="MEMBERSHIP ID:")
    finepayment_label.grid(row=1,column=0)
    input_memberid = tk.Entry(content_frame)
    input_memberid.grid(row=1,column=1)
    def collected_inputs():
        button.grid_forget()
        try:
            memberid = int(input_memberid.get())
        except ValueError:
            text = tk.Text(content_frame,height=1,width=16)
            text.insert("1.0","Invalid input")
            text.grid(row=0,column=0)
            return
        finepayment_text.grid_forget()
        finepayment_label.grid_forget()
        input_memberid.grid_forget()
        file_exists = os.path.exists("member_fines.csv")
        if not file_exists:
            text1 = tk.Text(content_frame,height=1,width=30)
            text1.insert("end","No fines have been issued yet")
            text1.grid(row=0,column=0)
            return
        with open("member_fines.csv","r") as f:
            fine_reader = csv.reader(f)
            for fine_row in fine_reader:
                if fine_row[0] == str(memberid):
                    total_fine = int(fine_row[1])
                    if total_fine > 0:
                        global fine
                        fine = False
                        import random
                        choice_label = tk.Label(content_frame,text="What would you like to do")
                        choice_label.grid(row=0,column=1)

                        def backbutton2_function():
                            for widget in content_frame.winfo_children():
                                widget.destroy()
                            choice_label = tk.Label(content_frame,text="What would you like to do")
                            choice_label.grid(row=0,column=1)
                            signup_button = tk.Button(content_frame,text="SIGN UP",command=signup_function)
                            signup_button.grid(row=1,column=0,pady=35,padx=10)
                            login_button = tk.Button(content_frame,text="LOG IN",command=login_function)
                            login_button.grid(row=1,column=2,pady=35,padx=10)
                            back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
                            back_button.grid(row=7,column=0)

                        def signup_function():
                            for widget in content_frame.winfo_children():
                                widget.destroy()
                            back_button2 = tk.Button(content_frame,text="<- BACK TO BANK MENU",command=backbutton2_function)
                            back_button2.grid(row=5,column=0)
                            back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
                            back_button.grid(row=7,column=0)
                            label1 = tk.Label(content_frame,text="SURNAME:")
                            label1.grid(row=0,column=0)
                            input_surname = tk.Entry(content_frame)
                            input_surname.grid(row=0,column=1)
                            label2 = tk.Label(content_frame,text="FIRST NAME:")
                            label2.grid(row=1,column=0)
                            input_firstname = tk.Entry(content_frame)
                            input_firstname.grid(row=1,column=1)
                            label3 = tk.Label(content_frame,text="OTHER NAMES:")
                            label3.grid(row=2,column=0)
                            input_othernames = tk.Entry(content_frame)
                            input_othernames.grid(row=2,column=1)
                            def collected_names():
                                button1.grid_forget()
                                surname = input_surname.get().strip().capitalize()
                                firstname = input_firstname.get().strip().capitalize()
                                other_names = input_othernames.get().strip().capitalize()
                                label1.grid_forget()
                                input_surname.grid_forget()
                                label2.grid_forget()
                                input_firstname.grid_forget()
                                label3.grid_forget()
                                input_othernames.grid_forget()
                                name = surname+" "+firstname+" "+other_names
                                password_label = tk.Label(content_frame,text="Set up a strong password for your account\nPassword must have at least: 8 characters, 1 lowercase, 1 upper case, 1 special character:\n")
                                password_label.grid(row=0,column=0)
                                input_password = tk.Entry(content_frame)
                                input_password.grid(row=0,column=1)
                                def collected_password(password):
                                    if hasattr(password,"get"):
                                        password = password.get().strip()
                                    else:
                                        password = password.strip()
                                    button2.grid_forget()
                                    password_label.grid_forget()
                                    input_password.grid_forget()
                                    if len(password) < 8:
                                        password_label.config(text="Your password has to be at least 8 characters\nSet Another password:")
                                        password_label.grid(row=0,column=0)
                                        input_password.grid(row=0,column=1)
                                        button2.grid(row=1,column=1)
                                    else:
                                        lower = 0
                                        upper = 0
                                        for case in password:
                                            if case.islower():
                                                lower += 1
                                            if case.isupper():
                                                upper += 1
                                        if lower < 1 or upper < 1:
                                            password_label.config(text="You should have at least 1 lower and 1 upper case characters\nSet Another password:")
                                            password_label.grid(row=0,column=0)
                                            input_password.grid(row=0,column=1)
                                            button2.grid(row=1,column=1)
                                        else:
                                            special_character = "!@#$%^&£~¬*()_+=-[]{}|\\:;""`<>,.?/`"
                                            special_count = 0
                                            for case in password:
                                                if case in special_character:
                                                    special_count += 1
                                            if special_count < 1: 
                                                password_label.config(text="Your password must have at least 1 special characters\nSet Another password:")
                                                password_label.grid(row=0,column=0)
                                                input_password.grid(row=0,column=1)
                                                button2.grid(row=1,column=1)
                                            else:
                                                numbers = "0123456789"
                                                number_count = 0
                                                for case in password:
                                                    if case in numbers:
                                                        number_count += 1
                                                if number_count < 1:
                                                    password_label.config(text="Your password must have at least one digit\nSet Another password:")
                                                    password_label.grid(row=0,column=0)
                                                    input_password.grid(row=0,column=1)
                                                    button2.grid(row=1,column=1)
                                                else:
                                                    text = tk.Text(content_frame,height=1,width=40)
                                                    text.insert("1.0","Password successfully set")
                                                    text.grid(row=0,column=0)
                                                    account_number = random.randint(1000000000,9999999999)
                                                    file_exists = os.path.exists("ToboBank_users.csv")
                                                    if file_exists:
                                                        duplicate = True
                                                        while duplicate:
                                                            with open("ToboBank_users.csv","r") as f:
                                                                reader = csv.reader(f)
                                                                next(reader)
                                                                for row in reader:
                                                                    if row[3] == account_number:
                                                                        account_number = random.randint(1000000000,9999999999)
                                                                        break
                                                                else:
                                                                    duplicate = False
                                                    with open("ToboBank_users.csv","a",newline="") as f:
                                                        bank_writer = csv.writer(f)
                                                        if not file_exists:
                                                            bank_writer.writerow(["Firstname","Middlename","Lastname","Account Number","Password","Account Balance"])
                                                        bank_writer.writerow([firstname,other_names,surname,account_number,password,0])
                                                    welcome_text = tk.Text(content_frame,height=2,width=50)
                                                    welcome_text.insert("1.0",f"Welcome to Tobo Bank {name}\nYour account number is {account_number}")
                                                    welcome_text.grid(row=0,column=0)
                                button2 = tk.Button(content_frame,text="SUBMIT",command=lambda:collected_password(input_password))
                                button2.grid(row=1,column=1)
                            button1 = tk.Button(content_frame,text="SUBMIT",command=collected_names)
                            button1.grid(row=3,column=1)
                        def login_function():
                            for widget in content_frame.winfo_children():
                                widget.destroy()
                            back_button2 = tk.Button(content_frame,text="<- BACK TO BANK MENU",command=backbutton2_function)
                            back_button2.grid(row=6,column=0)
                            back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
                            back_button.grid(row=7,column=0)
                            button_frame.pack_forget()
                            content_frame.pack()
                            account_label = tk.Label(content_frame,text="Enter your account number: ")
                            account_label.grid(row=0,column=0)
                            input_account = tk.Entry(content_frame)
                            input_account.grid(row=0,column=1)
                            def collected_account():
                                button1.grid_forget()
                                with open("ToboBank_users.csv","r") as f:
                                    bank_reader = csv.reader(f)
                                    next(bank_reader)
                                    for bank_row in bank_reader:
                                        button1.pack_forget()
                                        account_label.grid_forget()
                                        person_account = input_account.get().strip()
                                        input_account.grid_forget()
                                        if person_account == bank_row[3]:
                                            global found
                                            found = True
                                            correct_password = bank_row[4]
                                            balance = int(bank_row[5])
                                            firstname = bank_row[0]
                                            middlename = bank_row[1]
                                            lastname = bank_row[2]
                                            password_label = tk.Label(content_frame,text="What is your password: ")
                                            password_label.grid(row=0,column=0)
                                            input_password2 = tk.Entry(content_frame)
                                            input_password2.grid(row=0,column=1)
                                            attempts = 5
                                            def collected_password(input_password,button,label,attempts):
                                                button2.grid_forget()
                                                person_password = input_password.get().strip()
                                                button.grid_forget()
                                                label.grid_forget()
                                                input_password.grid_forget()
                                                if person_password == correct_password:
                                                    text = tk.Text(content_frame,height=1,width=50)
                                                    text.insert("1.0",f"Welcome Back {lastname} {middlename} {firstname}")
                                                    text.grid(row=0,column=0)
                                                    decision_label = tk.Label(content_frame,text="What do you want to do",font=("bold"))
                                                    decision_label.grid(row=2,column=0,padx=(50,0))
                                                    def deposit_function():
                                                        for widget in content_frame.winfo_children():
                                                            widget.destroy()
                                                        back_button2 = tk.Button(content_frame,text="<- BACK TO BANK MENU",command=backbutton2_function)
                                                        back_button2.grid(row=6,column=0)
                                                        back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
                                                        back_button.grid(row=7,column=0)
                                                        back_button4 = tk.Button(content_frame,text="<- BACK TO LOGIN MENU",command=backbutton4_function)
                                                        back_button4.grid(row=6,column=2)
                                                        deposit_label2 = tk.Label(content_frame,text="How much do you want to deposit: NGN")
                                                        deposit_label2.grid(row=0,column=0)
                                                        input_amount = tk.Entry(content_frame)
                                                        input_amount.grid(row=0,column=1)
                                                        def collected_amount():
                                                            try:
                                                                deposit_amount = int(input_amount.get())
                                                                deposit_label2.grid_forget()
                                                                input_amount.grid_forget()
                                                                deposit_button2.grid_forget()
                                                                if deposit_amount < 0:
                                                                    error_text = tk.Text(content_frame,height=1,width=20)
                                                                    error_text.insert("1.0","Invalid input")
                                                                    error_text.grid(row=0,column=0)
                                                                else:
                                                                    with open("ToboBank_users.csv","r") as f:
                                                                        bank_reader2 = csv.reader(f)
                                                                        rows = list(bank_reader2)
                                                                    for i in range(1,len(rows)):
                                                                        if rows[i][3] == person_account:
                                                                            rows[i][5] = int(rows[i][5]) + deposit_amount
                                                                    with open("ToboBank_users.csv","w",newline="") as f:
                                                                        bank_writer = csv.writer(f)
                                                                        bank_writer.writerows(rows)
                                                                    confirmation_text = tk.Text(content_frame,height=1,width=50)
                                                                    confirmation_text.insert("1.0",f"YOU HAVE SUCCESSFULLY DEPOSITED {deposit_amount} Naira")
                                                                    confirmation_text.grid(row=0,column=0)
                                                            except ValueError:
                                                                error_text = tk.Text(content_frame,height=1,width=20)
                                                                error_text.insert("1.0","Invalid input")
                                                                error_text.grid(row=0,column=0)
                                                        deposit_button2 = tk.Button(content_frame,text="SUBMIT",command=collected_amount)
                                                        deposit_button2.grid(row=1,column=1)
                                                    def finepayment_function():
                                                        for widget in content_frame.winfo_children():
                                                            widget.destroy()
                                                        back_button2 = tk.Button(content_frame,text="<- BACK TO BANK MENU",command=backbutton2_function)
                                                        back_button2.grid(row=6,column=0)
                                                        back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
                                                        back_button.grid(row=7,column=0)
                                                        back_button4 = tk.Button(content_frame,text="<- BACK TO LOGIN MENU",command=backbutton4_function)
                                                        back_button4.grid(row=6,column=2)
                                                        total_fine = 0
                                                        with open("member_fines.csv","r") as f:
                                                            fine_reader2 = csv.reader(f)
                                                            next(fine_reader2)
                                                            for fine_row2 in fine_reader2:
                                                                if fine_row2[0] == str(memberid):
                                                                    total_fine = int(fine_row2[1])
                                                        with open("ToboBank_users.csv","r") as f:
                                                            bank_reader3 = csv.reader(f)
                                                            next(bank_reader3)
                                                            for bank_row3 in bank_reader3:
                                                                if bank_row3[3] == person_account:
                                                                    current_balance = bank_row3[5]
                                                                    break
                                                        if int(current_balance) > total_fine and total_fine != 0:
                                                            with open("ToboBank_users.csv","r") as f:
                                                                bank_reader2 = csv.reader(f)
                                                                rows = list(bank_reader2)
                                                            for i in range(1,len(rows)):
                                                                if rows[i][3] == person_account:
                                                                    rows[i][5] = int(rows[i][5]) - total_fine
                                                            with open("ToboBank_users.csv","w",newline="") as f:
                                                                bank_writer = csv.writer(f)
                                                                bank_writer.writerows(rows)
                                                            confirmation_text = tk.Text(content_frame,height=2,width=50)
                                                            confirmation_text.insert("1.0",f"Payment of {total_fine} naira successful\nYou are now fine free")
                                                            confirmation_text.grid(row=0,column=0)
                                                            wanted_rows = []
                                                            with open("member_fines.csv","r") as f:
                                                                fine_reader = csv.reader(f)
                                                                for fine_row in fine_reader:
                                                                    if fine_row[0] == str(memberid):
                                                                        pass
                                                                    else:
                                                                        wanted_rows.append(fine_row)
                                                            with open("member_fines.csv","w",newline="") as f:
                                                                writer = csv.writer(f)
                                                                writer.writerows(wanted_rows)
                                                        elif total_fine == 0:
                                                            paid_text = tk.Text(content_frame,height=1)
                                                            paid_text.insert("1.0","Fine has already been paid")
                                                            paid_text.grid(row=0,column=0)
                                                        else:
                                                            lowbalance_text = tk.Text(content_frame,height=3)
                                                            lowbalance_text.insert("end",f"Insufficient funds\nMoney in account is {balance} naira\nFine is {total_fine} naira")
                                                            lowbalance_text.grid(row=0,column=0)
                                                    def check_balance():
                                                        for widget in content_frame.winfo_children():
                                                            widget.destroy()
                                                        back_button2 = tk.Button(content_frame,text="<- BACK TO BANK MENU",command=backbutton2_function)
                                                        back_button2.grid(row=6,column=0)
                                                        back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
                                                        back_button.grid(row=7,column=0)
                                                        back_button4 = tk.Button(content_frame,text="<- BACK TO LOGIN MENU",command=backbutton4_function)
                                                        back_button4.grid(row=6,column=2)
                                                        with open("ToboBank_users.csv","r") as f:
                                                            bank_reader2 = csv.reader(f)
                                                            next(bank_reader2)
                                                            for bank_row2 in bank_reader2:
                                                                if person_account == bank_row2[3]:
                                                                    current_balance = int(bank_row2[5])
                                                                    break
                                                        balance_text = tk.Text(content_frame,height=1)
                                                        balance_text.insert("1.0",f"Balance is {current_balance} naira")
                                                        balance_text.grid(row=0,column=0)
                                                    def backbutton4_function():
                                                        for widget in content_frame.winfo_children():
                                                            widget.destroy()
                                                        decision_label = tk.Label(content_frame,text="What do you want to do",font=("bold"))
                                                        decision_label.grid(row=2,column=0,padx=(50,0))
                                                        deposit_button = tk.Button(content_frame,text="1. DEPOSIT",command=deposit_function)
                                                        deposit_button.grid(row=3,column=0,pady=35)
                                                        finepayment_button = tk.Button(content_frame,text="2. PAYMENT OF FINE",command=finepayment_function)
                                                        finepayment_button.grid(row=3,column=1,pady=35,padx=(0,150))
                                                        checkbalance_button = tk.Button(content_frame,text="3. CHECK BALANCE",command=check_balance)
                                                        checkbalance_button.grid(row=3,column=2,pady=35)
                                                        back_button2 = tk.Button(content_frame,text="<- BACK TO BANK MENU",command=backbutton2_function)
                                                        back_button2.grid(row=6,column=0)
                                                        back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
                                                        back_button.grid(row=7,column=0)
                                                    deposit_button = tk.Button(content_frame,text="1. DEPOSIT",command=deposit_function)
                                                    deposit_button.grid(row=3,column=0,pady=35)
                                                    finepayment_button = tk.Button(content_frame,text="2. PAYMENT OF FINE",command=finepayment_function)
                                                    finepayment_button.grid(row=3,column=1,pady=35,padx=(0,150))
                                                    checkbalance_button = tk.Button(content_frame,text="3. CHECK BALANCE",command=check_balance)
                                                    checkbalance_button.grid(row=3,column=2,pady=35)
                                                    back_button4 = tk.Button(content_frame,text="<- BACK TO LOGIN MENU",command=backbutton4_function)
                                                    back_button4.grid(row=6,column=2)
                                                else:
                                                    if attempts > 0 and person_password != correct_password:
                                                        passwordlabel = tk.Label(content_frame,text=f"The password you entered is incorrect\nYou have {attempts} attempts left\n")
                                                        passwordlabel.grid(row=0,column=0)
                                                        inputpassword = tk.Entry(content_frame)
                                                        inputpassword.grid(row=0,column=1)
                                                        attempts -= 1
                                                        button3 = tk.Button(content_frame,text="SUBMIT",command=lambda:collected_password(inputpassword,button3,passwordlabel,attempts))
                                                        button3.grid(row=1,column=1)
                                                    elif attempts == 0:
                                                        noattempts_text = tk.Text(content_frame,height=1,width=30)
                                                        noattempts_text.insert("1.0","You have no attempts left")
                                                        noattempts_text.grid(row=0,column=0)
                                            button2 = tk.Button(content_frame,text="SUBMIT",command=lambda:collected_password(input_password2,button2,password_label,attempts))
                                            button2.grid(row=1,column=1)
                                
                                    if not found:
                                        error_text = tk.Text(content_frame)
                                        error_text.insert("1.0","Account number not found")
                                        error_text.grid(row=0,column=0)
                            button1 = tk.Button(content_frame,text="SUBMIT",command=collected_account)
                            button1.grid(row=1,column=1)
                        signup_button = tk.Button(content_frame,text="SIGN UP",command=signup_function)
                        signup_button.grid(row=1,column=0,pady=35,padx=10)

                        login_button = tk.Button(content_frame,text="LOG IN",command=login_function)
                        login_button.grid(row=1,column=2,pady=35,padx=10)

                        break
            else:
                error_text2 = tk.Text(content_frame,height=1,width=30)
                error_text2.insert("1.0","No Match")
                error_text2.grid(row=0,column=0)

    button = tk.Button(content_frame,text="SUBMIT",command=collected_inputs)
    button.grid(row=2,column=1)

# ==== USER INTERFACE ====
window = tk.Tk()
window.title("TOBO LIBRARY SERVICES")
window.config(bg="#421BD3")

title_frame = tk.Frame(window)
title_frame.pack()

title = tk.Label(title_frame,text="TOBO LIBRARY SERVICES",bg="#FF4500",fg="white",font=("Courier",20,"bold"))
title.pack()

button_frame = tk.Frame(window)
button_frame.pack()
button_frame.config(bg="#421BD3")

content_frame = tk.Frame(window)

search_button = tk.Button(button_frame,text="1. SEARCH A BOOK",fg="white",bg="#FF6B9D",font=("Bauhaus 93",14),command=searchbutton_function)
search_button.grid(row=1,column=3,padx=10,pady=(35,5))

borrow_button = tk.Button(button_frame,text="2. BORROW A BOOK",fg="white",bg="#7C3AED",font=("Bauhaus 93",14),command=borrowbutton_function)
borrow_button.grid(row=1,column=4,pady=(35,5))

return_button = tk.Button(button_frame,text="3. RETURN A BOOK",fg="white",bg="#2C2C2C",font=("Bauhaus 93",14),command=returnbook_function)
return_button.grid(row=2,column=3,padx=10,pady=5)

add_button = tk.Button(button_frame,text="4. ADMIN",fg="white",bg="#1ECBE1",font=("Bauhaus 93",14),command=admin)
add_button.grid(row=2,column=4,pady=5)

showbooks_button = tk.Button(button_frame,text="5. SHOW ALL BOOKS",fg="white",bg="#FFD700",font=("Bauhaus 93",14),command=showbook_function)
showbooks_button.grid(row=3,column=3,padx=10,pady=5)

become_member = tk.Button(button_frame,text="6. BECOME A MEMBER",fg="white",bg="#2ECC71",font=("Bauhaus 93",14),command=becomemember_function)
become_member.grid(row=3,column=4,pady=5)

deletemember_button = tk.Button(button_frame,text="7. DELETE MEMBERSHIP",fg="white",bg="#2C3E50",font=("Bauhaus 93",14),command=deletemember_function)
deletemember_button.grid(row=4,column=3,padx=10,pady=5)

searchmember_button = tk.Button(button_frame,text="8. SEARCH MEMBER",fg="white",bg="red",font=("Bauhaus 93",14),command=searchmember_function)
searchmember_button.grid(row=4,column=4,pady=5)

finepayment_button = tk.Button(button_frame,text="9. PAYMENT OF FINE",fg="white",bg="#00FF00",font=("Bauhaus 93",14),command=finepayment_function)
finepayment_button.grid(row=5,column=3,pady=5)

window.mainloop()
