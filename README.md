# AlgoTraining

![Alt Text](https://media.giphy.com/media/QxZ0nbcVgMlPlnfZos/giphy.gif)


🏆 Some technical challenges for practicing my problems solving skills 

This is not all the problems i solved which enonce i write in the readme
So i'll continiously update this readme 


### Exercice 1 (From CodeWars ) : Fundamentals
Convert a Number to a String!
We need a function that can transform a number into a string.

What ways of achieving this do you know?

Examples: 
number_to_string(123) returns '123' 
number_to_string(999) returns '999'

### Exercice 2 From CodeWars Fundamentals
 Given an array, find the int that appears an odd number of times.
 There will always be only one integer that appears an odd number of times.

## Exercice 3 FromCodewars Fundamentals 

Replace With Alphabet Position
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

## Exercice 4 
 A square of squares You like building blocks. You especially like building blocks that are squares. And what you
 even like more, is to arrange them into a square of square building blocks! However, sometimes, you can't arrange
 them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to
 know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building
 blocks is a perfect square. Task Given an integral number, determine if it's a square number: In mathematics,
 a square number or perfect square is an integer that is the square of an integer; in other words, it is the product
 of some integer with itself. The tests will always use some integral number, so don't worry about that in dynamic
 typed languages.
 Examples isSquare(-1) returns  false
 isSquare(0) returns   true
 isSquare(3) returns   false
 isSquare(4) returns   true
 isSquare(25) returns  true
 isSquare(26) returns  false
 
 
 ##Exercice5 
 
 There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return True if you're better, else False!

Note:
Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!

Test 

    test.describe("Basic Tests")

    test.it("better_than_average([2, 3], 5) should return True")
    test.assert_equals(better_than_average([2, 3], 5), True)

    test.it("better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75) should return True")
    test.assert_equals(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75), True)

    test.it("better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69) should return True")
    test.assert_equals(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69), True)