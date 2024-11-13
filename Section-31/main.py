import constants
from tkinter import *
from tkinter import messagebox
import pandas as pd
import random as rnd

to_learn = {}
current_card = {}
##### choosing words from the csv file
try:
    df = pd.read_csv("./data/words_to_learn.csv")
    to_learn = df.to_dict(orient='records')
except FileNotFoundError:
    df = pd.read_csv("./data/french_words.csv")
    to_learn = df.to_dict(orient='records')

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    if 'French' in df.columns:
        current_card = rnd.choice(to_learn)
        canvas.itemconfig(card_title, text="French")
        #word = df.sample(n=1).French.item()
        canvas.itemconfig(card_word, text=current_card['French'])
        canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(constants.TIMEOUT, func=flip_card)
def flip_card():
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card['English'])
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    pd.DataFrame(to_learn).to_csv("./data/words_to_learn.csv", index=False)
    next_card()
    print(len(to_learn))
    if len(to_learn)==0:
        messagebox.showinfo(title="Congratulations", message="You've learned all the words!")
        window.quit()
# Screen desing
window= Tk()
window.title("Flashy Quiz")
window.config(padx=constants.PADX, pady=constants.PADY, bg=constants.BACKGROUND_COLOR)
flip_timer=window.after(constants.TIMEOUT, func=flip_card)

canvas = Canvas(width=constants.SCREEN_WIDTH, height=constants.SCREEN_HEIGHT, bg=constants.BACKGROUND_COLOR)

card_front_img= PhotoImage(file = "./images/card_front.png")
card_back_img= PhotoImage(file = "./images/card_back.png")
card_background=canvas.create_image(constants.SCREEN_WIDTH_HALF, constants.SCREEN_HEIGHT_HALF, image=card_front_img)


canvas.config(bg=constants.BACKGROUND_COLOR, highlightthickness=0)  
canvas.grid(row=0, column=0, columnspan=2)

card_title=canvas.create_text(constants.SCREEN_WIDTH_HALF, constants.SCREEN_HEIGHT_HALF, text="Title", font=("Arial", 40, "italic"), fill=constants.TEXT_COLOR)
card_word=canvas.create_text(constants.SCREEN_WIDTH_HALF, constants.SCREEN_HEIGHT_HALF + 100, text="word", font=("Arial", 20, "bold"), fill=constants.TEXT_COLOR)


img_reject= PhotoImage(file = "./images/wrong.png")
btn_reject = Button(image=img_reject, highlightthickness=0, command=next_card)
btn_reject.grid(row=1, column=0)

img_accept = PhotoImage(file = "./images/right.png")
btn_accept = Button(image=img_accept, highlightthickness=0, command=is_known)
btn_accept.grid(row=1, column=1)

next_card()


















window.mainloop()