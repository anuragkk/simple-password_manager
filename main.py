from tkinter import *

import string
from tkinter import messagebox
from random import choice, randint, shuffle
import json
import pyperclip

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = list(string.ascii_letters)
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    random_number = randint(8, 10)
    password_letters = [choice(letters) for letter in range(random_number)]
    random_number_2 = randint(2, 4)
    password_symbol = [choice(numbers) for number in range(random_number_2)]
    password_numbers = [choice(symbols) for symbol in range(random_number_2)]
    password_list = password_letters + password_numbers + password_symbol
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="Please make sure you haven't left any fields empty.")
    else:
        with open("data.txt", mode="a") as file:
            file.write(f"{website} | {email} | {password}\n")
    website_entry.delete(0, "end")

    password_entry.delete(0, "end")
    messagebox.showinfo(title="success", message="your password is saved")

# ---------------------------- UI SETUP ------------------------------- #

"""window"""
window = Tk()
window.title("Password_manager")
window.config(padx=20, pady=20)
"""canvas"""
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)
"""website_label"""
website_label = Label(text="Website", font=(FONT_NAME, 14, "bold"))
website_label.grid(row=1, column=0)

"""email_label"""
email_label = Label(text="Email/Username", font=(FONT_NAME, 14, "bold"))
email_label.grid(row=2, column=0)

"""password_label"""
password_label = Label(text="Password", font=(FONT_NAME, 14, "bold"))
password_label.grid(row=3, column=0)

"""Generate_password_button"""
generate_password_button = Button(text="Generate_password", command=generate_password)
generate_password_button.grid(row=3, column=2)

"""add_button"""
add_button = Button(text="Add", width=36, command=save)

add_button.grid(row=4, column=1, columnspan=2)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0, "anuragsnd@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

window.mainloop()
