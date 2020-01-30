#Even or OddNu
#Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.


def evenOrOdd(number):
    if (number % 2) == 0:
        print("Even")
    else:
        print("Odd")


evenOrOdd(-1)