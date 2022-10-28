########################################################################
# author:Logan Stelter
# date:10/28/22
# description:
########################################################################
import math
# A function that prompts the user for the minimum value and returns it
# to the calling statement. Function to also deal with range checking to
# make sure that minimum value provided is greater than 0
def minValue():
    min = float(input("What is the minimum value? "))
    if (min > 0):
        return min
    else:
        print('Minimum value should be greater than 0')
        return minValue()
# A function that prompts the user for the maximum value and returns it
# to the calling statement. Function receives argument that is used in
# range checking to make sure maximum value provided by user is greater
# than minimum value (provided in function argument)
def maxValue():
    max = float(input("What is the maximum value? "))
    if (min <= max):
        return max
    else:
        print('Maximum value should be greater than 0.')
        return maxValue()
# A function that prompts the user for the step size and returns it to
# the calling statement. Function also deals with range checking to make
# sure that step size provided is greater than 0.
def StepSize():
    step = float(input("What is the step size value? "))
    if (step > 0):
        return step
    else:
        print('Step size should be greater than 0')
        return StepSize()
# A function that receives a number as an argument and returns the log
# of that number rounded to 4 decimal places.
def logFunc(val):
    return round(math.log(val, 10), 4)
# A function that receives the value at the left size of the log table
# (i.e. the value whose logarithms should be calculated). The function
# then creates a row of logarithmic values for that argument counting
# upwards in steps of 1 significant figure more than the argument. i.e.
# if the argument is 1.3, then the row gives values of the logs for
# 1.30, 1.31, 1.32, 1.33, ..., 1.39. If the argument is 2.456, then it
# gives logs for 2.4560, 2.4561, 2.4562, 2.4563, ..., 2.4569
def firstRow(val):
    i = 0
    print(f'{val:.4f}', end = '\t')
    while i < 10:
        logVal = logFunc(val + (0.1*i))
        print(f'{logVal: .4f}', end ='\t')
        i += 1
    print('')
# A function that receives the minimum, maximum and step size as
# arguments, and prints the table (making use of the function that
# creates a single row defined earlier)
def table(min, max, steps):
    n = min
    while n <= max:
        firstRow(n)
        n += steps
    return None
####################### MAIN #########################################
# Get the minimum, maximum and step size from the user using functions
# defined earlier.
min = minValue()
max = maxValue()
steps = StepSize()
# create the table using the function defined eariler.
print('\t 0\t 1\t 2\t 3\t 4\t 5\t 6\t 7\t 8\t 9')
print('-' * 100)
table(min, max, steps)