# Josh Sarath
# This program is a leap year calculator
def leapYear(year):
    """
    A boolean function that returns True or False according to 
    whether year is a leap year.
    >>> leapYear(2001)
    False
    >>> leapYear(2004)
    True
    """
    return year % 400 ==0 or year % 4==0 and year %100 !=0


def leapYears(startYear, endYear):
    """
    This function returns a list of boolean values, one for each
    year from startYear to endYear (inclusive) indicating whether the
    year was a leap year.
    >>> leapYears(2001,2004)
    [False, False, False, True]
    """
    list = []
    for i in range(startYear, endYear + 1):
        list.append(leapYear(i))
    return list
    
        

#
# The following are the standard way to ensure easy testing
#
def main():
    print('Testing...')
    import doctest
    doctest.testmod()


if __name__=='__main__':
    main()
