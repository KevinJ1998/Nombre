from tkinter import messagebox
from tkinter import *
tk = Tk()
x = 0
y = 0
tk.title("FUTBOL")
canvas = Canvas(tk, width = 1200, height = 675)
canvas.pack()

cancha = PhotoImage(file = "campo1.gif")
canvas.create_image(0,0, anchor = NW, image = cancha)
pelota = PhotoImage(file = "ball.gif")
canvas.create_image(585,325, anchor = NW, image = pelota)

def movepelota(event):
	global x,y 
	if event.keysym == 'Up':
		canvas.move(2, 0, -3)
		y=y-3
	elif event.keysym == 'Down':
		canvas.move(2, 0, 3)
		y=y+3
	elif event.keysym == 'Left':
		canvas.move(2, -3, 0)
		x=x-3
	else:
		canvas.move(2, 3, 0)
		x=x+3

	if x == 573 or x == -576:
		messagebox.showinfo(message = "GOOOOOOL!!!", title = "MENSAJE")
	
canvas.bind_all('<KeyPress-Up>',movepelota)
canvas.bind_all('<KeyPress-Down>',movepelota)
canvas.bind_all('<KeyPress-Left>',movepelota)
canvas.bind_all('<KeyPress-Right>',movepelota)
tk.mainloop()
