# Name: Josh Sarath
# These functions convert to/from roman to indian/arabic numerals
# You can assume the following equivalences:
#   I 1    V 5    X 10    L 50    C 100    D 500    M 1000
# 
roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I",]
numbers = [1000,900,500,400,100,90, 50, 40,10,9,5,4,1]

def toRoman(n):
    """
    This function converts positive integer n to its roman form.
    >>> toRoman(3)
    'III'
    >>> toRoman(1762)
    'MDCCLXII'
    """
    numeral = ""
    for i in range(len(roman)):
        while n >= numbers[i]: #sort numbers
            numeral= numeral + roman[i] #add correct numeral to list
            n = n- numbers[i] #gives remaining numbers not translated to roman numerals
    return numeral    

def fromRoman(s):
    """
    Converts string s, assumed to be a roman numeral to integer
    >>> fromRoman('III')
    3
    >>> fromRoman('MDCCLXII')
    1762
    """        
    num = []
    final = 0
    for i in s:
        num.append(numbers[roman.index(i)])
    for j in range(len(num)-1):
        if num[j] >= num[j+1]:
            final += num[j]
        else:
            final -= num[j]
    final += num[len(num)-1]
    return final         

#
# The following are the standard way to ensure easy testing
#
def main():
    print('Testing...')
    import doctest
    doctest.testmod()

if __name__=='__main__':
    main()
    
