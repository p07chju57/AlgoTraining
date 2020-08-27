
def collatz(n):
    if n != 1 :
        while n != 1:
            if (n % 2) == 0:
                print(n)
                n = n / 2
            else:
                print(n)
                n = (3*n) +1
    print(n)

collatz(22)
