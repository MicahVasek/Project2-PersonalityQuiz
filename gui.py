from tkinter import *
from functions import *


class Gui:
    """
    Start of the GUI
    'phase' is used to determine what the program should be doing.
    'QUESTIONS' and 'NUMBERS' are used for displaying info to the user.
    'name', 'reasult', 'answers', and 'score' are all used to record info inputed by the user.
    """
    QUESTIONS = ["I always prefer peaceful solutions.",
                 "Friendship can triumph through all.",
                 "Nothing beats a beautiful sunrise!",
                 "Violence begets violence.",
                 "I'd rather have lots of frineds than none at all.",
                 "Love and peace always beat hate and vengence.",
                 "Karma will always deliver justice.",
                 "An eye for an eye just makes the whole world blind.",
                 "I see myself as a friendly/cheerful person.",
                 "Love is one of the most powerful things in the world."]
    NUMBERS = ["Question 1:",
               "Question 2:",
               "Question 3:",
               "Question 4:",
               "Question 5:",
               "Question 6:",
               "Question 7:",
               "Question 8:",
               "Question 9:",
               "Question 10:"]
    phase = -1
    score = 0
    name = ''
    result = ''
    answers = []

    def __init__(self, window: Tk) -> None:
        self.window = window

        self.frame_1 = Frame(self.window)
        self.title = Label(self.frame_1, text='Welcome to the personality quiz!')
        self.title.pack(side='top')
        self.frame_1.pack(anchor='center', padx=10, pady=5)

        self.frame_2 = Frame(self.window)
        self.label_question = Label(self.frame_2, text='Enter your name below, then you can begin the quiz!')
        self.input_name = Entry(self.frame_2)
        self.radio_answer = IntVar()
        self.radio_answer.set(0)
        self.radiobutton_1 = Radiobutton(self.frame_2, text='S. disagree', variable=self.radio_answer, value=1)
        self.radiobutton_2 = Radiobutton(self.frame_2, text='Disagree', variable=self.radio_answer, value=2)
        self.radiobutton_3 = Radiobutton(self.frame_2, text='Neutral', variable=self.radio_answer, value=3)
        self.radiobutton_4 = Radiobutton(self.frame_2, text='Agree', variable=self.radio_answer, value=4)
        self.radiobutton_5 = Radiobutton(self.frame_2, text='S. agree', variable=self.radio_answer, value=5)
        self.label_question.pack(padx=15, pady=5, side='top')
        self.input_name.pack(padx=15, pady=5, side='top')
        self.frame_2.pack(anchor='center', padx=10, pady=10)

        self.frame_4 = Frame(self.window)
        self.button_save = Button(self.frame_4, text='ENTER', command=self.submit)
        self.button_save.pack(side='top')
        self.frame_4.pack(anchor='center', padx=10, pady=10)

        self.frame_5 = Frame(self.window)
        self.label_alert = Label(text='')
        self.label_alert.pack(side='top')
        self.frame_5.pack(anchor='center', padx=10, pady=10)

    def submit(self) -> None:
        """
        Take input when the user presses the 'ENTER' button. Depends on the 'phase'.
        On phase = -1, when the program first starts, the user inputs their name, which is recorded.
        On phase = 0-9, the program uses 'phase' to determine which question to display to the user.
        On phase = 10, the quiz is over, and the information is processed.
        """
        if Gui.phase == -1:
            try:
                Gui.name = self.input_name.get()
                if Gui.name == '':
                    raise ValueError
                self.input_name.pack_forget()
                self.label_question.pack(side='top')
                self.radiobutton_1.pack(side='left')
                self.radiobutton_2.pack(side='left')
                self.radiobutton_3.pack(side='left')
                self.radiobutton_4.pack(side='left')
                self.radiobutton_5.pack(side='left')
                Gui.phase += 1
                self.label_question.config(text=Gui.QUESTIONS[Gui.phase])
                self.title.config(text=Gui.NUMBERS[Gui.phase])
                self.label_alert.config(text='')
            except ValueError:
                self.label_alert.config(text='Enter a name before continuing.')
        elif -1 < Gui.phase < 9:
            try:
                if self.radio_answer.get() == 0:
                    raise ValueError
                Gui.answers.append(self.radio_answer.get())
                Gui.phase += 1
                self.radio_answer.set(0)
                self.label_question.config(text=Gui.QUESTIONS[Gui.phase])
                self.label_alert.config(text='')
            except ValueError:
                self.label_alert.config(text='Select an answer before continuing.')
        else:
            Gui.answers.append(self.radio_answer.get())
            Gui.score = calculate_score(Gui.answers)
            Gui.result = calculate_result(Gui.score)
            record_quiz(Gui.name, Gui.score, Gui.result)
            augment = f'Scores have been recorded. Congratulations, {Gui.name}! You are: {Gui.result}.'
            self.label_alert.config(text=augment)
