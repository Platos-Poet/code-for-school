################################################################################
# Name: Logan Stelter
# Date: 10/5/22
# Description: Four functions that are kind of redundant but are called and used to print the average of two test scores
################################################################################

# defines the function nameInput()
def nameIutput():
    # sets the variable name to global because I'm lazy
    global name
    # sets the variable name to an input
    name = input(f'Please enter your name: ')
# defines the function test1Input()
def test1Iutput():
    # sets the variable test 1 to global because I'm lazy
    global test1
    # takes the input for test1 and converts it to an integer
    test1 = int(input(f'Hi {name}. What did you score on your first test? '))
# defines the function test2Input()
def test2Input():
    # sets the variable test2 to global again because I'm lazy
    global test2
    # takes the input for test2 and converts it to an integer
    test2 = int(input(f'What did you score on your second test? '))
# defines the variable average
def average():
    # prints the average of test1 and test2
    print(f'The average of {test1} and {test2} is {(test1+test2)/2}') 

# calls the function nameInput()
nameIutput()
# calls the function test1Input
test1Iutput()
# calls the function test2Input()
test2Input()
# calls the fuction average()
average()