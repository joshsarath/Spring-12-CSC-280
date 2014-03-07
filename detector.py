#Josh Sarath
"""
This project simulates a detector area within a larger area. A ball is randomlly generated at a point within the area with a random direction. 
The ball will bounce off the walls until it hits the detector area or is obsorbed (a random assigned result of each bounce) with the returns being "hit" or "miss"
A turtle graphic also illustrates the movement of the ball.
"""

import random
from math import tan, radians, atan, degrees
boundary= [(0, 0), (100, 100)]
detector= [(0,0), (0,10), (10,0), (10,10)]

def randPoint(boundary):
    """
    picks a random starting point of the photon within a rectangle of size a X b
    """
    x=random.uniform(boundary[0][0], boundary[1][0])
    y=random.uniform(boundary[0][1], boundary[1][1])
    return x,y   

def randDirect():
    """
    picks a random direction for the photon to move
    """
    return random.uniform(0, 360)

def pickLine():
    """
    generates a line and angle randomly for the photon to follow
    """
    angle = randDirect()
    m = tan(radians(angle))
    x1,y1 = randPoint(boundary)
    return m, x1, y1, angle


def testBound(x1, y1, m, angle, bound):
    """
    takes the inital point x1, y1 and slope m of line and tests where it hits the boundary bound using angle as initial direction
    >>> testBound(20, 50, 1, 225, boundary)
    (0, 30)
    >>> testBound(20, 50, 1, 45, boundary)
    (70.0, 100)
    """
    if angle > 90 and angle < 270:
        x2 = bound[0][0]
        y2 = m*(x2-x1) + y1
        if y2 > bound[1][1]:
            y2 = bound[1][1]
            x2 = (y2-y1)/m + x1
        if y2 <bound[0][1]:
            y2 = bound[0][1]
            x2 = (y2-y1)/m + x1
    else:
        x2 = bound[1][0]
        y2 = m*(x2-x1) + y1
        if y2 > bound[1][1]:
            y2 = bound[1][1]
            x2 = (y2-y1)/m + x1
        if y2 <bound[0][1]:
            y2 = bound[0][1]
            x2 = (y2-y1)/m + x1
    return x2, y2    
    
def failed():
    """
    generates a number to randomly approximate photon absorbtion by the mirrors
    """
    reflect = random.randint(1, 20)
    if reflect == 1:
        return True
    else:
        return False
    
def newAngle(angle, x2, y2, boundary):
    """
    takes the intital angle and returns the mirrored angle as the photon hits the wall
    >>> newAngle(225, 0, 30, boundary)
    315
    >>> newAngle(118, 50, 100, boundary)
    208
    """  
    if angle < 90 and y2 == boundary[1][1]: #100
        new = 360- angle
    if angle < 90 and x2 == boundary[1][0]: #100
        new = 90 + angle
    if angle < 180 and angle > 90 and y2 == boundary[1][1]: #100
        new = angle - 90 + 180
    if angle <180 and angle > 90 and x2 == boundary[0][0]: #0
        new = angle - 90
    if angle < 270 and angle >180 and y2 == boundary[0][1]: #0
        new = angle - 180 + 90
    if angle < 270 and angle > 180 and x2 == boundary[0][0]: #0
        new = 360 - (angle-180)
    if angle < 360 and angle > 270 and y2 == boundary[0][1]: #0
        new = angle - 270
    if angle < 360 and angle >270 and x2 ==boundary[1][0]: #100
        new = (angle - 270) + 180
    return new


def testDetector(x1, y1, angle, detector):
    """
    Tests if photon hits detector before hitting the wall
    >>> testDetector(25, 20, 225, detector)
    ([201.80140948635182, 213.69006752597977, 218.65980825409008, 233.13010235415598], 225)
    >>> testDetector(25, 20, 45, detector)
    ([201.80140948635182, 213.69006752597977, 218.65980825409008, 233.13010235415598], 45)
    """
    angles = []
    for i in range(4):
        if detector[i][0]-x1 == 0:
            ang = degrees(atan(270))
        else:
            m = (detector[i][1]-y1)/(detector[i][0]-x1)
            ang = degrees(atan(m)) +180 #this number changes based on location of detector
        angles.append(ang)
    angles.sort()
    return angles, angle

def mirror(new):
    """
    reflects photon off border
    >>> mirror(208)
    0.5317094316614789
    >>> mirror(135)
    -1.0000000000000002
    """
    newslope = tan(radians(new))
    return newslope
    
def doesItHit(m, x, y, angle, Graphic, turtle):
    """
    tests whether the line hits or is absorbed
    >>> doesItHit(-1, 1.25, .5, 135, False, turtle)
    Hit
    1
    >>> doesItHit(-1, 25, 25, 135, False, turtle)
    Miss
    0
    >>> doesItHit(1, 25.5, 25, 225, False, turtle)
    Hit
    1
    """
    angles, angle = testDetector(x, y, angle, detector)
    if angle > angles[0] and angle < angles[3]:
        print("Hit")
        if Graphic == True:
            turtle.pendown()
            turtle.goto(detector[3])
            turtle.stamp()
        return 1
    else:
        x, y = testBound(x, y, m, angle, boundary)
        if Graphic == True:
            turtle.pendown()
            turtle.goto(x,y)
        if failed():
            print("Miss")
            if Graphic == True:
                turtle.stamp()
            return 0
        angle = newAngle(angle, x, y, boundary)
        m = tan(radians(angle))
        return doesItHit(m, x, y, angle, Graphic, turtle)
        
def fullThing(n):
    """
    the bread and butter
    """
    hits = 0
    for i in range(n):
        m, x, y, angle = pickLine()
        hit = doesItHit(m, x, y, angle, False, turtle)
        if hit != 0:
            hits += 1
    return hits

def turtle(n):
    """
    displays a graphic of the photon
    """
    import turtle
    turt = turtle.Turtle() 
    wn = turtle.Screen()
    
    for i in range(4):
        turt.fd(100)
        turt.left(90)   
    movement(n)
    
    wn.exitonclick()
    
def movement(n):
    """
    track photon movement in display
    """
    import turtle
    t = turtle.Turtle()
    for i in range(n):
        m, x, y, angle = pickLine()
        doesItHit(m,x,y,angle, True, t)
        t.penup()
        t.goto(0,0)
        
def wholeShebang(n, Graphic):
    if Graphic == False:
        return fullThing(n)
    else:
        turtle(n)

def main():
    print('Testing...')
    import doctest
    doctest.testmod()

if __name__=='__main__':
    main()

    