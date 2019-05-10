from tkinter import *
tk=Tk()
canvas=Canvas(tk, width=400, height=400)
canvas.pack()

my_image=PhotoImage(file="ball.gif")
canvas.create_image(50,50, anchor=NW, image=my_image)
tk.mainloop()