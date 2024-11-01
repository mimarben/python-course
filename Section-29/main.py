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

website_lable = Label(text="WebSite",font=(FONT_NAME, 20, "bold"))
website_lable.grid(column=0, row=1)
website_text=canvas.create_text(100, 140, text="", fill="white", font=(FONT_NAME, 35, "bold"))
website_text.grid(column=1, row=1)

email_label = Label(text="Email", font=(FONT_NAME, 20, "bold"))
email_label.grid(column=0, row=2)

password_label = Label(text="Password", font=(FONT_NAME, 20, "bold"))
password_label.grid(column=0, row=3)


#canvas.pack()
window.mainloop()