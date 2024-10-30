
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1 #25
SHORT_BREAK_MIN = 1 #5
LONG_BREAK_MIN = 2 #25
reps=0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_lable.config(text="Timer", fg=GREEN)
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN*60
    short_breack_sec = SHORT_BREAK_MIN*60
    long_breack_sec = LONG_BREAK_MIN*60
    if reps%2==0:
        count_down(short_breack_sec)
        title_lable.config(text="Short Break", fg=RED)
    elif reps%8==0:
        count_down(long_breack_sec)
        title_lable.config(text="Long Break", fg=RED)
    else:
        count_down(work_sec)
        title_lable.config(text="Work", fg=GREEN)
        
    count_down(WORK_MIN*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    canvas.itemconfig(timer_text, text=f"{count//60:02}:{count%60:02}")
    if count>0:
        global timer
        timer= window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        works_sessions= math.floor(reps/2)
        for _ in range(works_sessions):
            mark += "✔️"
        check_mark.config(text=marks)
        
                

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_lable = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_lable.grid(column=2, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text=canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=1, row=3)
reset_timer = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_timer.grid(column=3, row=3)

#Check marks
check_mark = Button(text="✔️", bg=YELLOW, fg=GREEN, highlightthickness=0)
check_mark.grid(column=2, row=3)



window.mainloop()