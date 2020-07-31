#print start according to the input
# n1 = int(input("Please enter the number\n"))
# b = int(input("Enter Boolen Number\n"))
# b = bool(b)
# if b == True:
#     for i in range(0,n1):
#         for j in range(0,i+1):
#             print("*",end="")
#         print("\r")
# else:
#     for i in range(n1, -1, -1):
#         for j in range(0,i+1):
#             print("*",end="")
#         print("\r")

#with function
a = int(input("please add number of line you want to print"))
b = bool(int(input("please add 0 for False")))
def star(a, b):
    if b == True:
        c = 1
        while c <= a:
            print(c * "*")
            c = c + 1
    else:
        while a > 0:
            print(a * "*")
            a = a - 1


star(a, b)