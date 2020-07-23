# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

print("Welcome to the Python Faulty Calculator:")
print("Enter Number One")
n1 = input()
print("Enter the operator. Choices \+\-*/")
op = input()
print("Enter Number Two")
n2= input()
str = n1+op+n2
if str == "45*3":
    print("Result : 555")
elif str=="56+9":
    print("Result : 77")
elif str=="56/6":
    print("Result : 4")
elif op == "+":
    calc = int(n1)+int(n2)
    print("Result :"+ str(calc))
elif op == "*":
    calc = int(n1)*int(n2)
    print("Result :"+ str(calc))
elif op == "/":
    calc = int(n1)/int(n2)
    print("Result :"+ str(calc))
elif op == "-":
    calc = int(n1)-int(n2)
    print("Result :"+ str(calc))
else:
    print("wrong Operator")

