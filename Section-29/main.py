from tkinter import *
from tkinter import messagebox
import random
import pyperclip


FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_letters = password_letters + [random.choice(symbols) for _ in range(nr_symbols)]
    password_letters = password_letters + [random.choice(numbers) for _ in range(nr_numbers)]
    
    random.shuffle(password_letters)
    
    password= "".join(password_letters)
    password_text.insert(0,password)
    print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    new_line = f"{website_text.get()} | {email_text.get()} | {password_text.get()}\n"
    if len(password_text.get()) > 0 and len(website_text.get()) > 0 and len(email_text.get()) > 0:
        confirmation=messagebox.askokcancel(title="Save Password", message=f"These are the details for:\n Website: {website_text.get()}\nEmail: {email_text.get()}\nPassword: {password_text.get()}")
        if confirmation==True:
            with open("password.txt", "a") as file:
                file.write(new_line)    
            website_text.delete(0, END)
            password_text.delete(0, END)
            email_text.delete(0, END)
    else:
        messagebox.showinfo(title="Oops", message="Please make sure to fill out all fields.")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1,row=0)

# labels
website_lablel = Label(text="WebSite: ",font=(FONT_NAME, 12, "bold"))
website_lablel.grid(column=0, row=1)

email_label = Label(text="Email: ", font=(FONT_NAME, 12, "bold"))
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ", font=(FONT_NAME, 12, "bold"))
password_label.grid(column=0, row=3)

#Entries
website_text=Entry(width=45)
website_text.grid(row=1, column=1, columnspan=2)
website_text.focus()
email_text=Entry(width=45)
email_text.grid(row=2, column=1, columnspan=2)
email_text.insert(0, "example@email.com")
password_text=Entry(width=21)
password_text.grid(row=3, column=1)
generate_button = Button(text="Generate Password", font=(FONT_NAME, 12), command=generate_password, width=18)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", font=(FONT_NAME, 12), command=save_password, width=35)
add_button.grid(row=4, column=1, columnspan=2)
#canvas.pack()
window.mainloop()