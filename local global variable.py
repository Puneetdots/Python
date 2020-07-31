x = 10 #Global Variable
def fun1():
    x = 5
    y = 10
    z = sum((x,y))
    print(z)

fun1()
print(x) #x is not accessible from outside of the function means print 10 not 5

a=1  #global variable

# def print_Number():
#     a=a+1;
#     print(a)
#
# print_number() #this will through error because variabe a can not change

#If you want to changes the "a" variable then use below

def print_number2():
    global a
    a = a + 5
    #print(a)
print_number2()

#other ex - function inside function
x = 89
def harry():
    x = 20
    def rohan():
        global x
        x = 88
     #print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)

harry()
print(x)