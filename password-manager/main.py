from tkinter import *
from tkinter import messagebox
from random import choice,randint, shuffle
import pyperclip
import json

def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
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
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if website == "" or password == "":
        messagebox.showinfo(title="Error", message="Please fill all the fields")
    else:
           try:
               with open('data.json', 'r') as data_file:
                    data = json.load(data_file)
           except FileNotFoundError:
               with open('data.json', 'w') as data_file:
                   json.dump(new_data, data_file, indent=4)
           else:
               data.update(new_data)
               with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
           finally:
               password_entry.delete(0, END)
               website_entry.delete(0, END)

def find_pass():
  website = website_entry.get()
  try:
     with open('data.json', 'r') as file:
          data = json.load(file)
  except FileNotFoundError:
      messagebox.showinfo(title="Error", message="No data File Found")
  else:
      if website in data:
          messagebox.showinfo(title=website,
                              message=f"email: {data[website]['email']} \n password: {data[website]['password']}")
          website_entry.delete(0, END)
      else:
          messagebox.showinfo(title=website, message=f"No details for the {website} exist")

window = Tk()
window.title("Password manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200,highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:",fg= "white")
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username:",fg= "white")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password:", fg="white")
password_label.grid(row=3, column=0)

website_entry = Entry(width=22,bg="white",fg= "black")
website_entry.grid(row=1, column=1)
website_entry.focus()
username_email_entry = Entry(width=39,fg="black",bg= "white",)
username_email_entry.grid(row=2, column=1, columnspan=2)
username_email_entry.insert(0,"yourmail@gmail.com")

password_entry = Entry(width=22, bg="white",fg= "black")
password_entry.grid(row=3, column=1)

search_button = Button(text="Search",bg="white",fg="black",command=find_pass, width=12)
search_button.grid(row=1, column=2)
generate_password = Button(text="Generate Password",bg="white",highlightthickness=0, command=generate_pass)
generate_password.grid(row=3, column=2)
add_password_button = Button(text="Add", width=36, bg="white",command=adding_password)
add_password_button.grid(row=4, column=1,columnspan=2)

window.mainloop()
