import turtle as fort
from random import choice
color_list = ['blue','green','red','cyan','pink','orange','yellow']
for i in range(100):
    x1 = choice(range(-200,200))
    y1 = choice(range(-200,200))
    a = fort.Turtle()
    #a.penup()
    a.color(choice(color_list))
    a.speed('slowest')
    a.goto(x1,y1)
fort.mainloop()    