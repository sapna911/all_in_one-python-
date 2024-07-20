from tkinter import *
import time
import random
root=Tk ()
root.title("moving ball")
canvas=Canvas(root,width=800,height=600)
canvas.pack()
class Ball:
    def __init__(self,color,size):
        self.ball=canvas.create_oval(10,10,size,size,fill=color)
        self.xspeed=random.randrange(1,8)
        self.yspeed=random.randrange(1,8)

    def animate(self):
        canvas.move(self.ball, self.xspeed,self. yspeed)
        pos = canvas.coords(self.ball)
        '''

        pos=[left top right bottom]
        '''

        if pos[3] >= 600 or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= 800 or pos[0] <= 0:
            self.xspeed = -self.xspeed


movingball=[]
for i in range(50):
    movingball.append(Ball("blue",50))

while True:
    for j in movingball:
        j.animate()



    root.update()
    time.sleep(0.01)

mainloop()
