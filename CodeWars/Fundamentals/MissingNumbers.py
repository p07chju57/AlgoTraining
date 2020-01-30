#Find the missing numbers in a array of 10 elements
#first in order

elements=[1,2,3,5,6,7,8,9,10]

def findMissingOne(array):
    for i in range(len(array)-1):
        if (array[i]+1)!= array[i+1]:
            return array[i]+1
    return



print(findMissingOne(elements))