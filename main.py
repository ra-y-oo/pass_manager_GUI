from tkinter import *
from tkinter import messagebox
import customtkinter
from random import choice, randint, shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                            f"Passowrd: {password} \n is it oksay to save")
        

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

#System settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

#Our app frame
app = customtkinter.CTk()
app.config(padx=50, pady=50)
app.title("Password Manager")

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

 #Labels
website_label = customtkinter.CTkLabel(app, text="Website:")
website_label.grid(row=1, column=0)
email_label = customtkinter.CTkLabel(app, text="Email/Username:")
email_label.grid(row=2, column=0)
pasword_label = customtkinter.CTkLabel(app, text="Password:")
pasword_label.grid(row=3, column=0)

#Entries
website_entry = customtkinter.CTkEntry(app, width=300)
website_entry.grid(row=1,  column=1, columnspan=2)
website_entry.focus()
email_entry = customtkinter.CTkEntry(app, width=300)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "youremail.com")
password_entry = customtkinter.CTkEntry(app, width=160)
password_entry.grid(row=3, column=1)

#Buttons
generate_password_btn = customtkinter.CTkButton(app, text="Generate Password", command=generate_password)
generate_password_btn.grid(row=3, column=2)
add_btn = customtkinter.CTkButton(app, text="Add", width=300, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

app.mainloop()