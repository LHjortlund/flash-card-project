from tkinter import *
from random import  choice, shuffle
import pandas
from pandas.core.interchange.dataframe_protocol import DataFrame

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"


# ------------------------- BUTTON COMMANDS ---------------------------- #
data = pandas.read_csv("data/franske_ord.csv")
to_learn = data.to_dict(orient="records")
current_card = {}
# print(to_learn)

def next_card():
    global current_card
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])


def flip_card():
    canvas.itemconfig(card_title, text="Dansk", fill="white")
    canvas.itemconfig(card_word, text=current_card["Dansk"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


#---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card - Fransk og Dansk")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(3000, func=flip_card)

#images/canvas
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image=card_front_img)
#create text
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400,263, text="word", font=("Arial", 60, "bold") )
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

#creating right and wrong buttons
cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image)
wrong_button.config(bg = BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_image)
right_button.config(bg = BACKGROUND_COLOR, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()