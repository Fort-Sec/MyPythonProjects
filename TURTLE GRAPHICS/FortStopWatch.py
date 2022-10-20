from traceback import format_tb
import turtle as fort
import time 

a = fort.Turtle()
#fort.pencolor('#279dd7')
b = fort.Screen()
b.title('STOP WATCH')
b.bgcolor('#279dd7')
seconds_count = 0
minute_count = 0
hour_count = 0
a.hideturtle()
a.speed(0)
def layout(hour_count,minute_count,seconds_count):
    a.clear()
    a.penup()
    a.pensize(3)
    a.goto(-80,100)
    a.pencolor('BLACK')
    a.write('STOP WATCH', font=25)
    a.goto(-100,40)
    a.pendown()
    for i in range(2):
        a.forward(140)
        a.right(90)
        a.forward(55)
        a.right(90)
    #hour count 
    a.penup()
    a.goto(-70,25)
    a.pencolor('green')
    a.write('hh')
    a.goto(-70,0)
    a.pendown()
    a.write(hour_count,font=150) 
    # :     
    a.penup()
    a.goto(-50,0) 
    a.pendown()
    a.write(':',font=150)
    # minute count
    a.penup()
    a.goto(-40,25)
    a.write('mm')
    a.goto(-35,0)
    a.pendown()
    a.write(minute_count,font=150)
    # :
    a.penup()
    a.goto(-10,0)
    a.pendown()
    a.write(':',font=150)
    # seconds count
    a.penup()
    a.goto(-0,25)
    a.write('ss')
    a.goto(-0,0)
    a.pendown()
    a.write(seconds_count,font=150)
def seconds(hour_count,minute_count,seconds_count):
    while True:
        seconds_count += 1
        time.sleep(1)
        a.undo()
        a.write(seconds_count,font=150)
        if seconds_count >= 60 :
            minute_count += 1
            seconds_count += 0
            hour_count += 0
            layout(hour_count,minute_count,seconds_count)
        if minute_count >= 60 :
            hour_count += 1
            minute_count += 0
            seconds_count += 0
            layout(hour_count,minute_count,seconds_count)
        if minute_count >= 60 :
            hour_count += 1
            minute_count += 0
            seconds_count += 0
            layout(hour_count,minute_count,seconds_count)    


layout(hour_count,minute_count,seconds_count) 
seconds(hour_count,minute_count,seconds_count)       
fort.done()