#Replace With Alphabet Position
#Welcome.In this kata you are required to, given a string, replace every letter with its position
# in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
#check prime number between 500 and 5000

def checkPrimeNumber():
    count=0
    for n in range(500,5001):
        if n>1:
            for i in range(2,n):
                if (n%i)==0:
                    break
            else:
                count=count+1
    print(count)

checkPrimeNumber()
