import sys

def multiplication(a,b):
    smaller = a if a<b else b
    bigger = a if a>b else b
    if(smaller == 1):
        return bigger
    if(smaller == 0):
        return 0
    else:
        side1 = 0
        if(smaller%2 != 0):
            side1 = bigger
        return 2*multiplication(smaller//2,bigger)+side1

if(__name__=='__main__'):
    print(multiplication(487,767))