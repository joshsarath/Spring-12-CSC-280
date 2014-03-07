#
# A Monte-Carlo Simulation to estimate pi
#
# Josh Sarath
#
from math import sqrt,pi
from random import uniform


def getPoint():
    """
    gets a randomly generated point
    """
    x=uniform(0,1)
    y=uniform(0,1)
    return (x,y)

def withinCircle(x,y):
    """
    determines if the randomly generated x,y point is within the circle of diameter height of square
    """
    if sqrt(x**2 + y**2) <= 1:
        return True
    else:
        return False

def approxPi(iterations,verbose):
    """
    agregates each individual test of withinCircle to begin to approximate real area of the circle
    """
    hit = 0
    miss = 0
    if verbose == True:
        for i in range(iterations):
            x,y= getPoint()
            withinCircle(x,y)
            if withinCircle(x,y):
                z = "Hit" 
                hit = hit + 1
            else:
                z = "Miss"
                miss = miss + 1
            ratio = hit/(hit + miss)
            pi = ratio*4
            print((i), (x,y), (z), (pi)) #print out after each loop would get "verbose" for high iterations
    if verbose == False:
        for i in range(iterations):
            x,y= getPoint()
            withinCircle(x,y) 
            if withinCircle(x,y):
                hit = hit + 1
                z = "Hit"
            else:
                miss = miss + 1
                z = "Miss"
            ratio = hit/(hit + miss)
            pi = ratio*4 
    print(pi)
            
approxPi(10, False)        

def main():
    import doctest
    print("Testing...")
    doctest.testmod()

if __name__ == '__main__':
    main()

