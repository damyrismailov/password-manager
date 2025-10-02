from tkinter import *
from tkinter import messagebox
from random import choice,randint, shuffle
import pyperclip

def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers)for _ in range(randint(2, 4))]

    new_password = password_letters + password_symbols + password_numbers
    shuffle(new_password)
    password = [f"{char}" for char in new_password]

    password = "".join(password)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def adding_password():
    website = website_entry.get()
    email = username_email_entry.get()
    password = password_entry.get()

    if website == "" or password == "":
        messagebox.showinfo(title="Error", message="Please fill all the fields")
    else:
        is_okay = messagebox.askokcancel(title = website, message = f"These are the details entered: \nEmail: {email}\nPassword: {password}\n is it ok yo save")
        if is_okay:
            with open('password.txt', 'a') as file:
                file.write(f"{website} | {email} | {password} \n")
            username_email_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.delete(0, END)



window = Tk()
window.title("Password manager")
window.config(padx=40, pady=40, bg="white")

canvas = Canvas(width=200, height=200, background="white",highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:",fg= "black" ,bg="white")
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username:",fg= "black", bg="white")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password:",bg="white", fg="black")
password_label.grid(row=3, column=0)

website_entry = Entry(width=39,bg="white",fg= "black",highlightthickness=0)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
username_email_entry = Entry(width=39,bg="white",fg= "black",highlightthickness=0)
username_email_entry.grid(row=2, column=1, columnspan=2)
username_email_entry.insert(0,"username@gmail.com")

password_entry = Entry(width=22, bg="white",fg= "black",highlightthickness=0)
password_entry.grid(row=3, column=1)

generate_password = Button(text="Generate Password",bg="white",highlightthickness=0, command=generate_pass)
generate_password.grid(row=3, column=2)
add_password_button = Button(text="Add", width=36, bg="white",command=adding_password)
add_password_button.grid(row=4, column=1,columnspan=2)

window.mainloop()
