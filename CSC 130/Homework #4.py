#########################################################################
# name: Logan Stelter
# date: 10/19/22
# description: A program that utilizes recursion as a form of repetition to print the number of
# blocks in a pyramid with the number of levels the user inputs.
#########################################################################

# A function to prompt the user for the number of levels that their
# pyramid will have and return it to the calling statement.
def levelInput():
    return int(input('How many levels will your pyramid have? '))
# A function that receives the number of pyramid levels and the number
# of blocks as arguments, and prints the appropriate results to the
# screen.
def pyramidBuilder(level, blocks):
    return level ** 2 + blocks

# A recursive function that receives the number of the level, calculates
# the number of blocks required, and returns the result to the calling
# statement.
def pyramidAssembler(level):
    ### Base Case ###
    if level == 1:
        return 1
    ### Base Case ###
    else:
        return pyramidBuilder(level, pyramidAssembler(level - 1))

################################ MAIN ################################
# using the function(s) defined above, ask the user for the number of
# pyramid levels
level = levelInput()
# using the function(s) defined above, calculate and display the final results
print(f'For {level} levels, you will need {pyramidAssembler(level)} blocks')