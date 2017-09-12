# first version where there are no duplicates
import sys
def magicFast(array,high,low):
    middle = (high+low)//2
    if(high < low):
        return -1
    if(array[middle]== middle):
        return middle
    elif(array[middle] > middle):
        return magicFast(array,middle - 1,low)
    else:
        return magicFast(array,high,middle+1)

if(__name__=='__main__'):
    array =[int(x) for x in input().split()] # one way of input
    print('Magic Index',magicFast(array,len(array)-1,0))
    # print('=================')
    # a2 = list(map(int,input().split(',')))
    # print(a2)
    # print(array)
