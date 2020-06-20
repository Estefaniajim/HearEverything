from tkinter import * 
from tkinter.ttk import *
import main
root = Tk() 
Label(root, text = 'Hear Everything', font =( 
  'Verdana', 15)).pack(side = TOP, pady = 10) 
photo = PhotoImage(file = r"mic.png") 
photoimage = photo.subsample(3, 3) 
Button(root, text = 'Click Me !', image = photoimage).pack(side = TOP)
main.wit()
mainloop() 