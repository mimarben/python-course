from tkinter import *
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=0)

website_lable = Label(text="WebSite",font=(FONT_NAME, 12, "bold"))
website_lable.grid(column=0, row=1)
website_text=Entry(width=35)
website_text.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email", font=(FONT_NAME, 12, "bold"))
email_label.grid(column=0, row=2)
email_text=Entry(width=35)
email_text.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password", font=(FONT_NAME, 12, "bold"))
password_label.grid(column=0, row=3)
password_text=Entry(width=35)
password_text.grid(row=3, column=1, columnspan=2)

#canvas.pack()
window.mainloop()