import tkinter as tk
from tkinter import messagebox
def button_clicked():
    user_text = user_input1.get()
    label1.config(text = f"you typed {user_text}")
    print(f"ACTIVITY:{user_text}")
def show_choice():
    if check_var.get() == 1:
        label1.config(text="checked")
    else:
        label1.config(text="unchecked")
def showchoice_radio():
    choice = radio_var.get()
    label2.config(text=f"You selected {choice}")
def show_selection(event):
    selection = listbox.curselection()  # Gets index of selected item
    if selection:
        item = listbox.get(selection[0])  #  Gets the actual text
        label2.config(text=f"You selected {item}")
def show_error():
    messagebox.showerror("Error","This is an error message")
window = tk.Tk()
window.title("My first app")
window.geometry("400x700")
window.config(bg="red")

top_frame = tk.Frame(window)
top_frame.pack()

bottom_frame = tk.Frame(window)
bottom_frame.pack()

text_box = tk.Text(bottom_frame,bg="green",fg="white",font=("Courier",14,"bold"))
text_box.grid(row=5,column=0)
text_box.insert("1.0","This is the text box\n")
text_box.insert("end","More text in the textbox")


listbox = tk.Listbox(bottom_frame)
listbox.grid(row=3,column=0)
listbox.insert(0,"Python")
listbox.insert(1,"Javascript")
listbox.insert(2,"Java")
listbox.insert(3,"C++")
listbox.bind("<<ListboxSelect>>",show_selection)  # Triggers when an item is selected

radio_var = tk.StringVar()
radio_var.set("Small")  # Set default selection
#Create radio buttons
radio1 = tk.Radiobutton(bottom_frame,text="Small",variable=radio_var,value="Small")
radio1.grid(row=0,column=0)

radio2 = tk.Radiobutton(bottom_frame,text="Medium",variable=radio_var,value="Medium")
radio2.grid(row=1,column=0)

radio3 = tk.Radiobutton(bottom_frame,text="Large",variable=radio_var,value="Large")
radio3.grid(row=2,column=0)

check_var = tk.IntVar()
checkbox = tk.Checkbutton(top_frame,text="I agree",variable=check_var,command=show_choice,bg="orange",fg="white",font=("Courier",14,"bold"))
checkbox.grid(row=0,column=0)

label1 = tk.Label(top_frame,text = "Something",bg="green",fg="white",font=("Courier",14,"bold"))
label1.grid(row=0,column=1)

user_input1 = tk.Entry(top_frame)
user_input1.grid(row=0,column=2)

label2 = tk.Label(top_frame,text = "mehn")
label2.grid(row=1,column=3)

user_input2 = tk.Entry(bottom_frame,bg="blue",fg="white",font=("times",14,"bold"))
user_input2.grid(row=1,column=1)

button = tk.Button(top_frame,text = "Submit",command=show_error,bg="orange",fg="white",font=("Courier",14,"bold"))
button.grid(row=2,column=1,columnspan=5, sticky="ew")
window.mainloop()