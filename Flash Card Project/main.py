from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
currentcard = {}
tolearn = {}


try:
    data = pandas.read_csv("data/wordstolearn.csv")
except FileNotFoundError:
    originaldata = pandas.read_csv("data/french_words.csv")
    tolearn = originaldata.to_dict(orient="records")
else:
    tolearn = data.to_dict(orient="records")



def nextcard():
    global currentcard, fliptimer
    window.after_cancel(fliptimer)
    currentcard = random.choice(tolearn)
    canvas.itemconfig(cardtitle, text="French", fill="black")
    canvas.itemconfig(cardword, text=currentcard["French"], fill="black")
    canvas.itemconfig(cardbackground, image=cardfrontimg)
    fliptimer = window.after(3000, func=flipcard)

def flipcard():
    canvas.itemconfig(cardtitle, text="English", fill="white")
    canvas.itemconfig(cardword, text=currentcard["English"], fill="white")
    canvas.itemconfig(cardbackground, image=cardbackimg)

def isknown():
    tolearn.remove(currentcard)
    data = pandas.DataFrame(tolearn)
    data.to_csv("data/wordstolearn.csv", index=False)

    nextcard()

#-----------------------------UI------------------------------------
window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
messagebox.showinfo(title="Flashcard App", message="1. Cards will flip after 3s to show the correct English translation.\n2. If you select 'tick' to the question, that word will not be tested again.\n3.All the best!")

window.after(3000, func=flipcard)

fliptimer = window.after(300, func=flipcard)


canvas = Canvas(width=800, height=526)
cardfrontimg = PhotoImage(file="images/card_front.png")
cardbackimg = PhotoImage(file="images/card_back.png")
cardbackground = canvas.create_image(400, 263, image=cardfrontimg)
cardtitle = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
cardword = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

crossimage = PhotoImage(file="images/wrong.png")
unknownbutton = Button(image=crossimage, highlightthickness=0, command=nextcard)
unknownbutton.grid(row=1, column=0)

checkimage = PhotoImage(file="images/right.png")
knownbutton = Button(image=checkimage, highlightthickness=0, command=isknown)
knownbutton.grid(row=1, column=1)


nextcard()

window.mainloop()