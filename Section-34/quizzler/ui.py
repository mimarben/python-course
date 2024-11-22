from tkinter import Label, Button, PhotoImage, Tk, Canvas
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"
FONT_SIZE = 12
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 450
MIDDLE_WIDTH = CANVAS_WIDTH / 2
MIDDLE_HEIGHT = CANVAS_HEIGHT / 2
QUESTION_TEXT_WIDTH = CANVAS_WIDTH - 20
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.score = 0
        self.quiz=quiz_brain
        self.window = Tk()  # noqa: F405
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        # labels
        self.score_lablel = Label(text="Score: 0",font=(FONT_NAME, FONT_SIZE, "bold"), fg="white", bg=THEME_COLOR)
        self.score_lablel.grid(column=1, row=0)
        
        self.canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        
        
        self.question_text = self.canvas.create_text(
            MIDDLE_WIDTH,
            MIDDLE_HEIGHT,
            width=QUESTION_TEXT_WIDTH,
            text="some question", 
            font=(FONT_NAME, 20, "italic"), 
            fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2,pady=50)
        
        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")
        
        self.true_button = Button(image=true_img, highlightthickness=0, command=lambda: self.check_answer("True"))
        self.true_button.grid(column=0, row=2)
        
        false_button = Button(image=false_img, highlightthickness=0, command=lambda: self.check_answer("False"))
        false_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_lablel.config(text=f"Score: {self.score}/{self.quiz.question_number}")
            self.canvas.configure(bg="white")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.configure(bg="grey")
            self.canvas.itemconfig(self.question_text,text="End of the game 10 question")
            self.score_lablel.config(text=f"Final Score: {self.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def check_answer(self, answer: str):
        user_answer = self.quiz.check_answer(answer)
        print(user_answer)
        if user_answer:
            self.canvas.configure(bg="green")
            self.score += 1
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)
        