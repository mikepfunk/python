pal = input("Enter a string: ")

def isPal(pal):
    pal = pal.lower()
    pal = pal.replace(" ", "")
    
    '''return boolean is string is equal
    to its reverse.  First we make it
    the same case, then we remove spaces,
    removing spaces is optional on this
    problem.
    '''
    
    return pal == pal[::-1]

'''Slicing works like [start:stop:step]
# So [::-1] means default, default, reverse
# so its start of the word, to the end, but in reverse order.
'''

if isPal(pal):
    print(pal, "is a palindrome")
else:
    print(pal, "is not a palindrome")
    