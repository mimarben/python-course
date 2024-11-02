from tkinter import *
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
def generate_password():
    pass
def save_password():
    pass
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
email_text=Entry(width=45)
email_text.grid(row=2, column=1, columnspan=2)
password_text=Entry(width=21)
password_text.grid(row=3, column=1)
generate_button = Button(text="Generate Password", font=(FONT_NAME, 12), command=generate_password, width=18)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", font=(FONT_NAME, 12), command=save_password, width=35)
add_button.grid(row=4, column=1, columnspan=2)
#canvas.pack()
window.mainloop()