import turtle as fort
#Assigning fuctions to variables 
a = fort.Turtle()
#Choosing my shape,color,pen and size
a.shape('turtle'),a.penup(),a.color('blue'),a.shapesize(4),fort.bgcolor('red')
#defining different movement funtions
def forward():
    a.fd(50)
    a.speed('fastest')
def backward():
    a.back(50)
    a.speed('fastest')
def left():
    a.left(45)
    a.speed('fastest')
def right():
    a.right(45)  
    a.speed('fastest')
#let the program listen and assign keys to the movement    
fort.listen()
fort.onkeypress(forward,'w')
fort.onkeypress(backward,'s') 
fort.onkeypress(left,'a') 
fort.onkeypress(right,'d')
fort.mainloop()



