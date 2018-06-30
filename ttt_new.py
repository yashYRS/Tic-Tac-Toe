import tkinter as tk 
from tkinter import * 
import tkinter.messagebox
from PIL import Image, ImageTk
import time 

main_page = tk.Tk()
main_page.title('Tic Tac Toe')
def makeImg(path):
	im = Image.open(path)
	im = im.resize((70,70), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(im)
	return img

x = makeImg('x.png')
o = makeImg('o.jpeg')
ph = makeImg('each_place.png')
ttt_board = []					# actually keeping track of what is going on in the game 
for i in range(9):
	ttt_board.append(9)				# value of 1 : x present , 0 : o present 

def checkwin(winner):
	if ttt_board[0] == ttt_board[4] == ttt_board[8]!=9 or \
		ttt_board[2] == ttt_board[4] == ttt_board[6]!=9 or \
		ttt_board[0] == ttt_board[1] == ttt_board[2]!=9 or \
		ttt_board[3] == ttt_board[4] == ttt_board[5]!=9 or \
		ttt_board[6] == ttt_board[7] == ttt_board[8]!=9 or \
		ttt_board[0] == ttt_board[3] == ttt_board[6]!=9 or \
		ttt_board[1] == ttt_board[4] == ttt_board[7]!=9 or \
		ttt_board[2] == ttt_board[5] == ttt_board[8]!=9 :
			main_page.destroy()
			win = tk.Tk()
			win.after(3000,win.destroy)
			Label(win,text = winner + " is winner ",font = ("Courier",30)).pack()
			win.mainloop()


def select(b,n):
	global a,buttons
	a = a+1
	if(a%2==0):
		b.configure(image = x)
		ttt_board[n] = 1
		checkwin('X')
	elif(a==9):
		main_page.destroy()
		win = tk.Tk()
		win.after(3000,win.destroy)
		Label(win,text = " It's a DRAW ",font =("Courier",30)).pack()
	else : 
		b.configure(image = o)
		ttt_board[n] = 0
		checkwin('O')
global a
a = 0 				# a keeps track of which players turn is on....

def single_new():
	main_page.destroy()
def double_new():
	main_page.destroy()
def score_see():
	main_page.destroy()	
def disp_rules():
	rules = "The objective of Tic Tac Toe is to get three in a row or column or along a diagonal." + \
	"You play on a three by three game board." + \
	" The first player is known as X and the second is O." + \
	" Players alternate placing Xs and Os on the game board until either"+ \
	" achieves that or all nine squares are filled."
	tkinter.messagebox.showinfo(" Rules of the game ",rules)

menubar = Menu(main_page)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label = "1-Player",command = single_new)
filemenu.add_command(label = "2-Player",command = double_new)
filemenu.add_command(label = "Score",command = score_see)
filemenu.add_command(label="Exit", command=main_page.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label = "Rules",command = disp_rules)
menubar.add_cascade(label="Help", menu=helpmenu)

main_page.config(menu = menubar)

but1 = Button(main_page,image = ph,fg = 'white',command = lambda:select(but1,0))
but1.grid(row = 0,column = 0)

but2 = Button(main_page,image = ph,fg = 'white',command = lambda:select(but2,1))
but2.grid(row = 0,column = 1)

but3 = Button(main_page,image = ph,fg = 'white',command = lambda:select(but3,2))
but3.grid(row = 0,column = 2)

but4 = Button(main_page,image = ph,fg = 'white',command = lambda:select(but4,3))
but4.grid(row = 1,column = 0)

but5 = Button(main_page,image = ph,fg = 'white',command = lambda:select(but5,4))
but5.grid(row = 1,column = 1)

but6 = Button(main_page,image = ph,fg = 'white',command = lambda:select(but6,5))
but6.grid(row = 1,column = 2)

but7 = Button(main_page,image = ph,fg = 'white',command = lambda:select(but7,6))
but7.grid(row = 2,column = 0)

but8 = Button(main_page,image = ph,fg = 'white',command = lambda:select(but8,7))
but8.grid(row = 2,column = 1)

but9 = Button(main_page,image = ph,fg = 'white',command = lambda:select(but9,8))
but9.grid(row = 2,column = 2)

main_page.mainloop() 
