#Name: Josh Sarath
import turtle
wn = turtle.Screen()
a = turtle.Turtle()
wn.bgcolor("darkgreen")
a.pencolor("white")
a.pensize(5)

a.penup()
a.bk(300)
a.right(90)
a.forward(175)
a.left(90)

a.pendown()

for i in range(2):      #creates border of field
    a.forward(600)
    a.left(90)
    a.forward(350)
    a.left(90)
    
for i in ["50", "110", "140", "140", "110"]: #creates solid line markers
    i = int(i)
    a.forward(i)
    a.left(90)
    a.forward(350)
    a.right(180)
    a.forward(350)
    a.left(90)
    
b = turtle.Turtle()
b.pencolor("white")
b.pensize(3)

b.penup()
b.bk(225)
b.left(90)
b.forward(150)
b.left(90)
b.pendown()
b.forward(25)
b.right(180)
b.forward(25)

def fivemeter():
    for i in range(22):  #dotted 5m line on top
        b.penup()
        b.forward(10)
        b.pendown()
        b.forward(10)

fivemeter()        

b.penup()
b.forward(10)
b.pendown()
b.forward(25)
b.right(90)
b.forward(300)
b.right(90)
b.forward(25)

fivemeter()
    
b.penup()    
b.forward(10)
b.pendown()
b.forward(25)


c = turtle.Turtle()
c.pencolor("white")
c.pensize(3)

c.penup()
c.right(90)
c.forward(175)
c.right(90)
c.forward(50)
c.right(90)

def dottedline(): #10m line on left
    for i in range(18):
        c.pendown()
        c.forward(10)
        c.penup()
        c.forward(10)
    
dottedline() #10m line on right

c.right(180)
c.penup()
c.forward(10)
c.left(90)
c.forward(100)
c.right(90)

dottedline()


d= turtle.Turtle()
d.color("white")
d.pensize(3)
d.penup()
d.bk(250)
d.right(90)
d.forward(175)
d.right(180)

def goallinehash():
    for i in range(2):
        d.forward(75)
        d.right(90)
        d.pendown()
        d.forward(25)
        d.right(180)
        d.penup()
        d.forward(25)
        d.right(90)
        d.forward(125)
        
goallinehash()

d.penup()
d.back(50)
d.right(90)
d.forward(500)
d.right(90)

goallinehash()


e = turtle.Turtle()
e.penup()
e.color("white")
e.pensize(3)
e.bk(225)
e.right(90)
e.forward(175)
e.right(180)

def fivemeterhash(): #6 hashmarks at the 5m goal line
    e.forward(12.5)
    e.pendown()
    e.forward(25)
    e.penup()
    e.forward(25)
    e.pendown()
    e.forward(25)
    e.penup()
    e.forward(55)
    e.pendown()
    e.forward(25)
    

fivemeterhash()

def convientthing():
    e.penup()
    e.forward(182.5)
    e.right(180)
    
convientthing()    
fivemeterhash()

e.penup()
e.forward(182.5)
e.left(90)
e.forward(450)
e.left(90)

fivemeterhash()
convientthing()
fivemeterhash()

f = turtle.Turtle()
f.color("white")
f.pensize(3)
f.penup()

f.backward(140)
f.right(90)
f.forward(100)
f.left(90)

def fifteenmeter():   #15m hash marks
    for h in ("0", "90", "50", "50", "90"):
        h = int(h)
        f.forward(h)
        f.forward(12.5)
        f.pendown()
        f.right(180)
        f.forward(25)
        f.right(180)
        f.penup()
        f.forward(12.5)
        f.left(90)
        f.forward(200)
        f.right(90)
        f.forward(12.5)
        f.pendown()
        f.right(180)
        f.forward(25)
        f.right(180)
        f.penup()
        f.forward(12.5) 
        f.right(90)
        f.forward(200)
        f.left(90)
            
fifteenmeter()

g = turtle.Turtle()
g.color("white")
g.penup()
g.bk(140)
g.right(90)
g.bk(110)
g.left(90)

def line():
        g.write(i, move=False, align="center", font=("Arial", 35, "bold"))
        g.right(90)
        g.forward(250)
        g.write(i, move=False, align="center", font=("Arial", 35, "bold"))
        g.bk(250)
        g.left(90)
        
for i in ["22"]: 
        line()   
        
g.forward(90)
for i in ["10"]:
        line()

g.forward(50)
for i in ["50"]:
        line()
        
g.forward(50)
for i in ["10"]:
        line()
        
g.forward(90)
for i in ["22"]:
        line()


a.penup()
a.bk(1000)
b.penup()
b.bk(1000)
c.penup()
c.bk(1000)
d.penup()
d.bk(1000)
e.penup()
e.bk(1000)
f.penup()
f.bk(1000)
g.penup()
g.bk(1000)

wn.exitonclick()