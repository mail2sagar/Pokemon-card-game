from tkinter import *
import random


window = Tk()

window.title("Pokemon Card Game")
window.geometry("600x400")

window.config(background="dark orange")


label1 = Label(window,text="Player 1")
label1.config(background="firebrick1")


label2 = Label(window,text="Player 2")
label2.config(background="firebrick1")

p1_score = Label(window)
p1_score.config(background="DodgerBlue2")

p2_score = Label(window)
p2_score.config(background="DodgerBlue2")

label_result = Label(window)
label_result.config(background="alice blue")

player1_btn = Button(window)

player2_btn = Button(window)


label1.place(relx=0.1,rely=0.3,anchor=CENTER)
label2.place(relx=0.9,rely=0.3,anchor=CENTER)

p1_score.place(relx=0.1,rely=0.4,anchor=CENTER)
p2_score.place(relx=0.9,rely=0.4,anchor=CENTER)


label_result.place(relx=0.5,rely=0.5,anchor=CENTER)

window.mainloop()