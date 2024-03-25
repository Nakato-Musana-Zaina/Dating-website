
import random
import tkinter


colors_name = ['red','yellow','green','purple','white','cyan','purple','black','brown']

score = 0
time_left = 60

def startGame(play):
    if time_left == 60:
        countdown()
        changeColor()

def changeColor():
    global score
    global time_left

    if time_left> 0:
        e.focus_set()
        if e.get().lower() == colors_name[1].lower():
            score += 1

        e.delete(0, tkinter.END)
        random.shuffle(colors_name)
        label.config(fg = str(colors_name[1]), text = str(colors_name[0]))
        scoreLabel.config(text = "score: "+ str(score))


def countdown():
    global time_left
    if time_left > 0:
        time_left -=1
        timeLabe1.config(text = 'Time Left: '+ str(time_left))
        timeLabe1.after(1000,countdown)  

root = tkinter.Tk()
root.title('The COLORGAME')
root.geometry('600*400')

instruct = tkinter.Label(root, text = 'Which Color?', font = ('san-serifif', 30))
instruct.pack()

scoreLabel = tkinter.Label(root, text ='Press Enter Key To start', font = ('san-serif',24))
scoreLabel.pack()

timeLable = tkinter.Label(root,text = 'Time Left: '+ str(time_left), font = ('san-serif',18))
timeLabe1.pack()

label = tkinter.Label(root, font = ('san-serif', 60))
label.pack()

e =tkinter.Entry(root)
root.bind('<Return',startGame)
e.pack()
e.focus_set()

root.mainloop()


