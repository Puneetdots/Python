#1 String Formatting (% Operator)
# name="Jack"
# n="%s My name is %s" %name
# print(n)

#2 Using Tuple ()
name="Jack"
class1=5
s="%s is in class %d"%(name,class1)
#print(s)

#3  String Formatting (str.format)
str = "This article is written in {} "
print (str.format("Python"))

#4 Using f-Strings ( f ):
str1="Python"
str2="Programming"
print(f"Welcome to our {str1} {str2} tutorial")
print((f"I am learnig {str1} {str2} with code with harry channel"))
# F strings with moduel
import math
me = "Harry"
a1 = 3
a = f"this is {me} {a1} {math.cos(65)}"
# time
print(a)
