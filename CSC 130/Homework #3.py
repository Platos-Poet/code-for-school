#################################################################################
# name:Logan Stelter
# date: 10/12/22
# description:
#################################################################################

# A function that prompts the user for a number and returns it.
def numInut():
    num = int((input('Enter a number : ')))
    return num
# A function that receives two numbers as arguments, and returns the
# larger of the two numbers.
def isLarger(a, b):
    if a > b:
        return a
    else:
        return b

# A function that receives three numbers as arguments, and returns the
# largest of the three numbers.
def isLargest(a, b, c):
    return isLarger(isLarger(a,b), c)

# A function that receives three numbers as arguments, and returns the
# product of the two largest arguments.
def twoLargestMultiplied(a, b, c):
    secondLargest = 0
    if a > b:
        if a > c:
            largest = a
        else:
            largest = c
    else:
        if b > c:
            largest = b
        else:
            largest = c
    if largest == a:
        if b > c:
            secondLargest = b
        else:
            secondLargest = c
    if largest == b:
        if c > a:
            secondLargest = c
        else:
            secondLargest = a
    if largest == c:
        if b > a:
            secondLargest = b
        else:
            secondLargest = a
    return secondLargest * largest

# A function that receives an argument and returns a string representing
# whether that argument is even or odd.

def evenOrOdd(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
# A function that receives an argument and determines whether that
# argument is a prime number.
def primeOrNot(num):
    n = 2
    while(n < num):
        if num % n == 0:
            return False
        else:
            n += 1
    return True


##################################### MAIN PROGRAM #######################
# Functions that were defined above should be executed below in an order
# that satisfies the original problem statement. Additional statements
# can be included if needed.
##########################################################################

# Prompt for three different numbers and store them appropriately.
a = numInut()
b = numInut()
c = numInut()
# Print out the table header information and print out the table contents for each of the three numbers.
print(f'''
--------------------
Num Even Prime
--------------------
{a} {evenOrOdd(a)} {primeOrNot(a)}
{b} {evenOrOdd(b)} {primeOrNot(b)}
{c} {evenOrOdd(c)} {primeOrNot(c)}
--------------------
''')

# Print out the identity of the largest number and the largest product
# from the given numbers.

print(f'The largest number {isLargest(a, b, c)}')
print(f'The largest possible product is {twoLargestMultiplied(a, b, c)}')