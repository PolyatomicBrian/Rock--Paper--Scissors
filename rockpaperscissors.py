
from Tkinter import *
import random

root = Tk()

screenW = root.winfo_screenwidth()
screenH = root.winfo_screenheight()

root.title("Rock, Paper, Scissors")
root.geometry(str(screenW/4)+"x"+str(screenH/2))
root.resizable(0,0)
root.configure(background="white")

app = Frame(root)
app.grid()

imgRock = PhotoImage(file="Assets/Rock.gif")
imgPaper = PhotoImage(file="Assets/Paper.gif")
imgScissors = PhotoImage(file="Assets/Scissors.gif")

lbl = Label(app, text="", font="Times 20 bold")

lblYou = Label(app)
lblEnemy = Label(app)

def setTextColor():
    if lbl.cget("text") == "WIN":
        lbl.configure(fg = "dark green")
    elif lbl.cget("text") == "LOSE":
        lbl.configure(fg = "red")
    else:
        lbl.configure(fg = "black")

def enemyThrow():
    rndNum = random.randint(1,3)
    if rndNum == 1:
        rndThrow = "Rock"
        lblEnemy.configure(image=imgRock)
    elif rndNum == 2:
        rndThrow = "Paper"
        lblEnemy.configure(image=imgPaper)
    else:
        rndThrow = "Scissors"
        lblEnemy.configure(image=imgScissors)
    return rndThrow

def throwR():
    enemyThrown = enemyThrow()
    lblYou.configure(image=imgRock)
    if enemyThrown == "Rock":
        lbl.configure(text="TIE")
    elif enemyThrown == "Paper":
        lbl.configure(text="LOSE")
    else:
        lbl.configure(text="WIN")
    setTextColor()

def throwP():
    enemyThrown = enemyThrow()
    lblYou.configure(image=imgPaper)
    if enemyThrown == "Rock":
        lbl.configure(text="WIN")
    elif enemyThrown == "Paper":
        lbl.configure(text="TIE")
    else:
        lbl.configure(text="LOSE")
    setTextColor()

def throwS():
    enemyThrown = enemyThrow()
    lblYou.configure(image=imgScissors)
    if enemyThrown == "Rock":
        lbl.configure(text="LOSE")
    elif enemyThrown == "Paper":
        lbl.configure(text="WIN")
    else:
        lbl.configure(text="TIE")
    setTextColor()

btnRock = Button(app, text = "Rock", command=throwR).grid(row=1,column=1,sticky="s")
btnPaper = Button(app, text = "Paper", command=throwP).grid(row=1,column=2,sticky="s")
btnScissors = Button(app, text = "Scissors", command=throwS).grid(row=1,column=3,sticky="S")

lblYou.grid()
lbl.grid()
lblEnemy.grid()

root.mainloop()
