import time
import argparse
from pathlib import Path

import tkinter as tk
from tkinter import *
import tkinter.messagebox

from PIL import Image, ImageTk

import utils

parser = argparse.ArgumentParser(description='Tic Tac toe')
parser.add_argument("--method", help="Method for running the algorithm",
                    default="minmax", type=str)
args = parser.parse_args()

assert args.method in ['minmax', 'abprune'], "Method can be minmax / abprune"
if args.method == 'minmax':
    import minmax as method_ai
else:
    import alpha_beta_pruning as method_ai


main_page = tk.Tk()
main_page.title('Tic Tac Toe')
image_dir = Path('Images')


def makeImg(path):
    im = Image.open(path)
    im = im.resize((70, 70), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(im)
    return img


x = makeImg(image_dir / 'x.png')
o = makeImg(image_dir / 'o.jpeg')
ph = makeImg(image_dir / 'each_place.png')

global a, ai_enabled, player_first, button_dictionary, ttt_board
a = 0               # a tells us how many moves are already done...
ai_enabled = False
button_dictionary = {}
player_first = True
ttt_board = [9 for i in range(9)]


def reset():
    global ttt_board, a
    a = 0
    ai_enabled = False
    player_first = True
    enable_buttons("disabled")
    ttt_board = [9 for i in range(9)]


def select(b, n):
    global a, ai_enabled, player_first, button_dictionary, ttt_board
    if ttt_board[n] != 9:
        tkinter.messagebox.showinfo("Error", " Choose some other box")
        return
    a = a+1
    if ai_enabled and player_first:   # True, and player_first then
        if(a % 2 == 0):
            b.configure(image=x)
            ttt_board[n] = 1            # computer's move done..
            if utils.check_win(ttt_board) == 1:
                reset()
                tkinter.messagebox.showinfo("COMPUTER WON", " Better Luck next time.. ")
            elif utils.check_win(ttt_board) == 0:
                reset()
                tkinter.messagebox.showinfo("It's a DRAW", " Well played..  ")
        else:
            b.configure(image=o)
            ttt_board[n] = 0
            if utils.check_win(ttt_board) == -1:
                reset()
                tkinter.messagebox.showinfo("PLAYER WON", " CONGRATULATIONS.... ")
            elif utils.check_win(ttt_board) == 0:
                reset()
                tkinter.messagebox.showinfo("It's a DRAW", " Well played..  ")
            move = method_ai.best_move(ttt_board)
            select(button_dictionary[move], move)  # call for computer to make a move
    elif ai_enabled:
        # player goes second
        if (a % 2 != 0):
            b.configure(image=x)
            ttt_board[n] = 1        # computer's move done..
            if utils.check_win(ttt_board) == 1:
                reset()
                tkinter.messagebox.showinfo("COMPUTER WON", " Better Luck next time.. ")
            elif utils.check_win(ttt_board) == 0:
                reset()
                tkinter.messagebox.showinfo("It's a DRAW", "Well played .. ")
        else:
            b.configure(image=o)
            ttt_board[n] = 0
            if utils.check_win(ttt_board) == -1:
                reset()
                tkinter.messagebox.showinfo("Player WON", " CONGRATULATIONS... ")
            elif utils.check_win(ttt_board) == 0:
                reset()
                tkinter.messagebox.showinfo("It's a DRAW", "Well played .. ")
            move = method_ai.best_move(ttt_board)
            select(button_dictionary[move], move)  # call for computer to make a move
    else:
        # double player mode
        if (a % 2 == 0):
            b.configure(image=x)
            ttt_board[n] = 1
        else:
            b.configure(image=o)
            ttt_board[n] = 0
        res = utils.check_win(ttt_board)
        if res == 0:
            reset()
            tkinter.messagebox.showinfo("It's a DRAW", "Well played people.. ")
        elif res == -1:
            reset()
            tkinter.messagebox.showinfo(" RESULTS ", " And the winner is O")
        elif res == 1:
            reset()
            tkinter.messagebox.showinfo(" RESULTS ", " And the winner is X ")


def enable_buttons(state_set):
    but1.configure(state=state_set, image=ph)
    but2.configure(state=state_set, image=ph)
    but3.configure(state=state_set, image=ph)
    but4.configure(state=state_set, image=ph)
    but5.configure(state=state_set, image=ph)
    but6.configure(state=state_set, image=ph)
    but7.configure(state=state_set, image=ph)
    but8.configure(state=state_set, image=ph)
    but9.configure(state=state_set, image=ph)


def single_new(player):
    reset()
    global ai_enabled, player_first
    ai_enabled = True
    player_first = player
    enable_buttons("normal")
    if player:
        tkinter.messagebox.showinfo("New Game", " Player starts first ")
    else:
        select(but9, 8)  # 1st move made by computer


def double_new():
    global ai_enabled
    reset()
    ai_enabled = False
    enable_buttons("normal")


def disp_rules():
    rules = ("The objective of Tic Tac Toe is to get three in a row or column"
             "or along a diagonal. You play on a three by three game board."
             " The first player is known as X and the second is O."
             " Players alternate placing Xs and Os on the game board until"
             "either achieves that or all nine squares are filled.")
    tkinter.messagebox.showinfo(" Rules of the game ", rules)


but1 = Button(main_page, image=ph, fg='white', state=DISABLED, command=lambda: select(but1, 0))
but1.grid(row=0, column=0)
button_dictionary[0] = but1


but2 = Button(main_page, image=ph, fg='white', state=DISABLED, command=lambda: select(but2, 1))
but2.grid(row=0, column=1)
button_dictionary[1] = but2


but3 = Button(main_page, image=ph, fg='white', state=DISABLED, command=lambda: select(but3, 2))
but3.grid(row=0, column=2)
button_dictionary[2] = but3


but4 = Button(main_page, image=ph, fg='white', state=DISABLED, command=lambda: select(but4, 3))
but4.grid(row=1, column=0)
button_dictionary[3] = but4


but5 = Button(main_page, image=ph, fg='white', state=DISABLED, command=lambda: select(but5, 4))
but5.grid(row=1, column=1)
button_dictionary[4] = but5


but6 = Button(main_page, image=ph, fg='white', state=DISABLED, command=lambda: select(but6, 5))
but6.grid(row=1, column=2)
button_dictionary[5] = but6


but7 = Button(main_page, image=ph, fg='white', state=DISABLED, command=lambda: select(but7, 6))
but7.grid(row=2, column=0)
button_dictionary[6] = but7


but8 = Button(main_page, image=ph, fg='white', state=DISABLED, command=lambda: select(but8, 7))
but8.grid(row=2, column=1)
button_dictionary[7] = but8


but9 = Button(main_page, image=ph, fg='white', state=DISABLED, command=lambda: select(but9, 8))
but9.grid(row=2, column=2)
button_dictionary[8] = but9
menubar = Menu(main_page)


single_menu = Menu(menubar, tearoff=0)
single_menu.add_command(label="Player 1st", command=lambda: single_new(True))
single_menu.add_command(label="Computer 1st", command=lambda: single_new(False))
menubar.add_cascade(label=" 1-player ", menu=single_menu)

double_menu = Menu(menubar, tearoff=0)
double_menu.add_command(label="New game", command=lambda: double_new())
menubar.add_cascade(label=" 2-player ", menu=double_menu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Rules", command=disp_rules)
helpmenu.add_command(label=" Exit", command=main_page.quit)
menubar.add_cascade(label="Help", menu=helpmenu)

main_page.config(menu=menubar)
main_page.mainloop()
