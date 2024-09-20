from tkinter import *
from random import choice, shuffle



# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card - Fransk og Dansk")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#images/canvas
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=card_front_img)
#create text
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400,263, text="word", font=("Arial", 60, "bold") )
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

#creating right and wrong buttons
cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image)
wrong_button.config(bg = BACKGROUND_COLOR, highlightthickness=0)
wrong_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_image)
right_button.config(bg = BACKGROUND_COLOR, highlightthickness=0)
right_button.grid(column=1, row=1)



window.mainloop()