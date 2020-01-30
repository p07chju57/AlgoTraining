# Given an array, find the int that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.
array = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]
# first try to get the array size
for i in range(len(array)):
    print(array[i],end='')
    print(' apparait ',end='')
    print(array.count(array[i]))




