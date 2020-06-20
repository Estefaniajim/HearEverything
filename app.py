from tkinter import * 
from tkinter.ttk import *
import main
root = Tk() 
Label(root, text = 'Hear Everything', font =( 
  'Verdana', 15)).pack(side = TOP, pady = 10) 
photo = PhotoImage(file = r"mic.png") 
photoimage = photo.subsample(3, 3) 
Button(root, image = photoimage, command = main.wit).pack(side = TOP)
main.face()
mainloop() 