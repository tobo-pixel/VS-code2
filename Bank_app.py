import tkinter as tk
import csv
import os
window = tk.Tk()
window.title("TOBO BANK APP")

button_frame = tk.Frame(window)
button_frame.pack()

content_frame = tk.Frame(window)
attempts = 5

def bankapp(fine,memberid):
  global found
  found = False
  import random
  label = tk.Label(button_frame,text="What would you like to do")
  label.grid(row=0,column=1)

  def backbutton_function():
    for widget in content_frame.winfo_children():
        widget.destroy()
    content_frame.pack_forget()
    button_frame.pack()

  def signup_function():
      back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
      back_button.grid(row=5,column=0)
      button_frame.pack_forget()
      content_frame.pack()
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
        from Password_checker import password_checker
        password_label = tk.Label(content_frame,text="Set up a strong password for your account\nPassword must have at least: 8 characters, 1 lowercase, 1 upper case, 1 special character:\n")
        password_label.grid(row=0,column=0)
        input_password = tk.Entry(content_frame)
        input_password.grid(row=0,column=1)
        def collected_password():
          password = input_password.get().strip()
          button2.grid_forget()
          password_label.grid_forget()
          input_password.grid_forget()
          password_checker(password)
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
          text = tk.Text(content_frame,height=2,width=50)
          text.insert("1.0",f"Welcome to Tobo Bank {name}\nYour account number is {account_number}")
          text.grid(row=0,column=0)
        button2 = tk.Button(content_frame,text="SUBMIT",command=collected_password)
        button2.grid(row=1,column=1)
      button1 = tk.Button(content_frame,text="SUBMIT",command=collected_names)
      button1.grid(row=3,column=1)
  def login_function():
    back_button = tk.Button(content_frame,text="<- RETURN TO MAIN MENU",command=backbutton_function)
    back_button.grid(row=5,column=0)
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
            password_label = tk.Label(content_frame,text="What is your password: ")
            password_label.grid(row=0,column=0)
            input_password = tk.Entry(content_frame)
            input_password.grid(row=0,column=1)
            def collected_password(input_password,button,label):
              button2.grid_forget()
              person_password = input_password.get().strip()
              button.grid_forget()
              label.grid_forget()
              input_password.grid_forget()
              if person_password == bank_row[4]:
                text = tk.Text(content_frame,height=1,width=50)
                text.insert("1.0",f"Welcome Back {bank_row[2]} {bank_row[1]} {bank_row[0]}")
                text.grid(row=0,column=0)
                decision_label = tk.Label(content_frame,text="What do you want to do",font=("bold"))
                decision_label.grid(row=2,column=0,padx=(50,0))
                def deposit_function():
                  text.grid_forget()
                  decision_label.grid_forget()
                  deposit_button.grid_forget()
                  finepayment_button.grid_forget()
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
                  text.grid_forget()
                  decision_label.grid_forget()
                  deposit_button.grid_forget()
                  finepayment_button.grid_forget()
                  if int(bank_row[5]) > fine:
                    with open("ToboBank_users.csv","r") as f:
                      bank_reader2 = csv.reader(f)
                      rows = list(bank_reader2)
                    for i in range(1,len(rows)):
                      if rows[i][3] == person_account:
                        rows[i][5] = int(rows[i][5]) - fine
                    with open("ToboBank_users.csv","w",newline="") as f:
                      bank_writer = csv.writer(f)
                      bank_writer.writerows(rows)
                    confirmation_text = tk.Text(content_frame,height=2,width=50)
                    confirmation_text.insert("1.0",f"Payment of {fine} naira successful\nYou are now fine free")
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
                  else:
                    lowbalance_text = tk.Text(content_frame,height=3)
                    lowbalance_text.insert("end",f"Insufficient funds\nMoney in account is {bank_row[5]} naira\nFine is {fine} naira")
                    lowbalance_text.grid(row=0,column=0)
                deposit_button = tk.Button(content_frame,text="1. DEPOSIT",command=deposit_function)
                deposit_button.grid(row=3,column=0,pady=35)
                finepayment_button = tk.Button(content_frame,text="2. PAYMENT OF FINE",command=finepayment_function)
                finepayment_button.grid(row=3,column=1,pady=35,padx=(0,150))
              else:
                global attempts
                if attempts > 0 and person_password != bank_row[4]:
                    passwordlabel = tk.Label(content_frame,text=f"The password you entered is incorrect\nYou have {attempts} attempts left\n")
                    passwordlabel.grid(row=0,column=0)
                    inputpassword = tk.Entry(content_frame)
                    inputpassword.grid(row=0,column=1)
                    attempts -= 1
                    button3 = tk.Button(content_frame,text="SUBMIT",command=lambda:collected_password(inputpassword,button3,passwordlabel))
                    button3.grid(row=1,column=1)
                elif attempts == 0:
                    noattempts_text = tk.Text(content_frame,height=1,width=30)
                    noattempts_text.insert("1.0","You have no attempts left")
                    noattempts_text.grid(row=0,column=0)
            button2 = tk.Button(content_frame,text="SUBMIT",command=lambda:collected_password(input_password,button2,password_label))
            button2.grid(row=1,column=1)
          
        if not found:
          error_text = tk.Text(content_frame)
          error_text.insert("1.0","Account number not found")
          error_text.grid(row=0,column=0)
    button1 = tk.Button(content_frame,text="SUBMIT",command=collected_account)
    button1.grid(row=1,column=1)
  signup_button = tk.Button(button_frame,text="SIGN UP",command=signup_function)
  signup_button.grid(row=1,column=0,pady=35,padx=10)

  login_button = tk.Button(button_frame,text="LOG IN",command=login_function)
  login_button.grid(row=1,column=2,pady=35,padx=10)

  window.mainloop()