# Try and except blocks are used in Python to handle the exception.
#the except block is the same as the catch block.
'''print("Enter num 1 :")
num1 = int(input()) # Expect a number as input
print("Enter num 2 :")
num2 = int(input()) # Expect a number as input
print("Sum of these two numbers is",num1+num2)'''
# Above program will give error if input is not a number

print("Enter num 1 :")
num1 = input()
print("Enter num 2 :")
num2 = input()
try: # try it else run exception and proceed
    print("Sum of these two numbers is",
            int(num1)+int(num2))
except Exception as e:
    print(e)

print("This line is very important") #this will executive always