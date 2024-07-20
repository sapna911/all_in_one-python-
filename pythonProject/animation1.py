from tkinter import *
import time
root=Tk ()
root.title("moving ball")
canvas=Canvas(root,width=800,height=600)
canvas.pack()
ball=canvas.create_oval(10,10,60,60,fill="red")
'''for i in range(400):
    canvas.move(ball, 1, 0)

    root.update()
    time.sleep(0.01)'''''
xspeed=1
yspeed=2
while True:
    canvas.move(ball, xspeed,yspeed )
    pos=canvas.coords(ball)
    '''
    pos=[left top right bottom]
    '''

    if pos[3]>=600 or pos[1]<=0:
        yspeed=-yspeed
    if pos[2] >= 800 or pos[0] <= 0:
        xspeed = -xspeed

    root.update()
    time.sleep(0.01)

mainloop()