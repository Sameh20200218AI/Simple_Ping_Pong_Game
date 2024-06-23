from tkinter import font
import turtle
wind = turtle.Screen()
wind.title("My game ")
wind.bgcolor("black")
wind.setup(width=800,height=600)
wind.tracer(0)
# first madrab
m1=turtle.Turtle()
m1.speed(0)
m1.shape("square")
m1.color("blue")
m1.shapesize(stretch_wid=5,stretch_len=1)
m1.penup()
m1.goto(-350,0)
# second madrab
m2=turtle.Turtle()
m2.speed(0)
m2.shape("square")
m2.color("red")
m2.shapesize(stretch_wid=5,stretch_len=1)
m2.penup()
m2.goto(350,0)
# ball
b=turtle.Turtle()
b.speed(0)
b.shape("circle")
b.color("white")
#b.shapesize(stretch_wid=5,stretch_len=1)
b.penup()
b.goto(0,0)
b.dx=.16
b.dy=.16
score=turtle.Turtle()
score.speed(0)
s1=0
s2=0
score.color("greenyellow")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1 : 0  player 2 : 0 ",align=("center"),font=("courier",24,"normal"))
def m1_up():
    y=m1.ycor()

    y+=20
    m1.sety(y)
def m1_down():
    y=m1.ycor()
    y-=20
    m1.sety(y)
def m2_up():
    y=m2.ycor()
    y+=20
    m2.sety(y)
def m2_down():
    y=m2.ycor()
    y-=20
    m2.sety(y)
wind.listen()
wind.onkeypress(m1_up,"w")
wind.onkeypress(m1_down,"s")
wind.onkeypress(m2_up,"Up")
wind.onkeypress(m2_down,"Down")
while True:
    wind.update()
    b.setx(b.xcor()+b.dx)
    b.sety(b.ycor()+b.dy)
    if b.ycor()>290:
        b.sety(290)
        b.dy*=-1
    if(b.ycor()<-290):
        b.sety(-290)
        b.dy*=-1
    if(b.xcor()>390):
        b.goto(0,0)
        b.dx*=-1
        s2 = s2+1
        score.clear()
        score.write("Player 1 : {}  player 2 : {} ".format(s1,s2),align=("center"),font=("courier",24,"normal"))
    if(b.xcor ()<-390):
        b.goto(0,0)
        b.dx*=-1
        s1 = s1+1
        score.clear()
        score.write("Player 1 : {}  player 2 : {} ".format(s1,s2),align=("center"),font=("courier",24,"normal"))
    if(b.xcor()>340 and b.xcor()<350)and( b.ycor()<m2.ycor()+40 and b.ycor()>m2.ycor()-40):
        b.setx(340)
        b.dx*=-1
       
    if(b.xcor()<-340 and b.xcor()>-350)and( b.ycor()<m1.ycor()+40 and b.ycor()>m1.ycor()-40):
            b.setx(-340)
            b.dx*=-1
    #####################
    

