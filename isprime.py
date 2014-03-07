# Josh Sarath
#
#
# This module tests integers for primality.
# An integer n is prime if if is evenly divided only by 1 and itself
# For instance 2, 3, 5, 7 are prime but 4 and 6 are not since 4 = 2*2 and 6 = 2*3
# You must implement a test. 

from math import sqrt
def isPrime(n):
    """
    Returns True or False according to whether n is prime.
    >>> isPrime(17)
    True
    >>> isPrime(18)
    False
    """
    a = 0
    for i in [2, int(sqrt(n))]:
        if n%i == 0:
            a = 1
    return a != 1
         




#
# The following are the standard way to ensure easy testing
#
def main():
    print('Testing...')
    import doctest
    doctest.testmod()

if __name__=='__main__':
    main()
