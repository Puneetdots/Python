# Function helps in code reuseability
a = 9
b = 8
# Sum is a inbuilt function in Python
# takes tuple or list (more, general Iterables) as input
c = sum((a,b))
print(c) # Output : 17

## Example of user defined function

## The keyword def introduces a function definition.
# It must be followed by the function name and
# the parenthesized list of formal parameters.
# The statements that form the body of the function
# start at the next line, and must be indented.
def function1():
    print("You are in function one")
function1()

def function2(a,b):
    print("You are in function 2,", "Sum :", a + b)
function2(6,2)

# If we want to store value calculated by function in a variable
# We have to use return statement
def function4(a,b):
    average = (a+b)/2
    # print("Average :",average)
    return average
val = function4(15,7)
print("Average :",val)
# Output : 6.0
################ Doc strings ##################

# Used to store information about function
# """ Documentation """ or ''' Documentation '''
# # This is not a comment but docstring ...
# ...if written as first line in function
# written elsewhere in function treated as comment
def function5(a, b):
    '''This is a function which calculates average of two numbers'''
    average = (a + b) / 2
    return average


print(function5.__doc__)
# Output : This is a function which calculates average of two numbers

# docstring is helpful to know about functions
# in diiferent imported modules
# Also if we have large no. of functions
# we can use docstring to know about function




