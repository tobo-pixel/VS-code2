import tkinter as tk
window = tk.Tk()
window.title("PASSWORD CHECKER")
password_label = tk.Label(window)
input_password = tk.Entry(window)
button = tk.Button(window,text="SUBMIT",command=lambda:password_checker(input_password))
def password_checker(password):
  password_label.grid_forget()
  input_password.grid_forget()
  button.grid_forget()
  if hasattr(password,"get"):
    password = password.get().strip()
  else:
    pass
    password = password.strip()
  if len(password) < 8:
    password_label.config(text="Your password has to be at least 8 characters\nSet Another password:")
    password_label.grid(row=0,column=0)
    input_password.grid(row=0,column=1)
    button.grid(row=1,column=1)
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
      button.grid(row=1,column=1)
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
        button.grid(row=1,column=1)
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
          button.grid(row=1,column=1)
        else:
          text = tk.Text(window,height=1,width=40)
          text.insert("1.0","Password successfully set")
          text.grid(row=0,column=0)
          return

  window.mainloop()          

          
        
