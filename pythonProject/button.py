from tkinter import *
root=Tk()

def leftclick(event):
    print("mouse leftbutton is clicked")

def rightclick(event):
    print("mouse right button is clicked")
def middlebuttonclick(event):
    print("mouse middle button is clicked")

btn=Button(root,text="Left click",fg="blue",bg="yellow",
           font=("Comic Sans Ms",20,'bold'))
btn.bind("<Button-1>",leftclick)
btn.pack()

btn1=Button(root,text="Right Click",fg="blue",bg="yellow",
           font=("Comic Sans Ms",20,'bold'))
btn1.bind("<button-2>',middlebuttonclick")
btn1.pack()
btn3=Button(root,text="Middle Button click",fg="blue",bg="yellow",
           font=("Comic Sans Ms",20,'bold'))
btn3.bind("<Button-3>",rightclick)
btn3.pack()
root.resizable(0,0)
root.geometry("400x400+300+150")
root.mainloop()