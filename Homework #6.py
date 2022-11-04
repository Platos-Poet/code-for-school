##############################################################################
# author: Logan Stelter
# date:  11/4/22
# description: Python program that uses lists to store multiple
# names and associated ages which are provided by the user
#############################################################################

# A function that prompts the user for the number of people this program
# will be comparing.
def numNames():
    return int(input('How many people are you comparing? '))
# A function that receives the size of a list, and repeatedly prompts the user
# for that number of names. It then returns the complete list of names.
def name(n):
    print()
    person = 1
    names = []
    while n > 0:
        names.append(input(f'What is the name of person number {person}: '))
        n -= 1
        person += 1
    return names
# A function that receives the size of a list, and repeatedly prompts
# the user for that number of ages. It then returns the complete list of
# ages.
def age(n):
    print()
    person = 1
    ages = []
    while n > 0:
        ages.append(int(input(f'What is the age of person number {person}: ')))
        n -= 1
        person += 1
    return ages
################################ MAIN ################################
# Ask for the number of people using one of the functions defined above.
num = numNames()
print('----------------------------------------')
# Ask for the names of the people using one of the functions defined
# above.
nameList = name(num)
print('----------------------------------------')
# Ask for the ages of the people using one of the functions defined
# above.
ageList = age(num)
print('----------------------------------------')
# Identify the names of the youngest and oldest people in the list.
ageMax = max(ageList)
ageMaxIndex = ageList.index(ageMax)
ageMin = min(ageList)
ageMinIndex = ageList.index(ageMin)
# Display information about the lists.

print(f'{nameList[ageMinIndex]} is the youngest at {ageList[ageMinIndex]} years old')

print(f'{nameList[ageMaxIndex]} is the oldest at {ageList[ageMaxIndex]} years old')
average = sum(ageList)/len(ageList)
print(f'The average age is {round(average, 1)}')