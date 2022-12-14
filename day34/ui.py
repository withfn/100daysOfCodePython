from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.canvas = Canvas(width=300, height=300, highlightthickness=0)
        self.question = self.canvas.create_text(
            150, 
            150,
            width=280,
            text="", 
            fill=THEME_COLOR, 
            font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=30, pady=40)
        
        self.score = Label(text=f"Score: ", font=('Arial', 18, 'italic'), bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)
        
        self.cross_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.cross_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=0)
        
        self.right_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.right_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=1)
        
        self.get_question()
        
        self.window.mainloop()
        
    def get_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            
        
    
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))
    
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_question)