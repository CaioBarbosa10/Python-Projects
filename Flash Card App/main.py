from tkinter import *

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
data_list = {}
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


try:
    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_list = original_data.to_dict(orient="records")

else:
    data_list = data.to_dict(orient='records')

def is_known():
    data_list.remove(random_word)
    data = pandas.DataFrame(data_list)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()



def flip_card():
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=random_word["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_img)



def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(data_list)
    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(card_word, text= random_word["French"],fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, flip_card)



flip_timer = window.after(3000,flip_card)

canvas= Canvas(width=800, height=526)
card_front = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400,263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
card_word = canvas.create_text(400 , 263, font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0,columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file="images/right.png")
know_button = Button(image=check_image,highlightthickness=0,command= is_known)
know_button.grid(row=1,column=1)




next_card()












window.mainloop()



