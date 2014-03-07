#Josh Sarath
import turtle
wn = turtle.Screen()
a = turtle.Turtle()

a.speed(10)
a.penup()
a.goto(-200,-200)
a.pendown()
def square():
    a.pendown()
    a.begin_fill()
    a.fd(50)
    a.left(90)
    a.fd(50)
    a.left(90)
    a.fd(50)
    a.left(90)
    a.fd(50)
    a.left(90)
    a.fd(50)
    a.end_fill()

def oddrank():
    
    for i in range(8):
        if i in [0,2,4,6]:
            a.fillcolor("dimgray")
        else:
            a.fillcolor("tan")
        square()
        a.penup()
def evenrank():
    
    for i in range(8):
        if i in [1,3,5,7]:
            a.fillcolor("dimgray")
        else:
            a.fillcolor("tan")
        square()
        a.penup()

oddrank()


a.goto(-200,-150)
evenrank()


a.goto(-200,-100)
oddrank()

a.goto(-200,-50)
evenrank()


a.goto(-200,0)
oddrank()

a.goto(-200,50)
evenrank()

a.goto(-200,100)
oddrank()

a.goto(-200,150)
evenrank()

b = turtle.Turtle()
b.speed(10)

from math import sqrt


def pawn():
    b.begin_fill()
    b.pendown()
    b.circle(5)
    b.end_fill()
    
    b.begin_fill()
    b.bk(7)
    b.right(90)
    b.fd(5)
    b.left(90)
    b.fd(14)
    b.left(90)
    b.fd(5)
    b.right(90)
    b.bk(7)
    b.end_fill()
    
    b.penup()
    b.right(90)
    b.fd(5)
    b.left(90)
    b.fd(3.5)
    b.pendown()
    
    b.begin_fill()
    b.right(80)
    b.fd(sqrt(106.25))
    b.right(100)
    b.forward(12)
    b.right(100)
    b.fd(sqrt(106.25))
    b.right(80)
    b.fd(7)
    b.end_fill()
    
    b.penup()
    b.bk(3.5)
    b.right(90)
    b.fd(10)
    b.left(90)
    b.fd(11)
    b.pendown()
    
    b.begin_fill()
    b.right(90)
    b.forward(10)
    b.right(90)
    b.fd(22)
    b.right(90)
    b.fd(10)
    b.right(90)
    b.fd(22)
    b.end_fill()
    
    b.penup()
    b.bk(9.58)
    b.left(90)
    b.fd(15)
    b.right(90)
    b.fd(50)    
 
b.penup()    
b.goto(-175,-115)

b.fillcolor("white")
for i in range(8):
    pawn()

b.penup()
b.goto(-175,135)

b.fillcolor("black")
for i in range(8):
    pawn()
    
c = turtle.Turtle()
c.speed(10)

def rook():
    c.begin_fill()
    c.pendown()
    c.left(90)
    c.fd(10)
    c.right(90)
    c.fd(5)
    c.right(90)
    c.fd(5)
    c.left(90)
    c.fd(5)
    c.left(90)
    c.fd(5)
    c.right(90)
    c.fd(5)
    c.right(90)
    c.fd(5)
    c.left(90)
    c.fd(5)
    c.left(90)
    c.fd(5)
    c.right(90)
    c.fd(5)
    c.right(90)
    c.fd(10)
    c.right(90)
    c.fd(25)
    c.end_fill()
    
    c.begin_fill()
    c.left(90)
    c.fd(10)
    c.left(90)
    c.fd(25)
    c.left(90)
    c.fd(10)
    c.left(90)
    c.fd(25)
    c.end_fill()
    
    c.penup()
    c.left(90)
    c.fd(10)
    c.left(90)
    c.fd(5)
    c.pendown()
    
    c.begin_fill()
    c.right(90)
    c.forward(15)
    c.left(90)
    c.fd(15)
    c.left(90)
    c.fd(15)
    c.left(90)
    c.fd(15)
    c.end_fill()
    
    c.penup()
    c.fd(5)
    c.right(90)
    c.fd(10)
    c.right(90)
    c.fd(350)

c.penup()
c.fillcolor("white")
c.goto(-185,-165)    
for i in range(2):
    rook()




c.penup()
c.fillcolor("black")
c.goto(-185,185)
for i in range(2):
    rook()

d = turtle.Turtle()
d.speed(10)

def knight():
    d.pendown()
    d.write("N", move= False, align = "center", font = ("arial", 40, "bold"))
    d.penup()
    d.fd(250)
    
d.penup()
d.goto(-125, -195)
d.color("white")
for i in range(2):
    knight()

d.goto(-125, 155)
d.color("black")
for i in range(2):
    knight()

d.penup()

def bishop():
    d.pendown()
    d.write("B", move= False, align = "center", font = ("arial", 40, "bold"))
    d.penup()
    d.fd(150)

d.goto(-75,-195)
d.color("white")
for i in range(2):
    bishop()
    
d.goto(-75, 155)
d.color("black")
for i in range(2):
    bishop()

d.goto(-25,-195)
d.color("white")
d.write("Q", move= False, align = "center", font = ("arial", 40, "bold"))
d.goto(-25,155)
d.color("black")
d.write("Q", move= False, align = "center", font = ("arial", 40, "bold"))

d.goto(25,-195)
d.color("white")
d.write("K", move= False, align = "center", font = ("arial", 40, "bold"))
d.goto(25, 155)
d.color("black")
d.write("K", move= False, align = "center", font = ("arial", 40, "bold"))

a.penup()
a.fd(150)
b.penup()
b.fd(100)

d.penup()
d.forward(300)


wn.exitonclick()
