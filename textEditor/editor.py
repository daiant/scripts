import sys
if sys.version_info[0] == 3:
    # for Python3
    from tkinter import *
else:
    # for Python2
    from Tkinter import *
from tkinter import messagebox
#Inicia la ventana
root = Tk()
text=Text(root)
text.pack()
def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")
button = Button(root,text="Hello penelio", command= helloCallBack)
button.pack()


#Al lio
root.mainloop()
