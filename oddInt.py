# Given an array, find the int that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.
array = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]
#first try to get the array size


def check_if_oddor_even(num):
    for j in range(len(num)):
        odd=j%2

        print(num.count(num[j]))
        print(odd, end=" ")







print(check_if_oddor_even(array))