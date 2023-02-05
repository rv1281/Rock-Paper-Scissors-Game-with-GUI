from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import messagebox
import sys

root = Tk()

user_wins = 0
computer_wins = 0
values = ["rock", "paper", "scissors"]

#App setting
root.title("Rock, Paper, Scissors Game")
root.geometry("600x600+100+200")
root.resizable(False, False)
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
bg_color = "#%02x%02x%02x" % (r, g, b)
root.configure(bg=bg_color)
img = Image.open("static/label.png")
img = img.resize((500,100), resample=Image.Resampling.LANCZOS)
p = ImageTk.PhotoImage(img)
label = Label(root, image = p, bg=bg_color)
label.place(x=50,y=50)
result = Text(root,width=55, height=1, bg=bg_color, relief=FLAT)
result.place(x=95,y=250)

score_label = Label(root, text="User Wins: {}  | Computer Wins: {}".format(user_wins, computer_wins), bg=bg_color)
score_label.place(x=200, y=500)

    

#Icons for buttons
img_r = Image.open("static/Rock.png")
img_r = img_r.resize((70,70), resample=Image.Resampling.LANCZOS)
photo1 = ImageTk.PhotoImage(img_r)

img_p = Image.open("static/Paper.png")
img_p = img_p.resize((70,70), resample=Image.Resampling.LANCZOS)
photo2 = ImageTk.PhotoImage(img_p)

img_s = Image.open("static/Scissors.png")
img_s = img_s.resize((70,70), resample=Image.Resampling.LANCZOS)
photo3 = ImageTk.PhotoImage(img_s)

#buttons
button1  = Button(root, image= photo1, bd = 0, bg = bg_color,activebackground= bg_color, command= lambda: press("rock"))
button1.place(x=100, y=350)

button2  = Button(root, image= photo2, bd = 0, bg = bg_color,activebackground= bg_color, command= lambda: press("paper") )
button2.place(x=265, y=350)

button3  = Button(root, image= photo3, bd = 0, bg = bg_color,activebackground= bg_color, command= lambda: press("scissors"))
button3.place(x=430, y=350)


def press(user_choice):
    global user_wins, computer_wins
    random_number = random.randint(0, 2)
    computer_pick = values[random_number]
    result.delete("1.0", "end")
    if user_choice == "rock" and computer_pick == values[2]:
        result.insert(END, "You clicked rock. Computer picked scissors. You win!")
        result.tag_configure("center", justify='center')
        result.tag_add("center", 1.0, "end")
        user_wins += 1
    elif user_choice == "paper" and computer_pick == values[0]:
        result.insert(END, "You clicked paper. Computer picked rock. You win!")
        result.tag_configure("center", justify='center')
        result.tag_add("center", 1.0, "end")
        user_wins += 1
    elif user_choice == "scissors" and computer_pick == values[1]:
        result.insert(END, "You clicked scissors. Computer picked paper. You win!")
        result.tag_configure("center", justify='center')
        result.tag_add("center", 1.0, "end")
        user_wins += 1
    elif user_choice == computer_pick:
        result.insert(END, "You both picked the same. It's a tie!")
        result.tag_configure("center", justify='center')
        result.tag_add("center", 1.0, "end")
    else:
        computer_wins += 1
        result.insert(END, "You clicked {}. Computer picked {}. You lose!".format(user_choice, computer_pick))
        result.tag_configure("center", justify='center')
        result.tag_add("center", 1.0, "end")
    score_label.config(text="User Wins: {}   Computer Wins: {}".format(user_wins, computer_wins))



root.protocol("WM_DELETE_WINDOW", lambda: messagebox.showinfo("Result", "User Wins: {}   Computer Wins: {}\nYou {}!".format(user_wins, computer_wins, "won" if user_wins > computer_wins else "lost" if user_wins < computer_wins else "tied")) and sys.exit())
root.mainloop()
