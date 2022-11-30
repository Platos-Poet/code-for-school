####################################################################
# author: Logan Stelter
# date: 11/9/22
# desc:  Python program that generates a list of random
# integers, the size of which is provided by the user
###################################################################
import random
# constants defined to limit the scope of the randomly generated grades.
LOWEST_GRADE = 65
HIGHEST_GRADE = 100


# A function that prompts the user for the number of students in the
# class and returns that value to the calling statement.
def studentNum():
    return int(input('How many students are in this imaginary class? '))
# A function that receives the number of students as an argument, and
# creates a list of random integers of that size. The complete list is
# returned to the calling statement.
def randList(num):
    gradeList = []
    while num > 0:
        n = random.randint(LOWEST_GRADE, HIGHEST_GRADE)
        gradeList.append(n)
        num -= 1
    return gradeList
        
# A function that receives a single grade as its argument, and returns a
# letter corresponding to the correct letter grade.
def letterGrade(num):
    if num < 70:
        return "D"
    elif 70 <= num < 80:
        return "C"
    elif 80 <= num < 90:
        return "B"
    elif num >= 90:
        return "A"
# A function that receives a list of values, and prints them in order
# separated by a tab space.
def printGrades(list):
    for i in list:
        print(f'{i}', end= '\t')
    print('')
# A function that recieves a list of numerical values (corresponding to
# the numerical grades), and creates a list of corresponding letter
# grades. This list of letter grades is then returned to the calling
# statement.
def letterGradeList(list):
    letterGradeListed = []
    for i in list:
        letterGradeListed.append(letterGrade(i))
    return letterGradeListed
# A function that recieves a list of numerical values, and returns the
# mean/average of that list.
def averageGrades(list):
    return sum(list) / len(list)
############################# main ############################

# using functions defined above, get the class size, numerical grade
# list, and letter grade list.
studentNumber = studentNum()
randomGradeList = randList(studentNumber)
print('Numerical Grades:')
printGrades(randomGradeList)
print('Letter Grades:')
printGrades(letterGradeList(randomGradeList))
# Print out both numerical and letter grades as well as the average.
print(f'The average grade for the class is {round(averageGrades(randomGradeList),1)}')